"""
(Financial application: calculate tips) Write a program that reads the subtotal and the gratuity rate
and computes the gratuity and total. For example, if the user enters 10 for the subtotal and 15% for
the gratuity rate, the program displays 1.5 as the gratuity and 11.5 as the total. Here is a sample run:
Enter the subtotal and a gratuity rate: 15.69, 15
The gratuity is 2.35 and the total is 18.04
"""

# user inputs subtotal and gratutiy rate
# create input var that requires user input

subtotAndTip = eval(input(" Please enter the bill subtotal and the tip percentage\(ie..15.69,15\). -->"))
#seperate out subtotal
subtotal = subtotAndTip[0]
#seperate out tip percentage and convert to decimal
tip = subtotAndTip[1] / 100
#multiply tip by subtotal to get tip amount
tip = tip * subtotal
#add tip to subtot for tot
total = subtotal + tip
print("The gratuity is ","{:.2f}".format(tip), "and the total is ","{:.2f}".format(total),".")
