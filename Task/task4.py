#Write a Python function called calculate_average that takes a list of numbers as an argument.
def Average_number(l): 
    avg = sum(l) / len(l) 
    return avg
  
my_list = list(map(int,input().split()))
average = Average_number(my_list) 
  
print("Average of the number", average)