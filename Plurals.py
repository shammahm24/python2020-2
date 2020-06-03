#!/usr/bin/python
##################################################
# Program that determines plural form of verbs
##################################################
# Author: Tanyaradzwa Matasva
# Course: CPSC-442-11
# Instructor: Dr Abdelshakour Abuzneid
# School: University of Bridgeport
##################################################

while True:
    number = int(input("Enter number : "))
    word = input("Enter word : ")

    if number == 1:
        print(word)
    else:
        if word[-3:] == "ife":
            print(word[:-3] + "ives")
        elif word[-2:] == "sh" or word[-2:] == "ch":
            print(word + "es")
        elif word[-2:] == "us":
            print(word[:-2] + "i")
        elif word[-2:] == "ay" or word[-2:] == "oy" or word[-2:] == "ey" or word[-2:] == "uy":
            print(word + "s")
        elif word[-1:] == "y":
            print(word[:-1] + "ies")
        else:
            print(word + "s")