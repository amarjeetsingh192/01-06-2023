dict_a = {"name": "raj","age": 25 }
"""for i in dict_a.keys():
    if  i == "name":
        del dict_a

print(dict_a)"""


def my_kwargs(**kwargs):
    for i,j in kwargs.items():
        print("{}:{}".format(i,j))

my_kwargs(a=1, b=2)