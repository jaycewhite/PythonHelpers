from distutils.command.config import config
import re
from HelperFuncs import *
lines = ParseCSharpModelInputOnlyPublic()
hasClassName = False
for line in lines:
    split = line.split()
    if split[1] == 'class':
        print('export class {} {{'.format(split[2]))
        hasClassName = True
        continue
    if '()' in split[1]:
        continue
    typeReal = matchCSharpTypeToTypescriptType(line)
    name = split[2]
    name = name[0].lower() + name[1:]

    print('{}: {};'.format(name,typeReal))

if hasClassName:
    print('}')
input("Enter to close")

