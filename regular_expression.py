import re

text = "this is shivanand"
data = re.search("this",text)
print(data)

#find all the string
data1 =  re.findall("is",text)
print(data1)

#split the string 
data2 =  re.split("\s",text)
print(data2)


#Replace every white-space character with the number 9:

x = re.sub("\s", "9", text)
print(x)
