#!/usr/bin/python
##################################################
# 3 Python functions for
# i) detect prime numbers
# ii) change camel case to snake case
# iii) takes prompt as input
##################################################
# Author: Tanyaradzwa Matasva
# Course: CPSC-442-11
# Instructor: Dr Abdelshakour Abuzneid
# School: University of Bridgeport
##################################################

# function to check for prime numbers


def is_prime(num):  # Function to check is a number is prime
    if num == 1:  # 1 is not a prime number
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:  # check if any of the numbers from 2 to itself can divide it completely
                return False

        return True


def snake_case(string):  # Function to convert camel case to snake case
    result = ""  # stores the final result
    previous_index = 0  # keeps track of the position of the last upper case character
    for i in range(len(string)):
        if string[i].isupper():
            if len(result) == 0:  # the first word to be added on to the result string
                result = string[:i]
                if i < len(string):  # add _ to separate words unless it is the last word
                    result = result + "_"
            else:
                result = result + string[previous_index:i].lower()
                if i < len(string):
                    result = result + "_"  # add _ to separate words unless it is the last word

            previous_index = i
    result = result + string[previous_index:].lower()  # add the remaining word to the result string
    return result


def get_number_input(prompt):
    global result
    result = 0
    try:
        num = int(input(prompt))
        result = num
    except:
        get_number_input(prompt)
    return result


print("Check for prime numbers : ")
print("7 : "+str(is_prime(7)))
print("9 : "+str(is_prime(9)))
print("\nSnake Case:")
print("listOfInts : "+snake_case("listOfInts"))
print("\nFunction with prompt")
print(str(get_number_input("Enter an int : ")))
