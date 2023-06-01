def my_kwargs(**kwargs):
    print(kwargs)

my_kwargs(a=1, b=2, c=3)
my_kwargs()


def my_kwargs(**kwargs):
    for i,j in kwargs.items():
        print("{}:{}".format(i,j))

my_kwargs(a=1, b=2)