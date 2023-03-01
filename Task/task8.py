import re
import os
def file_data(filepath):
    data = filepath.read()
    lst = re.findall('\S+@\S+', data)
    print(lst) 
    file1 = open("output.txt","w")
    file1.write(str(lst))
    return data
filepath = open("input.txt")

print(file_data(filepath))