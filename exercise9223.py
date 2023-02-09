'''Write a program to prompt the user for hours and rate per hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75 

Pay: 96.25'''

enterHours = float(input("Enter the hour value: "))
enterRate = float(input("Enter the rate value: "))
pay = enterHours * enterRate
print('Pay: ' + str(pay) )
