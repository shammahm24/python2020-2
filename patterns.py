#!/usr/bin/python
##################################################
## Program that iteratively prints out patterns
##################################################
## Author: Tanyaradzwa Matasva
## Course: CPSC-442-11
## Instructor: Dr Abdelshakour Abuzneid
## School: University of Bridgeport
##################################################

print("a)")
for i in range(6):
    print("*"*i)

print("b)")
for i in range(6):
    print(" "*(6-i)+"*"*i)

print("c)")
for i in range(6):
    print(" "*(6-i)+"*"*i+"*"*i)