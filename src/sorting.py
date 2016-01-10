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
import re
string=raw_input()
print sorted(string,reverse=True)
numeric=re.findall("[-+]?\d+[\.]?\d*", string) 
small=re.findall("[a-z]+",string)
large=re.findall("[A-Z]+",string)
msg=small+large+numeric
print sorted(msg,reverse=True)
