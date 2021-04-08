import sys

import pyspark

from digit_extraction import pi_bbp

N = 1
if len(sys.argv) >= 2:
    N = int(sys.argv[1])

spark = pyspark.sql.SparkSession.builder \
    .appName("pi spark") \
    .getOrCreate()

df = spark.sparkContext\
    .parallelize(range(N))\
    .map(pi_bbp)
hex2char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
for d in df.collect():
    print(f"{hex2char[d]}")

