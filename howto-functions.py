# how to work with functions in python a basic overview
# this fucntion below will simply print out Hello in the console.
def showHello():
    print("Hello")

showHello()

# we can add variables to functions to be used as arguments see example below
# this one will take 1 string as an argument and then add that to the final print function
def showHello_2(name):
    print("Hello, ", name, " Nice to meet you")

showHello_2("Lebron James") # say hello

# function with multiple arguments
# we can use any data type for each for example number, string even lists can be passed it

def adding_two_values(numberA, numberB):
    print("Total is", numberA + numberB)

adding_two_values(2,5)