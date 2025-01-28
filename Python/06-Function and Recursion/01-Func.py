# A function is a block of reusable code that perform in organising code and reducing redundancy.

#syntax

def function_name(parameter):
    #code block
    return value #optional

#Example
def greet(name):
    return f"Hello, {name}!"
print(greet("Samiul")) 


"""
2.Types of function
    A.Build in function- predefined in python(eg. print(), len(), max())

    B.User-defined function - created by user to perform specific tasks

    C.Lambda function- Anonymous, single-line function
"""

#example of lambda funtion
square = lambda x: x * x
print(square(5))  # Output: 25


def describe_pet(animal, name="Buddy"):
    print(f"I have a {animal} named {name}.")

describe_pet("dog") 
describe_pet("cat", "Whiskers") 

