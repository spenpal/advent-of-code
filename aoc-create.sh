#!/bin/bash

# First create a directory at the current location, named with the current year
mkdir $(date +%Y)

# Then inside the year directory, create 25 directories from day01 to day25. 
# Inside each of these directories, create 4 files named input.txt, part1.py, part2.py, and README.md
for i in {01..25}; do
    mkdir $(date +%Y)/day$i;
    touch $(date +%Y)/day$i/input.txt;
    touch $(date +%Y)/day$i/part1.py;
    touch $(date +%Y)/day$i/part2.py;
    touch $(date +%Y)/day$i/README.md;
done