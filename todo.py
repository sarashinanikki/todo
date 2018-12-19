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
    todo_file = open(path, 'r')
    todo_map = json.load(todo_file, object_pairs_hook=OrderedDict)
    todo_file.close()
    index = len(todo_map)+1
    todo_map[index] = {}
    todo_map[index]['todo'] = args[1]
    todo_map[index]['by'] = 'None'
    todo_map[index]['on'] = 'None'
    todo_map[index]['will'] = 'None'
    todo_map[index]['unwill'] = 'None'

    for i in range(2, len(args)):
        if args[i] == 'by':
            todo_map[index]['by'] = args[i+1]
        elif args[i] == 'on':
            todo_map[index]['on'] = args[i+1]
        elif args[i] == 'will':
            todo_map[index]['will'] = args[i+1]
        elif args[i] == 'unwill':
            todo_map[index]['unwill'] = args[i+1]

    todo_out = open(path, 'w')
    json.dump(todo_map, todo_out, ensure_ascii=False)
    todo_out.close()
    complete = 'complete!!'
    return complete

def see(args):
    todo_file = open(path, 'r')
    todo_map = json.load(todo_file)
    todo_file.close()
    row = ['BY', 'ON', 'WILL', 'UNWILL']
    print('\n')
    print('\n')
    print('        num', end=' : \t')
    print('TODO'.ljust(30), end='\t')
    for r in row:
        print(r.ljust(18), end='\t')
    print('')
    print('        ', end='')
    for i in range(120):
        print('~', end='')
    print('\n')
    for i in todo_map:
        print('          ', end='')
        print(i, end=' : \t')
        print(todo_map[i]['todo'].ljust(30), end='\t')
        print(todo_map[i]['by'].ljust(18), end='\t')
        print(todo_map[i]['on'].ljust(18), end='\t')
        print(todo_map[i]['will'].ljust(18), end='\t')
        print(todo_map[i]['unwill'].ljust(18), end='\t\n')
        print('\n')
    print('        ', end='')
    for i in range(120):
        print('~', end='')
    print('')
    print('\n')
    print('\n')


def erase(args):
    if len(args) <= 1:
        alart = 'eraseするリストの番号を入力してください'
        return alart
    #TODOファイルを開く
    todo_file = open(path, 'r')
    todo_map = json.load(todo_file, object_pairs_hook=OrderedDict)
    todo_file.close()

    #Archiveファイルを開く
    archive_file = open(archive_path, 'r')
    archive_map = json.load(archive_file, object_pairs_hook=OrderedDict)
    archive_file.close()
    
    #TODOファイルからキーで削除
    archive = todo_map.pop(args[1])
    
    #archive_mapに削除した値を貼り付ける
    index = len(archive_map)+1
    archive_map[index] = archive
    
    #Archiveファイルに完成した辞書を出力する
    archive_out = open(archive_path, 'w')
    json.dump(archive_map, archive_out, ensure_ascii=False)
    archive_out.close()
    
    #TODO_mapの添字を整理する
    new_todo_map = {}
    count = 1
    for v in todo_map.values():
        new_todo_map[count] = v
        count += 1
    
    #TODOファイルに書き込む
    todo_out = open(path, 'w')
    json.dump(new_todo_map, todo_out, ensure_ascii=False)
    todo_out.close()
    complete = 'complete!!'
    return complete

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
        message = erase(command)
        print('')
        print(message+'\n')
    elif command[0] == "exit":
        print('Bye!!')
        sys.exit()
    else:
        print('')
        print(' 使用できるコマンドは "add", "see", "erase", "exit" です.')
        print('\n')
