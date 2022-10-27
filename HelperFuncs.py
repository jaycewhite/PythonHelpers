from operator import truediv
import re
#Takes multiline input and parses it to just the lines we need
def parseTableToLines():
    print("This is a very basic parser.\n" 
          "You must look through and validate the output is correct. This is a timesaver, not an all in one solution\n"
          "Please copy and paste the entire table definition\n"
          "To end input press enter, then Ctrl+d on Linux/Mac or Ctrl+z on Windows, then press enter again")
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    string = '\n'.join(lines)
    stack = 0
    startIndex = None
    results = []

    for i, c in enumerate(string):
        if c == '(':
            if stack == 0:
                startIndex = i + 1 # string to extract starts one index later

            # push to stack
            stack += 1
        elif c == ')':
            # pop stack
            stack -= 1

            if stack == 0:
                results.append(string[startIndex:i])
    noTab = results[0].replace('\t','')
    noTab = noTab.replace(' ','')
    lines = results[0].split("\n")
    for line in lines:
        line = line.replace('\t','')

    lines = [x for x in lines if 'constraint' not in x.lower()]
    lines = [x for x in lines if x]
    return lines


#Returns C# type from input line
def matchSqlTypeToCSharpType(line):
    split = line.split()
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
    return typeReal

#Returns lines from C# model only starting with public
def ParseCSharpModelInputOnlyPublic():
    print("This is a very basic parser.\n" 
          "You must look through and validate the output is correct. This is a timesaver, not an all in one solution\n"
          "Please copy and paste the properties you wish to convert\n"
          "To end input press enter, then Ctrl+d on Linux/Mac or Ctrl+z on Windows, then press enter again")
    lines = []
    while True:
        try:
            lines.append(input().strip())
        except EOFError:
            break
    lines = [x for x in lines if x.startswith('public')]
    return lines

#Returns typescript type from input line
def matchCSharpTypeToTypescriptType(line):
    
    if '?' in line:
        line = line.replace('?','')

    lineSplit = line.split()
    type = lineSplit[1]
    
    if '<' in type:
        templateSplit = type.split('<')
        type = templateSplit[0]
        match type.lower():
            case 'list' | 'icollection':
                type = 'Array'
            case _:
                type = type
        match = re.search('<.+?>', line)
        template = match.group(0)
        templateLower = template.lower()
        templateLower.replace('guid', 'string')
        templateLower.replace('datetime', 'Date')
        templateLower.replace('dateonly', 'Date')
        templateLower.replace('bool', 'boolean')
        templateLower.replace('int', 'number')
        templateLower.replace('long', 'number')
        templateLower.replace('decimal', 'number')

        if templateLower != template.lower():
            type = type + templateLower
        else:
            type = type + template
        return type

    typeReal = ''

    match type.lower():
        case 'guid':
            typeReal = 'string'
        case 'datetime' | 'dateonly':
            typeReal = 'Date'
        case 'bool':
            typeReal = 'boolean'
        case 'int' | 'long' | 'decimal':
            typeReal = 'number'
        case _:
            typeReal = type

    return typeReal

