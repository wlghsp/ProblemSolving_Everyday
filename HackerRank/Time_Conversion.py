#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    #
    # Write your code here.
    #
    convertedTime = ''
    if s[8] == 'A' and s[0:2] != '12':
        convertedTime = s[0:8]
    elif s[8] == 'A' and s[0:2] == '12':
        convertedTime = '00' + s[2:8]
    elif s[8] == 'P' and s[0:2] != '12':
        hour = int(s[0])*10 + int(s[1]) + 12
        convertedTime = str(hour) + s[2:8]
    elif s[8] == 'P' and s[0:2] == '12':
        convertedTime = s[0:8]
    return convertedTime


# 07:05:45PM
# 12:40:22AM
s = input()

result = timeConversion(s)

print(result)
