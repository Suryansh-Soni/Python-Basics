# # base: if no mode mentioned read is default
# r-read,w-write,a-append,x-create file if not exist,
# t-text mode,b-binary mode ,a+ - read and write mode,
# w+ - read and write mode, r+ - read and write mode
# # Read:
# file=open("file-handling.txt","r")
# data=file.read()
# print(data)

# #  Q) is word handling is in file or not
# if "handling" in data:
#     print("word handling is in file")

# # Write:
# file=open("file-handling.txt","w")
# file.write("This is file handling in python")
# file.close() # it will give error because we have opened file in write mode

# file=open("file-handling.txt","r")
# data=file.read()    
# print(data)

# # Append:
# file=open("file-handling.txt","a")
# file.write("\nThis is append mode") 
# file.close()
# file=open("file-handling.txt","r")
# data=file.read()    
# print(data)

# #  working with with keyword file autoclode :
# with open("file-handling.txt","r") as f:
#     data=f.read()
#     print(data)
# .read:read entire file, .readline: read one line at a time if no line left it will return empty string, 
# .readlines: read all lines and return list of lines

# copy delete,rename file
# copy used shutil module,delete used os module,rename used os module

# import shutil
# import os
# # copy file
# shutil.copy("file-handling.txt","copy-file-handling.txt")
# with open("copy-file-handling.txt","r") as f:
#     data=f.read()
#     print(data)
#     f.close()
# # rename file
# os.rename("copy-file-handling.txt","renamed-file-handling.txt")
# with open("renamed-file-handling.txt","r") as f:
#     data=f.read()
#     print(data)
#     f.close()
# # delete file
# os.remove("renamed-file-handling.txt")


# write try except block to handle file not found error
try:
    with open("file-handling.txt","r") as f:
        data=f.read()
        print(data)
except FileNotFoundError:
    print("File not found")