#homework 4 question 2.1

listfifty = [0]
for i in listfifty :
    if i < 50:
        listfifty.append(i := i + 1)
print(listfifty)

#output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
#Errors encountered:
#SyntaxError: had to switch from listfifty.append[(i = i + 1)] to listfifty.append[(i := i + 1)]. The error told me to try that
#says listfifty.append[(i := i + 1)] is not subscriptable. removed (). Still says not subscriptable. Hmm. changed [] to (). That worked.
#Code kept running without stopping = infinite loop. Added in line 5 and it works now :) slay