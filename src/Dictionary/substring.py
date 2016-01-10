import re
a = raw_input()
b = raw_input()
match = re.findall('(?='+b+')',a)
print len(match)
