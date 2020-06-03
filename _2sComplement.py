#!/usr/bin/python
##################################################
# Program that prints the 2's complement of a given
# number
##################################################
# Author: Tanyaradzwa Matasva
# Course: CPSC-442-11
# Instructor: Dr Abdelshakour Abuzneid
# School: University of Bridgeport
##################################################


def findComplement(num):
    numWord = bin(num)  # converts decimal number to binary representation
    numWord = numWord[2:]  # trims initial 2 chars from the string
    length = len(numWord)  # calculates the length of the string
    i = 0
    res = ''  # Following loop would iterate for every char to convert it.
    while i < length:
        if numWord[i] == '1':
            res += '0'
        else:
            res += '1'
        i += 1
    return res


def find2sComplement(num):
    complement = findComplement(num)
    temp = ''
    carry = 0
    for i in range(len(complement)):
        j = (len(complement)-1-i)
        if i == 0:  # add 1 to the first bit in the binary complement
            if complement[j] == '1':
                temp = temp+'0'
                carry = 1
            else:
                temp = temp+'1'
                carry=0
        else:  # continue addition on the remaining bits
            if complement[j] == '1':
                if carry == 1:
                    temp = temp + '1'
                    carry = 1
                else:
                    temp = temp + '1'
                    carry = 0
            else:
                if carry == 1:
                    temp = temp + '1'
                    carry = 0
                else:
                    temp = temp + '0'
                    carry = 0
    result = ''
    for i in range(len(temp)): # reverse the order of bits to form the correct binary number
        result = result + temp[(len(temp)-1)-i]

    decimal = 0  # the decimal number represented by the 2's complement
    num = int(result)
    for i in range(len(result)):

        dec = num % 10
        decimal = decimal + dec * pow(2, i)
        num = num // 10

    return decimal


def main():
    num = int(input("Enter number : "))
    result = find2sComplement(num)
    intValue=int(result)
    print(str(intValue))


main()
