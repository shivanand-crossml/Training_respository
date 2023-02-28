# Variables, Data Types, and Operators 

#Strings
string1 = 'Python programming'
print(string1)
#various operation in the string 
print(string1[1:4])
str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)




#set declared in python
x =  set(map(int,input().split()))
print(x)
numbers = {21, 34, 54, 12}
# using add() method
numbers.add(32)
print(numbers)
#update method 
x.update(numbers)
print(x)
   


#tuple declare in python 
tuple_data =  tuple(map(int,input().split()))
print(tuple_data)
print(tuple_data[4])
print(tuple_data.count('1'))
print(tuple_data.index(5))




#list declared in python 
my_list  =  list(map(int,input().split()))
print(my_list)
print(my_list[2:5])

print(my_list.append('django'))


# dictionary declared in the python 
mydictionary = { 'python': 'data science', 'machine learning' : 'tensorflow' , 'artificial intelligence': 'keras'}
print(mydictionary['machine learning'])
print(mydictionary.get("python"))

#for loop in python

for key,values in mydictionary.items():
    print(key)
    print(values)


for data in mydictionary.values():
    print(data,"####################################")
    


#condional statement
a =  30 
b = 40
if a>b:
    print("this is greater")
else:
    print("this is smaller ")
    
    
if a!=b:
    print("this is work done")
else:
    print("I am done work")
    
#while loop
i = 1
while(i<6):
    print("this is while loop")
    if (i==3):
        print("while loop execute")
        break
    i = i+1
print("execute")


#funtion in the python

def data_funtion(x,y):
    print("Hello from a function")
    print(x+y)
    
data_funtion(5,6)

# Lambda funtion in python

def lamda_define(a,b):
    return lambda a,b:a*b
data  = lamda_define(5,8)
print(data)

#Integer input in Python 

num = int(input("Enter a number: "))
add = num + 1
print(add)