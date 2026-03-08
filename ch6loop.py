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


# iteration tool: for ,comprehensions
# iterable objects: lists tupple files etc.
# open   file as f , here f is iterable but list =[1,2,3] list is not 
# __nest__(), i=iter(list) here i is iterable then i.__next__() giev op 1 i.__next__()->2 and so on  next(I) same 