"""
(Convert feet into meters) Write a program that reads a number in feet, converts it to meters, and
displays the result. One foot is 0.305 meters. Here is a sample run:
Enter a value for feet: 16.5
16.5 feet is 5.0325 meters

"""

#user inputs feet as an integer
#create a var that requires input form the user
numOfFeet = eval(input(" Enter the number of feet you would like to convert to meters. --> "))
meters = numOfFeet * 0.305
print( numOfFeet, "feet is ",meters, " meters.")
