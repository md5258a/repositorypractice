# Mary-Almah Davis
# CSC-148-002
# Programming Assignment 3
# February 9, 2022
#
# additionquiz.py: prompts the user three different levels of addition ranging from easy to hard.
# The user will get five addition problems based on the level of difficulty they choose.
#
#
import random

# global constants
MIN_ANSWER = 0
MAX_ANSWER = 999999

#global variables
num_problems = 0
num_correct = 0

# This function provides the minimum and maximum of allowable answers.
def get_int_input(prompt,min1,max1):
    response = input(prompt)
    if not response.isdigit():
        print("Invalid input!")
        return get_int_input(prompt,min1,max1)
    else: # value is numeric but is it in range?
        value = int(response)
        if value < min1 or value > max1:
            print("Value out of range!")
            return get_int_input(prompt,min1,max1)
        return value

# This Function calls the program to start
def main():
    print("Welcome to addition quiz!")
    play_game()

# This Function asks the user for a level of difficulty
def get_level():
    return get_int_input("Which level? (enter 1, 2, or 3): ", 1,3)

# This function asks the user if they want to continue playing and tells the user their score
def play_game():
    level = get_level()
    show_problems(level)
    repeat = get_int_input("Would you like to try some more problems? Enter 0 for no, 1 for yes: ",0,1)
    if repeat == 1:
        play_game()
    else:
        print("Your score is",num_correct,"correct out of",str(num_problems),".")
        print("Thank you for playing!\n")

# This function gives the user each addition problem
def show_problems(level):
    addition_problem(level)
    addition_problem(level)
    addition_problem(level)
    addition_problem(level)
    addition_problem(level)

# This function sets up the addition problems
def addition_problem(level):
    global num_problems,num_correct
    op1 = random.randint(10**(level-1),10**level)
    op2 = random.randint(10**(level-1),10**level)
    prompt = str(op1)+" + "+str(op2)+" = "
    answer = get_int_input(prompt,MIN_ANSWER,MAX_ANSWER)
    correct_answer = op1 + op2
    if answer == correct_answer:
        print("Correct!")
        num_correct = num_correct + 1
    else: 
        print("Sorry, wrong answer! Correct answer is",correct_answer)
    num_problems = num_problems + 1
main()