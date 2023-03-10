'''Rewrite your pay computation to give the employee 
1.5 times the hourly rate 
for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''


# define the function as compute pay
def computePay(enterHours, enterRate):
    # Use camel case for variable and function
    pay = 0
    
    # Try except method is used to catch the expected error
    if enterHours > 40 :                                     # Always give a single tab after colon
        extraHours = enterHours - 40
        pay = ((extraHours * 1.5 * enterRate) + (40 * enterRate))
    else :                                                   # Give a single tab after colon
        pay = enterHours * enterRate 

    return pay


if __name__ == "__main__":
    try:
        enterHours = float(input("Enter the hour value: "))  # Camel case, float is used to convert an int to decimel
        enterRate = float(input("Enter the rate value: "))   # Input is used to get value from the user
        pay = computePay(enterHours, enterRate)
        print(pay)
    except:
        print("USE NUMBERS ONLY")
        exit()
