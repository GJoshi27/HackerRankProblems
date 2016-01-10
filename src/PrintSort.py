'''
Problem Statement

You are given a string S.
S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

Input Format

A single line of input contains the string S.

Constraints

0<len(S)<1000

Output Format

Output the sorted string S.

Sample Input

Sorting1234

Sample Output

ginortS1324

Note:
a) Using join, for or while anywhere in your code, even as substrings, will result in a score of 0.
b) You can only use one sorted function in your code. A 0 score will be awarded for using sorted more than once. 
'''
from __future__ import print_function
upper = []
lower = []
even = []
odd = []

def separator(a):
    if a.isalpha():
        if a.isupper():
            upper.append(a)
        else:
            lower.append(a)
    else:
        if int(a)%2 == 0:
            even.append(a)
        else:
            odd.append(a)
    return 

map(separator,raw_input())  

upper.sort()
lower.sort()
even.sort()
odd.sort()

t = lower+upper+odd+even
map(lambda x: print(x,end=''),t)
