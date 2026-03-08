# prime number checker
import math


n=7
isprime=True
for i in range (2,math.floor(math.sqrt(n))+1):
    
    if(n%i==0): 
        isprime=False 
        break
if(isprime):
    print(f"The numebr {n} is Prime.")
else:
    print(f"The number {n} is not a Prime number.")
