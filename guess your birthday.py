day = 0
#Prompt the user with the first set
question1 = "Is your birthday in set?\n" + \
            " 1 3 5 7\n" + \
            "9 11 13 15\n" + \
            "17 19 21 23\n" + \
            "25 27 29 31" + \
            "\nEnter 0 for No and 1 for Yes: "

answer = eval(input(question1))

if answer == 1:
    day += 1
    
#Prompt the user with the second set
question2 = "Is your birthday in set?\n" + \
            " 2 3 6 7\n" + \
            "10 11 14 15\n" + \
            "18 19 22 23\n" + \
            "26 27 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "

answer = eval(input(question2))
if answer == 1:
    day +=2

#Prompt the user with the third set
question3 = "Is your birthday in set?\n" + \
            " 4 5 6 7\n" + \
            "112 13 14 15\n" + \
            "20 21 22 23\n" + \
            "28 29 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "

answer = eval(input(question3))
if answer == 1:
    day += 4


#Prompt the user with the fourth set
question4 = "Is your birthday in set?\n" + \
            " 8 9 10 11\n" + \
            "12 13 14 15\n" + \
            "24 25 26 27\n" + \
            "28 29 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "

answer = eval(input(question4))
if answer == 1:
    day +=8


#Prompt the user with the fifth set
question5 = "Is your birthday in set?\n" + \
            "16 17 18 19\n" + \
            "20 21 22 23\n" + \
            "24 25 26 27\n" + \
            "28 29 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "

answer = eval(input(question5))
if answer == 1:
    day +=16


print("\nYour Birthday is " + str(day) + "!")
