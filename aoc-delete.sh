#!/bin/bash

echo "Enter a number from 1 to 25:"
read num

for (( i=$num; i<=25; i++ ))
do
    dir="2022/day$(printf "%02d" $i)"
    rm -r $dir
done
