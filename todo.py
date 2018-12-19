import sys
import json
from collections import OrderedDict
import pprint

path = '/home/sarashin/Documents/py/todo/todo.json'
try:
    with open(path, mode='x') as init:
        init.write('{}')
except FileExistsError:
    pass

def add(args):
    jfile = open(path, 'r')
    jmap = json.load(jfile, object_pairs_hook=OrderedDict)
    jfile.close()
    index = len(jmap)+1
    jmap[index] = {}
    jmap[index]['todo'] = args[1]
    jmap[index]['by'] = None
    jmap[index]['on'] = None
    jmap[index]['will'] = None
    jmap[index]['unwill'] = None

    for i in range(2, len(args)):
        if args[i] == 'by':
            jmap[index]['by'] = args[i+1]
        elif args[i] == 'on':
            jmap[index]['on'] = args[i+1]
        elif args[i] == 'will':
            jmap[index]['will'] = args[i+1]
        elif args[i] == 'unwill':
            jmap[index]['unwill'] = args[i+1]

    jout = open(path, 'w')
    json.dump(jmap, jout, ensure_ascii=False)
    jout.close()

def see(parameter_list):
    jfile = open(path, 'r')
    jmap = json.load(jfile)
    jfile.close()
    row = ['BY', 'ON', 'WILL', 'UNWILL']
    #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n')
    print('\n')
    print('num', end=' : \t')
    print('TODO'.ljust(40), end='\t')
    for r in row:
        print(r, end='      \t')
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('')
    for i in jmap:
        print('  ', end='')
        print(i, end=' : \t')
        print(jmap[i]['todo'].ljust(40), end='\t')
        print(jmap[i]['by'], end='      \t')
        print(jmap[i]['on'], end='      \t')
        print(jmap[i]['will'], end='        \t')
        print(jmap[i]['unwill'], end='      \t\n')
        print('\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n')

while True:
    command = input().split()
    if not command:
        continue
    if command[0] == "add":
        add(command)
        print('done!!')
    elif command[0] == "see":
        see(command)
    elif command[0] == 'erase':
        pass
    elif command[0] == "exit":
        print('Bye!!')
        sys.exit()
