import sys
import json
from collections import OrderedDict
import pprint
import os

path = os.path.dirname(os.path.abspath(__file__))+'/todo.json'
archive_path = os.path.dirname(os.path.abspath(__file__))+'/todo_archive.json'

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

def add(args):
    if len(args) <= 1:
        alart = 'TODOの件名は必須となります'
        return alart
    todo_file = open(path, 'r')
    todo_map = json.load(todo_file, object_pairs_hook=OrderedDict)
    todo_file.close()
    index = len(todo_map)+1
    row = ['by', 'on', 'will', 'unwill']
    todo_map[index] = {}
    todo_map[index]['todo'] = args[1]
    for i in row:
        todo_map[index][i] = 'None'

    for i in range(2, len(args)):
        for j in row:            
            if args[i] == j:
                todo_map[index][j] = args[i+1]
                continue

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
    print('         ID', end=' : \t')
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
        alart = 'eraseする項目のIDを入力してください'
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
    see('')
    complete = 'complete!!'
    return complete

def edit(args):
    if len(args) <= 2:
        alart = 'editしたい項目のIDを入力してください'
        return alart
    todo_file = open(path, 'r')
    todo_map = json.load(todo_file, object_pairs_hook=OrderedDict)
    todo_file.close()

    row = ['todo', 'by', 'on', 'will', 'unwill']
    index = args[1]
    for i in range(2, len(args)):
        for j in row:
            if args[i] == j:
                todo_map[index][j] = args[i+1]
                break

    todo_out = open(path, 'w')
    json.dump(todo_map, todo_out, ensure_ascii=False)
    todo_out.close()
    complete = 'complete!!'
    return complete

def dicsort(args):
    if len(args) <= 1:
        see(args)
        alart = 'sortする項目を入力してください'
        return alart
    #TODOファイルを開く
    todo_file = open(path, 'r')
    todo_map = json.load(todo_file, object_pairs_hook=OrderedDict)
    todo_file.close()

    #keyが有効か確認
    row = ['todo', 'by', 'on', 'will', 'unwill']
    sure = False
    keys = args[1]
    for i in row:
        if i == keys:
            sure = True
    if not sure:
        alart = '有効なkeyを入力してください'
        return alart

    #sort
    swap_map = {}
    int_none = '100000000000010'
    str_none = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
    if keys == 'will' or keys == 'unwill':
        for i in todo_map:
            todo_value = todo_map[i][keys]
            if todo_value == 'None':
                todo_value = int_none
            swap_map[i] = int(todo_value)
    else:
        for i in todo_map:
            todo_value = todo_map[i][keys]
            if todo_value == 'None':
                todo_value = str_none
            swap_map[i] = (todo_value)

    sorted_swap = sorted(swap_map.items(), key=lambda x: x[1])
    new_todo_map = {}
    count = 1
    for i in sorted_swap:
        stringkey = str(i[0])
        new_todo_map[count] = todo_map[stringkey]
        count+=1

    #TODOファイルに書き込む
    todo_out = open(path, 'w')

    json.dump(new_todo_map, todo_out, ensure_ascii=False)
    todo_out.close()
    see('')
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
    elif command[0] == 'edit':
        message = edit(command)
        print('')
        print(message+'\n')
    elif command[0] == 'sort':
        message = dicsort(command)
        print('')
        print(message+'\n')
    elif command[0] == "exit":
        print('Bye!!')
        sys.exit()
    else:
        print('')
        print(' 使用できるコマンドは "add", "see", "erase", "exit" です.')
        print('\n')
