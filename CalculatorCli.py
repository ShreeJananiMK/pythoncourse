'''
Calculator App Operations:
    Add
    Sub
    multiplication
    Division (5 decimal points)
# for prompt use variable = input("message").<trimming_operaton>()
Prompt operation (enter Operation)
    add/+, sub/-, mul/*, div// # convert to upper or lower and compare and in or condition check for operators
    They case insensitive
    they have accept spaces ("add " = "add") # trimming the string in python Prompt number a and number b # a = input("1st number") output:
print(output as "a operation b") # Possible error scenarios

Assignment 2
Define amount number
do the operation on all numbers

'''
# Use camel case to denote function and variable
numList = list()
# strip to remove space
# 'Input' is used to get data from the user
operation = input('operation:').strip()

def multiply(numList):                  # camel case for function
    total = 1                           # camel case for variable. Set total=1 so that the multiplied value cannot be zero
    for x in numList:                   # Always give a single tab after colon
        total *= x                      # Equal symbol should always on right
    return total


def add(numList):                       # camel case for function
    total = 0                           # camel case for variable. Set total=0 to maintain addition between the items only
    for x in numList:                   # Always give a single tab after colon
        total += x                      # Equal symbol should always on right
    print (total)

def sub(numList):                       # camel case for function
    total = 0                           # camel case for variable. Set total=0 to maintain subtraction between the items only
    for x in numList:                   # Always give a single tab after colon
        total -= x                      # Equal symbol should always on right
    return total

def div(numList):                       # camel case for function
    total = 1                           # camel case for variable. Set total=1 to avoid getting infinity as result
    for x in numList:                   # Always give a single tab after colon
        total = x / total               # Equal symbol should always on right
    return total

try:                                    # Try except method is used to catch error
    n = int(input('Enter the number of elements'))
    for X in range(n):
        num = int(input('Enter number '))
        numList.append(num)             # Append is used to add items to an existing list
  
except:
  print("USE NUMBERS ONLY")
  exit()

print(numList)


operation = operation.upper()           # Upper is used to convert the lower case to upper case
if operation == 'ADD' or operation== '+':
    add(numList)

elif operation == 'SUB' or operation == '-':
    print(sub(numList))

elif operation == 'MUL' or operation == '*':
    print(multiply(numList)) 

elif operation == 'DIV' or operation == '/':
    print(div(numList))

else:
    print('ENTER SUITABLE OPERATION')

