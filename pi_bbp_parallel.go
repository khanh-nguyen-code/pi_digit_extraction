package main

import (
	"flag"
	"fmt"
	"github.com/khanhhhh/pi_digit_extraction/digit_extraction"
	"math/big"
	"runtime"
)

func main() {

	var one = big.NewInt(1)
	var zero = big.NewInt(0)
	var hex2char = [16]string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"}

	flag.Parse()
	args := flag.Args()
	var N = big.NewInt(1)
	if len(args) >= 1 {
		temp, ok := (&big.Int{}).SetString(args[0], 10)
		if ok {
			N = temp
		}
	}

	var maxConcurrent = runtime.NumCPU()

	// digit channel, it holds (<-chan int) containing the result
	var digitChan = make(chan (<-chan int), maxConcurrent)

	// notify channel, send into it a struct{}{} to notify scheduler to start a worker
	var notify = make(chan struct{}, maxConcurrent)

	var workerFunc = func(n *big.Int, result chan int, notify chan struct{}) {
		result <- digit_extraction.PiBPP(n)
		close(result)
		notify <- struct{}{}
	}

	var schedulerFunc = func() {
		var n = big.NewInt(0)
		for n.Cmp(N) == -1 {
			<-notify
			result := make(chan int, 1)
			arg := (&big.Int{}).Add(n, zero)
			go workerFunc(arg, result, notify)
			digitChan <- result
			n = n.Add(n, one)
		}
		//close(notify)
	}
	go schedulerFunc()

	for i := 0; i < maxConcurrent; i++ {
		notify <- struct{}{}
	}
	var n = big.NewInt(0)
	for n.Cmp(N) == -1 {
		result := <-digitChan
		digit := <-result
		fmt.Println(hex2char[digit])
		n = n.Add(n, one)
	}
	close(notify)
	close(digitChan)
}
