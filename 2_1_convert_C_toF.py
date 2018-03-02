"""(Convert Celsius to Fahrenheit) Write a program that reads a Celsius degree from the console and
converts it to Fahrenheit and displays the result. The formula for the conversion is as follows:
fahrenheit = (9 / 5) * celsius + 32
Here is a sample run of the program:
Enter a degree in Celsius: 43
43 Celsius is 109.4 Fahrenheit """

# User inputs temp in Celsius

#create a var that requries input from the user.  Call that input degreeC
degreeC = eval(input("Enter a temp in Celsius degrees. --> "))
#create a var that converts degreeC into degreeF
degreeF = (9/5) * degreeC + 32
# print the results of degreeC and degreeF in a sentence. 
print(degreeC, "Celcius is ", degreeF, " Fahrenheit.")
