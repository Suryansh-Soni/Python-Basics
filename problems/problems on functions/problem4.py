# problem 4: in a function take multiple inputs 
def sum_all(*args): # make all input values in a tupple 
    return sum(args)

def sums(*args):
    for i in args:
        print(i*2)
    return sum(args)
print(sums(1,2,3,4,5))