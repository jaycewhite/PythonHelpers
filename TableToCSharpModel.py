import re
from HelperFuncs import *
lines = parseTableToLines()

for line in lines:
    result = re.search('\\[(.*)\\]',line)
    split = line.split()
    if result:
        name = result.group(1)
    else:
        name = split[0]
    
    typeStr = split[1].lower()
    typeReal = matchSqlTypeToCSharpType(line)

    print('public {} {} {{ get; set; }}'.format(typeReal,name,name))

input("Enter to close")

