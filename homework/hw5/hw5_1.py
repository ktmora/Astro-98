
import numpy as np

arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])

print(arr[0])

def findEqual( a ) :
    i = arr[0]
    for j in range(len(i)) : 
        if a.all(arr[i]) == j :
            return True
        i += i
        j += j

print(findEqual(arr))
