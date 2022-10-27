import re
from HelperFuncs import *
lines = parseTableToLines()

for line in lines:
    outputStr = '   @'
    result = re.search('\\[(.*)\\]',line)
    split = line.split()
    if result:
        name = result.group(1)
    else:
        name = split[0]
    outputStr += name + ' '
    typeStr = split[1].upper()
    
    if '(' in typeStr:
        resultType = re.search('\([^\)]+\)', line)
        if resultType:
            typeSplit = typeStr.split('(')
            typeStr = typeSplit[0] + resultType.group(0)
    outputStr += typeStr

    if 'null' in split[2].lower():
        outputStr += ' = NULL'

    outputStr += ','

    print(outputStr)

input("Enter to for assignments")

for line in lines:
    outputStr = '   '
    result = re.search('\\[(.*)\\]',line)
    split = line.split()
    if result:
        name = result.group(1)
    else:
        name = split[0]
    outputStr += name + ' = @' + name + ','
    print(outputStr)

input("Enter for value pairs")

print('(')
for line in lines:
    outputStr = '   ['
    result = re.search('\\[(.*)\\]',line)
    split = line.split()
    if result:
        name = result.group(1)
    else:
        name = split[0]
    outputStr += name + '],'
    print(outputStr)
print(')')

print('VALUES')
print('(')

for line in lines:
    outputStr = '   @'
    result = re.search('\\[(.*)\\]',line)
    split = line.split()
    if result:
        name = result.group(1)
    else:
        name = split[0]
    outputStr += name + ','
    print(outputStr)
print(')')
input("Enter to close")
