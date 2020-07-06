#!/bin/bash

path=/home/rd/brush
logpath=/result

for i in $(seq 1 6)
do   
echo $path$i$logpath
ls -ld $path$i$logpath |awk '{print $9}'|xargs -n 10 sudo rm -rf
done  

