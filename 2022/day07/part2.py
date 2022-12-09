# IMPORTS
import re
from collections import defaultdict


# GLOBALS
dir_info = defaultdict(lambda: {'files': [], 'dirs': []})
dir_sizes = []

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
            
    dir_sizes.append(dir_size)
    return dir_size


# MAIN
with open("input.txt") as f:
    cwd = []
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

total_space = 70_000_000
used_space = get_dir_size('/')
unused_space = total_space - used_space
needed_space = 30_000_000 - unused_space

for dir_size in sorted(dir_sizes):
    if needed_space <= dir_size:
        print(dir_size)
        break