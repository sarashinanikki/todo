import sys
import json
from collections import OrderedDict
import pprint

path = '/home/sarashin/Documents/py/todo/todo.json'
archive_path = '/home/sarashin/Documents/py/todo/todo_archive.json'
try:
    with open(path, mode='x') as init:
        init.write('{}')
except FileExistsError:
    pass

try:
    with open(archive_path, mode='x') as archive_init:
        archive_init.write('{}')
except FileExistsError:
    pass

error_messages = ['']

def add(args):
    if len(args) <= 1:
        alart = 'TODOの件名は必須となります'
        return alart
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
    complete = 'done!!'
    return complete

def see(args):
    jfile = open(path, 'r')
    jmap = json.load(jfile)
    jfile.close()
    row = ['BY', 'ON', 'WILL', 'UNWILL']
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
    print('\n')


def erase(args):
    if len(args) <= 1:
        alart = 'eraseするリストの番号を入力してください'
        return alart
    jfile = open(path, 'r')
    jmap = json.load(jfile, object_pairs_hook=OrderedDict)
    jfile.close()
    index = str(args[1])
    archive = jmap.pop(index)


while True:
    print(' -> ', end=' ')
    command = input().split()
    if not command:
        continue
    if command[0] == "add":
        message = add(command)
        print('')
        print(message+'\n')
    elif command[0] == "see":
        see(command)
    elif command[0] == 'erase':
        erase(command)
    elif command[0] == "exit":
        print('Bye!!')
        sys.exit()
    else:
        print('')
        print(' 使用できるコマンドは "add", "see", "erase", "help" です. 詳細は"help"を叩いてください')
        print('\n')
