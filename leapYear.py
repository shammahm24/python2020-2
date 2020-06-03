#!/usr/bin/python
##################################################
## Program that checks if an entered year is a leap
## year
##################################################
## Author: Tanyaradzwa Matasva
## Course: CPSC-442-11
## Instructor: Dr Abdelshakour Abuzneid
## School: University of Bridgeport
##################################################

year = int(input("Enter year: "))

if year % 4 ==0 :
    if year % 100 ==0:
        if year % 400 ==0:
            print("True")
        else:
            print("False")
    else:
        print("True")
else:
    print("False")