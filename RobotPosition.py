#!/usr/bin/python
##################################################
# Program that determines if a robot has moved in
# a complete circle
##################################################
# Author: Tanyaradzwa Matasva
# Course: CPSC-442-11
# Instructor: Dr Abdelshakour Abuzneid
# School: University of Bridgeport
##################################################

x = 0  # X position for circle starting point
y = 0  # Y position for circle starting point
sequence = input("Enter robot sequence : ")

for i in range(len(sequence)):
    if sequence[i] == 'U':
        y = y + 1
    elif sequence[i] == 'D':
        y = y - 1
    elif sequence[i] == 'L':
        x = x - 1
    elif sequence[i] == 'R':
        x = x + 1

if x == 0 and y == 0:
    print("True")
else:
    print("False")