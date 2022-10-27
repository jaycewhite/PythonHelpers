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
    typeReal = ''
    match typeStr:
        case 'uniqueidentifier':
            typeReal = 'Guid'
        case 'datetime':
            typeReal = 'DateTime'
        case 'date':
            typeReal = 'DateTime'
        case 'bit':
            typeReal = 'bool'
        case 'bigint':
            typeReal = 'long'
        case _:
            typeReal = typeStr

    if re.match('decimal.*',typeStr):
        typeReal = 'decimal'
    if re.match('varchar.*',typeStr):
        typeReal = 'string'
    if 'null' in split[2].lower():
        typeReal += '?'

    print('{} = x.Field<{}>("{}"),'.format(name,typeReal,name))

input("Enter to close")

