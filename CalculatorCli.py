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
NumList = list()
Operation = input('Operation:').strip()

def multiply(NumList):
    total = 1
    for x in NumList:
        total *= x
    return total


def add(NumList):
    total = 0
    for x in NumList:
        total += x
    print (total)

def sub(NumList):
    total = 0
    for x in NumList:
        total -= x
    return total

def div(NumList):
    total = 1
    for x in NumList:
        total = x / total
    return total

try:
    N = int(input('Enter the number of elements'))
    for X in range(N):
        Num = int(input('Enter number '))
        NumList.append(Num)  
  
except:
  print("USE NUMBERS ONLY")
  exit()

print(NumList)


Operation = Operation.upper()
if Operation == 'ADD' or Operation== '+':
    add(NumList)

elif Operation == 'SUB' or Operation == '-':
    print(sub(NumList))

elif Operation == 'MUL' or Operation == '*':
    print(multiply(NumList)) 

elif Operation == 'DIV' or Operation == '/':
    print(div(NumList))

else:
    print('Enter suitable operation')

