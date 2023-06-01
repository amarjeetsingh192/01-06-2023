def greet(arg1 = "Hi", arg2 = "raj"):
    print(arg1 + " " + arg2)

data = ["Hello", "Ramu"]
greet(*data)


def greet(arg1, arg2):
    print(arg1 + "_" + arg2)

data = ["Hello", "Ramu"]
greet(*data)


def greet(arg1 = "Hi", arg2 = "raj"):
    print(arg1 + " " + arg2)

data = {"arg1":"hello","arg2":"RAM"}
greet(**data)