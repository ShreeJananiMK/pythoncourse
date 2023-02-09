Operation = input('Operation:').strip()
#Operation = ('ADD','SUB','MUL','DIV','+','-','*','/')
try:
    A= list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
except:
  print("USE NUMBERS ONLY")
  exit()
Operation = Operation.upper()
if Operation == 'ADD' or Operation== '+':
    print(A+B)
elif Operation == 'SUB' or Operation == '-':
    print(A-B)
elif Operation == 'MUL' or Operation == '*':
    print(A*B)
elif Operation == 'DIV' or Operation == '/':
    print(A/B)
else:
    print('Enter suitable operation')