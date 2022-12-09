# IMPORTS
import re
from collections import defaultdict


# GLOBALS
dir_info = defaultdict(lambda: {'files': [], 'dirs': []})
cwd = []
dirs_under_100000 = []

CD = re.compile(r'\$ cd (.+)')
FILE = re.compile(r'(\d+) (.+)')
DIR = re.compile(r'dir (\w+)')


# FUNCTIONS
def get_dir_size(curr_dir):
    dir_size = 0
    
    if dir_info[curr_dir]['files']:
        for file in dir_info[curr_dir]['files']:
            dir_size += int(file[0])
            
    if dir_info[curr_dir]['dirs']:
        for nested_dir in dir_info[curr_dir]['dirs']:
            dir_size += get_dir_size(nested_dir)
    
    if dir_size < 100000:
        dirs_under_100000.append(dir_size)
        
    return dir_size


# MAIN
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        cwd_str = '/'.join(cwd)
        
        if (match := CD.match(line)):
            dir = match[1]
            if dir == '..':
                cwd.pop()
            else:
                cwd.append(dir)
        elif (match := FILE.match(line)):
            file_size, file_name = match.group(1, 2)
            dir_info[cwd_str]['files'].append((file_size, file_name))
        elif (match := DIR.match(line)):
            nested_dir_path = '/'.join(cwd + [match[1]])
            dir_info[cwd_str]['dirs'].append(nested_dir_path)


get_dir_size('/')
print(sum(dirs_under_100000))