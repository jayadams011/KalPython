"""
(Sum the digits in an integer) Write a program that reads an integer between 0 and 1000 and adds
all the digits in the integer. For example, if an integer is 932, the sum of all its digits is 14. (Hint: Use
the % operator to extract digits, and use the // operator to remove the extracted digit. For instance,
932 % 10 = 2 and 932 // 10 = 93.) Here is a sample run:
Enter a number between 0 and 1000: 999
The sum of the digits is 27
"""
#user inputs an integer between 0 and 1000
#create a var that requires user input - it is an eval of an integer
userInt = eval(input("Enter a number between 0 and 1000: "))
def sum_digits(userInt):
    results = 0
    while userInt > 0:
        remainder =  userInt % 10
        results += remainder
        userInt = (userInt-remainder)/10
    return results
sum_digits(userInt)
print("The sum of the digits is ",, ".")



