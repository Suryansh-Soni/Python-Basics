# # function : make the code more readable and reusable
#  reduce redundancy and make the code more organized

# def add(a,b):
#     return a+b

# # function call
# result=add(3,4)
# print(result)

# def welcome():
#     print("welcome to python programming"*3) 

# welcome()

import string


def con_vov(string):
    vowels="aeiouAEIOU"
    vovcount =0
    for char in string:
        if char in vowels:
            vovcount+=1
    return vovcount ,len(string)-vovcount

strings="hello world"
print("the vovwl count aand consonant count is ",con_vov(strings))