#homework 4 question 4

lis = [1, 1, 2, 3, 4, 4]
def removeDuplicates(lis):
    lis = list(dict.fromkeys(lis))
    return lis
print(removeDuplicates(lis))

#Returns: [1, 2, 3, 4]
#code on line 5 from: https://www.w3schools.com/python/python_howto_remove_duplicates.asp 
#lis = list(dict.fromkeys(lis)) rewrite lis as a dictionary with keys with the same values as the entries in lis
#this is because dictionaries do not allow for duplicate values, so rewriting as a dict will automatically remove any dups
#then the outter list() command switches lis back to a list from a dict, since the problem asks to return it as a list
#thus the list that is return has values taken from the keys in the dict, which do not have any duplicate values
#errors: first run returned the original list because my print statement was print(lis), fixed by changing print statement to print(removeDuplicates(lis))
