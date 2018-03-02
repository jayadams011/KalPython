"""
(Convert pounds into kilograms) Write a program that converts pounds into kilograms. The program
prompts the user to enter a value in pounds, converts it to kilograms, and displays the result. One
pound is 0.454 kilograms. Here is a sample run:
Enter a value in pounds: 55.5
55.5 pounds is 25.197 kilograms
"""
#user inputs number of pounds to convert to Kgs
#create a var that requires input from the user

pounds = eval(input( "Enter the number of pounds you would like to convert to kilograms. -->"))
# convert pounds to kilograms
kilograms = pounds * 0.454

#print output
print( pounds, " is ",kilograms, " kilograms.")
