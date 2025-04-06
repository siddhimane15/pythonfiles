from scipy import stats
import numpy as np

list = [10,17,22.5,22.5,9,9,17,17,19,0.5]
mean = sum(list)/len(list)
print(mean)

mode= stats.mode(list)
print(mode)

median=np.median(list)
print(median)