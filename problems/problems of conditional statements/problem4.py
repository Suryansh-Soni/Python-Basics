# password strength checker 
password="vkjij2022"
if(len(password)<6):
    strength ="week"
elif(len(password)<=10):
    strength="medium"
else:
    strength="strong"
print(strength)