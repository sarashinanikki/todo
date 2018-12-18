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
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n')
    for i in jmap:
        print(jmap[i]['todo'], end='  ')
        print(jmap[i]['by'], end='  ')
        print(jmap[i]['on'], end='  ')
        print(jmap[i]['will'], end='  ')
        print(jmap[i]['unwill'], end='  ')
        print('\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

while True:
    command = input().split()
    if command[0] == "add":
        add(command)
        print('done!!')
    elif command[0] == "see":
        see(command)
    elif command[0] == "exit":
        print('Bye!!')
        sys.exit()
