#homework 3 question 3 : leap year
# let y = year
y = 2000
def leapYear(x) :
    if y % 400 == 0 :
        return True
    elif y % 100 == 0 : 
        return False
    elif y % 4 == 0 : 
        return True
    return False
print( (y), 'is a leapyear =', leapYear(y) ) 

#Return : 2000 is a leapyear = True

#I originally had the code below:
"""y = 2024
def leapYear(x) :
    if y % 4 != 0 :
        return False
    elif y % 400 != 0 :
        return False
    elif y % 4 == 0 :
        return True
    elif y % 100 == 0 and y % 400 == 0 : 
        return True
    elif y % 100 == 0 :
        return False 

print( (y), 'is a leapyear =', leapYear(y) ) """

#Which didn't work, but I used StackOverflow to cut out parts of my code to make it work. I had the correct commands but not in the right order.
# Site : https://stackoverflow.com/questions/11621740/how-to-determine-whether-a-year-is-a-leap-year
#It was mostly the order and I had a lot of unnecessary commands. Instead of doing all the elif statements if it is not true, I put return False
#at the bottom so that instead of returning 'None' it will return 'False' for all statements that are not True.
#The code order goes 400, 100, and then 4 because those are the order in which they are most applicable. All leap years are divisible by 400,
#but they are not divisible by 100 unless they are divisible by 400, which is why 400 much come first. Then if they aren't divisible by 100 it
#will return false, which is why the second elif statement is 100. 
#The last elif statement is 4 because that is most applicable to every year, so if that were put first then some years would be classified wrongly.
#This order is very specific because python will stop running once it reaches an if/elif statement that is true (not True in the same sense that I
# set it as True). 