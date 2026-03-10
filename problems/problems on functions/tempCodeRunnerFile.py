def print_(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
print_(power="lazer",name="superman",enemy="dr doom")