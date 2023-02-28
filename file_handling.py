import os
file  = open("text.txt",'r')


#read the file
print(file.read())
for data in file:
    print(data)


#write some content in the file
# file  = open("text.txt",'w')
# file.write("This is the write command")
# file.write("It allows us to write in a particular file")
# file.close()


#append mode to add the data in file mode 
file_1 = open('geek.txt', 'r')

data =  file_1.readlines()
for line in data:
	word = line.split()
	print(word)
        
def create_file(filename):
    try:
        file_data = open(filename,'w')
        file_data.write("hello world data are find")
        print("File  created successfully.")
    except IOError:
        print("Error: could not create file " + filename)
    
def read_file(filename):
    try:
        read_file = open(filename,'r')
        read_data =  read_file.readlines()
        for reads in read_data:
            data_row = reads.split()
            print(data_row)
    except:
        print("Error: could not create file " + filename)      

def append_file(filename,text):
    try:
        append_file =  open(filename,'a')
        append_file.write(text)
        print("Text appended to file " + filename + " successfully.")
    except:
        print("Error: could not append to file " + filename)
def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)


def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)

        
if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"
 
    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    rename_file(filename, new_filename)
    delete_file(new_filename)
