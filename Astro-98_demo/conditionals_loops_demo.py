#compare x with 10
x = 10
if (x > 10): 
    print("x is greater than 10")
elif (x==10):
    print("x is equal to 10")
else:
    print("x is less than 10")

#while loop
i = 10
while i > 0:
    print(i)
    i -= 1 #notation same as i = i - 1

for i in range(1,11):
    print(i)

#sum of the numbers 1-10
count = 0 #initializes the value of your sum
for i in range (1,11):
    count +=i 
print(count)
