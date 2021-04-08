import math
import sys

import pyspark

from digit_extraction import pi_bbp

N = 1
if len(sys.argv) >= 2:
    N = int(sys.argv[1])

spark = pyspark.sql.SparkSession.builder \
    .appName("pi spark") \
    .getOrCreate()

df = spark.sparkContext \
    .parallelize(range(N), numSlices=int(math.sqrt(N))) \
    .map(pi_bbp) \
    .zipWithIndex().cache()

hex2char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

for n in range(N):
    d = df.filter(lambda pair: pair[1] == n) \
        .map(lambda pair: pair[0]) \
        .collect()[0]
    print(f"{hex2char[d]}")
