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
    jmap = json.load(jfile)
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
    json.dump(jmap, jout)
    jout.close()

def see(parameter_list):
    pass

while True:
    command = input().split()
    if command[0] == "add":
        add(command)
    elif command[0] == "see":
        see(command)
    elif command[0] == "exit":
        sys.exit()
