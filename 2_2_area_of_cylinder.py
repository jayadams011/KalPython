""" (Compute the volume of a cylinder) Write a program that reads in the radius and length of a cylinder
and computes the area and volume using the following formulas:
area = radius * radius * π volume = area * length
Here is a sample run:
Enter the radius and length of a cylinder: 5.5, 12
The area is 95.0331 The volume is 1140.4 """

#user inputs radius and length of a cylinder
#create a var that requires input form the user
cylinderRadiusLength = eval(input("Enter the radius and length of your cylinder, ie 5.5,12 -->: "))
#calculate area
# constant to store PI value
#v pull first of two user input values
radius = cylinderRadiusLength[0]
PI = 3.1417
area = PI * (radius ** 2)
#calculate volume
#pull second of two user input values
volume = area * cylinderRadiusLength[1]
print("The area is ", area,". The volume is ", volume, ".")
      
                            
