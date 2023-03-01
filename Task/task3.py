#Write a Python program that generates a list of 10 random integers between 1 and 100.

import random

data= list(range(1,100))
print(data[1:11])
 
rand_list=[]
n=10
for i in range(n):
    rand_list.append(random.randint(3,9))
print(rand_list)

num  = int(input())
list1 = []
while(num>50):
    list1.append(num)
    print(list1)
    break


