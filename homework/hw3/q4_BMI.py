#homework 3 question 4 : BMI function

height =  1.67  #meters
weight =  70   #kilograms

def BMI(height, weight) : 
    x = height
    y = weight
    BMI = y / ( x ** 2 )  
    print(BMI)
    if BMI < 18.5 : 
        return 'unhealthy'
    elif BMI >= 18.5 and BMI <= 24.9 :
        return 'healthy'
    elif BMI > 24.9 and BMI <= 29.9 :
        return 'overweight'
    elif BMI >= 30.0 :
        return 'obsese'
print (BMI(height, weight))   

#Returns: 25.099501595611173 overweight
#I wasn't sure how much this question wanted us to put, but I saw that there were categories. 
#Got the category idea from : https://www.geeksforgeeks.org/program-to-calculate-bmi/ 
#Everything in my function is my own code, but I did briefly see the idea first of Geeks for Geeks^. 
#I got the BMI categories from the CDC : https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html
