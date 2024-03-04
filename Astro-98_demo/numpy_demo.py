import numpy as np

#add two arrays and add two lists

#sum of two lists
ls1 = [1, 2, 3]
ls2 = [4, 5, 6]

print(f'{ls1+ls2}')

#sum of two arrays; an array is like a mini function

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = arr1 + arr2
print(arr3) #or you could use this print command instead: print(f'Adding two arrays: {arr1 + arr2}')

#product of a scalar and an array
arr1 = 2
arr2 = np.array([4, 5, 6])
arr3 = np.dot(arr1, arr2)
print(f'Product of arr1 and arr2: {arr3}')
#output: [8, 10, 12]. idea found from https://datagy.io/numpy-python-dot-product/#:~:text=Let%E2%80%99s%20break%20down%20what%20we%E2%80%99ve%20done%20here%3A%201,value%20in%20the%20original%20array%20and%20the%20scalar.

#take a sum of numbers 1 thru 100 with both a for loop and an array
sum = 0
def forloop():
    for i in range(1, 101, 1):
        sum += i
    return(forloop(sum))

def arraySum():
    #takes the sum of the numbers 0 to 100 using numpy
    x = np.arange(101) #don't need to put (0,101) bc python assumes you start at 0 and uses a step of 1
    return(np.sum(x))
# you can also do this all in one line as: return np.sum(np.arrnage(101))
# expected output: 5050


