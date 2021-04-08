import ctypes
import multiprocessing as mp
import os
import queue
from typing import List, Callable, Any, Iterator, Optional

Packet = Any
Mapping = Callable[[Any, ], Any]


def pipeline(
        data_in: Iterator[Packet],
        mapping_list: List[Mapping],
        queue_size_list: List[int],
        parallel_list: Optional[List[int]] = None,
        timeout: float = 60.0,
) -> Iterator[Packet]:
    """
    :param data_in: the iterator that yields input packets
    :param mapping_list: the list of mappings
    :param parallel_list: the list of number of processes for each mapping
    :param queue_size_list: the list of sizes of connecting queues
    :param timeout: the timeout for each mapping
    :return:
    """
    # preprocess
    num_mappings: int = len(mapping_list)
    if parallel_list is None:
        num_cpus = os.cpu_count()
        if num_cpus is None:
            num_cpus_each = 1
        else:
            num_cpus_each = num_cpus // num_mappings
        parallel_list = [num_cpus_each for _ in range(num_mappings)]

    # main
    queue_list: List[mp.Queue] = [mp.Queue(queue_size_list[i]) for i in range(len(queue_size_list))]
    process_list: List[List[mp.Process]] = []
    running: mp.Value = mp.Value(ctypes.c_bool, True)
    count: mp.Value = mp.Value(ctypes.c_int, -1)

    def process_func(mapping: Mapping, queue_in: mp.Queue, queue_out: mp.Queue, running: mp.Value):
        while True:
            try:
                packet_in: Packet = queue_in.get(timeout=timeout)
                packet_out: Packet = mapping(packet_in)
                queue_out.put(packet_out)
            except queue.Empty:
                if not running.value:
                    break

    # start processes
    for idx in range(num_mappings):
        mapping = mapping_list[idx]
        queue_in = queue_list[idx]
        queue_out = queue_list[1 + idx]
        process_list.append([])
        for _ in range(parallel_list[idx]):
            process_list[-1].append(mp.Process(target=process_func, args=(mapping, queue_in, queue_out, running)))
            process_list[-1][-1].start()

    # put input and yield output
    def feed_in_func(data_in: Iterator[Packet], queue_out: mp.Queue, count: mp.Value):
        c = 0
        for packet in data_in:
            queue_out.put(packet)
            c += 1
        count.value = c

    feed_in_process = mp.Process(target=feed_in_func, args=(data_in, queue_list[0], count))
    feed_in_process.start()
    c = 0
    while True:
        try:
            packet_out: Packet = queue_list[-1].get(timeout=timeout)
            yield packet_out
            c += 1
        except queue.Empty:
            if count.value == c:
                running.value = False
                break
    # join
    feed_in_process.join()
    for idx in range(num_mappings):
        for process in process_list[idx]:
            process.join()


if __name__ == "__main__":
    import time


    def data_in_func():
        for i in range(100):
            yield i


    data_in = data_in_func()


    def f1(x):
        time.sleep(0.1)
        return x + 0.1


    def f2(x):
        time.sleep(0.2)
        return x + 0.2


    def f3(x):
        time.sleep(0.3)
        return x + 0.3


    t1 = time.time()
    data_out = pipeline(
        data_in=data_in,
        mapping_list=[f1, f2, f3],
        parallel_list=[4, 4, 4],
        queue_size_list=[10, 10, 10, 10],
        timeout=1.0,
    )

    for i in data_out:
        print(i)
    t2 = time.time()
    print(f"elapsed time: {t2 - t1}")
