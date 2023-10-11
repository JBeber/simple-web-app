import time
import os

FILEPATH = 'files/todos.txt'
if not os.path.exists(FILEPATH): 
    with open(FILEPATH, 'w'):
        pass

# read todo items from text file to a list
def read_list():
    with open(FILEPATH, 'a+') as todo_file:
        # Since append filemode sets the file handle to EOF, we must reset to the beginning to read in the currently stored list
        todo_file.seek(0)
        item_lst = todo_file.readlines()

    mod_time = '' 
    # pop off the first line read in which contains the last modification time stamp
    if len(item_lst) != 0: 
        mod_time = item_lst.pop(0).strip('\n')    

    # strip off trailing newline chars
    item_lst = [item.strip('\n') for item in item_lst]

    return mod_time, item_lst
##########################################################################################

# Utility function used to visually separate CLI outputs 
def wait():
    print('Press any key to continue...')
    input()
##########################################################################################

def print_list(item_lst):
    if len(item_lst) == 0:
        print('\nItem list is empty!')
    else:
        print('CURRENT LIST')   
        for index,item in enumerate(item_lst):
            print(f'{index+1}: {item}')
    wait()

def add_item(item_lst, item):
    item_lst.append(item)
    return time.strftime('%b %d, %Y %H:%M:%S')

def edit_item(item_lst, item_num, item):
    item_lst[item_num] = item
    return time.strftime('%b %d, %Y %H:%M:%S')

def remove_item(item_lst, item_num):
    item_lst.pop(item_num)
    return time.strftime('%b %d, %Y %H:%M:%S')

def write_list(mod_time, item_lst):
     with open(FILEPATH, 'w') as todo_file:
        # Write timestamp
        todo_file.write(f'{mod_time}\n')
        # Write list
        for item in item_lst:
            todo_file.write(f'{item}\n')