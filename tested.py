x =  set(map(int,input().split()))
print(x)
for data in x:
    print(data)
   
    

#
mydictionary = { 'python': 'data science', 'machine learning' : 'tensorflow' , 'artificial intelligence': 'keras'}
print(mydictionary['machine learning'])
print(mydictionary.get("python"))

for key,values in mydictionary.items():
    print(key)
    print(values)


for data in mydictionary.values():
    print(data,"####################################")
    

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
    

i = 1
while(i<6):
    print("this is while loop")
    if (i==3):
        print("while loop execute")
        break
    i = i+1
print("execute")



def data_funtion(x,y):
    print("Hello from a function")
    print(x+y)
    
data_funtion(5,6)

def lamda_define(a,b):
    return lambda a,b:a*b
data  = lamda_define(5,8)
print(data)