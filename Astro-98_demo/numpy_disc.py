import numpy as np
import time 

def function(num):
    return num**2

def loop_speedtest(n):
    start = time.time()
    print(start)
    result = list(range(n))
    for i in result:
        result[i] = function(result[i])
    end = time.time()#takes the time
    print(end)
    return end - start #returns the time passed from start of function to end of function

def numpy_speedtest(n):
    start = time.time()
    print(start)
    result = np.arange(n)
    result = function(result)
    end = time.time()
    print(end)
    return end - start

reps = 100
#print(loop_speedtest(reps))
#print(numpy_speedtest(reps))

##
## Find the unique elements in an array and the number of each element
## [10, 2, 5, 10, 8, 2, 9, 8]
## Expected output: [2, 5, 8, 9, 10], [2, 1, 2, 1, 2]


myArray = np.array([10, 2, 5, 10, 8, 2, 9, 8])
def unique(n):
    return np.unique(myArray, return_counts = True)

#print(np.unique(myArray, return_counts = True))
#for more info about these array commands and how they work : https://numpy.org/doc/stable/reference/generated/numpy.unique.html

#last wednesday Megan talked about how to index thru a 2D array (can that be used on homework4?)

## Given a 2D array, find the mean of each of the columns and replace each element less than the column's mena with the mean

##  ([[34, 37, 29],
##   [1,  36, 41],
##   [37, 34, 29],
##   [1,  49, 14]])

myArray = np.array([[34, 37, 29], [1,  36, 41], [37, 34, 29], [1,  49, 14]])
means = np.mean(myArray, axis = 0)
for i in range(myArray.shape[1]):
    myArray[:,i][myArray[:,i] < means[i]] == means[i]
#the : means skip over the rows and go to columns
print(myArray)
