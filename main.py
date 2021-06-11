import csv
import rich
import colorama
import math
import numpy as np
from scipy import stats
colorama.init(autoreset=True)
rows = 0
heights = []
with open('data.csv', newline='') as csvfile:
    csvread = csv.reader(csvfile)
    for row in csvread:
        rows += 1
        heights.append(row[1])
heights.pop(0)
rich.inspect(heights, title='Heights')
val = 0
for height in heights:
    val = val + float(height)
mean = val/len(heights)
print(colorama.Fore.GREEN+"Mean = "+ str(mean))
if len(heights) % 2 == 0:
    qwerty = float(heights[12501]) + float(heights[12502])
    median = qwerty/2
    print(colorama.Fore.GREEN+"Median = "+ str(median))
rheights = []
for height in heights:
    rheights.append(math.ceil(float(height)))
print(colorama.Fore.GREEN+"Mode = "+ str(stats.mode(rheights)[0]))
