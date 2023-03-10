'''Write a program to prompt the user for hours and rate per hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75 

Pay: 96.25'''
# Enter the input value
enterHours = float(input("Enter the hour value: "))  # Use camel case for variable
enterRate = float(input("Enter the rate value: "))   # Use camel case for variable
pay = enterHours * enterRate                         # '*' is used to multiply numbers
print('pay: ' + str(pay) )                           # '+' is used to concatenate two strings
