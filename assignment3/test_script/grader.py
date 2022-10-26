import os
import string
import random

# non-bash process 
for _ in range(5):
    os.system('man man &')
    os.system('pkill man')


# SYS folder
for _ in range(3):
    folder_base = '/tmp/' + ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=10)) 
    folder = folder_base + '/SYS'
    os.system(f'mkdir {folder_base}')
    os.system(f'mkdir {folder}')

# reading multiple files
os.system('./reader/read')

want = '''
exptected:

stats:
number of non-bash processes: 42
number of SYS folders: 3
number of opened p-files: 4
'''
print(want)
