 with open('example.txt','r') as file:
     content = file.read()
     print(content)

# with open('write.txt','w') as file:
#     file.write("i am lahari\n")
#     file.write("hey are you happy")

# with open('append.txt','a') as file:
#     file.write("my village\n")
#     file.write("my city")

# data=b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
# with open('example.bin','wb') as file:
#     file.write(data)

# w+ mode is used to open a file for both writing and reading. If the file does not exist, it will be created. If the file already exists, its contents will be truncated (i.e., erased) when opened in 'w+' mode.
# and seek is used to move the file pointer to a specific position in the file. It allows you to read or write data from a specific location in the file.
with open ('example.txt','w+') as file:
    file.write("hello world\n")
    file.write("this is a new line\n")

    file.seek(3)

    content=file.read()
    print(content)

#  current working directory
import os
cwd=os.getcwd()
print(f"Current working directory: {cwd}")

# mkdir creating the folder in the current working directory
# new_directory = "pakage"
# os.mkdir(new_directory)
# print(f"Directory '{new_directory}' create")

# (.) is used to represent the current directory in a file path.
# It is a shorthand notation that refers to the directory where the script or command is being executed. For example, if you are in the directory /home/user/project and you use ./file.txt, it refers to the file.txt located in the /home/user/project directory.

items=os.listdir('.')
print("Items in the current directory:")
print(items)

##joining paths
#see

dir_name="folder"
file_name="file.txt"
full_path=os.path.join(dir_name, file_name)
print(f"Full path: {full_path}")

#see
dir_name="folder"
file_name="file.txt"
full_path=os.path.join(dir_name, file_name)
print(full_path)

#exist
path="example.txt"
if os.path.exists(path):
    print(f"The path '{path}' exists.")
else:
    print(f"The path '{path}' does not exist.")

if os.path.isfile(path):
    print(f"The path '{path}' is a file.")
elif os.path.isdir(path):
    print(f"The path '{path}' is a directory.")
else:
    print(f"The path '{path}' is neither a file nor a directory.")


##getting absolute path(example.txt is the file name)
relative_path = "example.txt"
absolute_path = os.path.abspath(relative_path)
print(absolute_path)

