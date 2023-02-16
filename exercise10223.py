'''Rewrite your pay computation to give the employee 
1.5 times the hourly rate 
for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

'''
pay = 0
try:
    enterHours = float(input("Enter the hour value: "))
    enterRate = float(input("Enter the rate value: "))
except:
    print("USE NUMBERS ONLY")
    exit()

if enterHours > 40 :
    extraHours = enterHours - 40
    pay = ((extraHours * 1.5 * enterRate) + (40 * enterRate))
else :
    pay = enterHours * enterRate 
print('Pay: ' + str(pay) )

