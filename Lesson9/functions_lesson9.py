def hello():
    print("Hello world!")
    
hello()

def sum(num1 = 0, num2 = 0):
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

total =  sum()
print(total)

# When you don't know how many argument will be passed into your function

def multiple_items(*args):
    print(args)
    print(type(args))
    
multiple_items("Sadiq", "John", "Sara")

# function with key word arguments
def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
multi_named_items(first = "Sadiq", last ="Abdulrahaman")
