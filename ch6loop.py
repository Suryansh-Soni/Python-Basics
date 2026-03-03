# n=5
# for i in range (n):
#     print(i)
# while n>0:
#     print(n)
#     n-=1

for num in range(1, 101):
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            print(num)
            break
