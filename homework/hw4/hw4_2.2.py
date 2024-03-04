#homework 4 question 2.2:

lis = [2, 3, 4]
def square(lis):
    return [i ** 2 for i in lis]
print([i ** 2 for i in lis])

#returns [4, 9, 16]
#tried to use square = pow(x ,y) but error came up that it is the incorrect operand type. Fixed this by using a different command since pow() and ** doesn't like lists
#tried to return(len(square)) but error say object of type 'int' has no len(), so just removed len(). Additional fix: used return statement and then a print statement for same purpose
#referrenced StackOverflow for code "def square(lis): return [i ** 2 for i in lis]" 
#this code allows for each value within lis to be reassigned the value i ** 2, which squares the entire list.
#link for source:
#https://stackoverflow.com/questions/12555443/squaring-all-elements-in-a-list