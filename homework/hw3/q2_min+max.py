
#nums = [1,2,3,4,5,6]
nums = [2, 5, 7, 3, -34, 4, 8, 27, 10]
def minMax(x):
    tupleOne = tuple(nums)
    tupleTwo = (min(tupleOne), max(tupleOne))
    return tupleTwo
print ( 'min and max of the list are', minMax(nums) )

#Returns "min and max of the list are (-34, 27)"
#Also looked up how to create a tuple out of a list on : https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/ 
#Also looked at proper syntax for the print statement on Stack: https://stackoverflow.com/questions/3136059/getting-one-value-from-a-tupleclea
#But the rest of the code above is mine :)
