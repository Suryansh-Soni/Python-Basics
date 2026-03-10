# Problem 6: Write a generator fun taht yields even number 
def even_generator(n):
    for i in range(2,n+1,2):
        yield i # keep the values in the memory 
#         print(i)
# even_generator(10)

for i in even_generator(10):
    print(i)

 

