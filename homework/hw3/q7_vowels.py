#homework 3 question 7 : Vowels

myString = 'Is the universe just a really thin soup? They did call the infant universe a primoridal soup... '


def vowels(x) :
    v = 0
    for vowel in myString : 
        if vowel in "aeiouAEIOU" : 
            v = v + 1 
    return v
print(vowels(myString))

#Expected output : 30
#Returns : 30
#Originally I tried to write my code in one line but I wasn't sure what command would allow me to put all of the variables in one arguement.
#I had something similar to the code above written in one line, but it didn't work and this was easier. I got the format from Stack : https://stackoverflow.com/questions/35377013/python-counting-vowels-from-list
#If I were to write it in one line though, I now realize you can use the sum command. Also, I didn't know you could use the statement "if vowel in 'aeiouAEIOU' : " 
#Essentially the above code works by going through the string somewhat similar to how it indexes through a list, and everytime there is a vowel of aeiou or AEIOU, 
#It will add one to the value v, which stands for vowel, and then returns v as the vowel count in the string. 
