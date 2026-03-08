# sum of even number 
sum=0
n=10
for i in range(1,n+1):
    if(i%2==0):
        sum+=i
print(f"Sum of even number till {n} is {sum}")