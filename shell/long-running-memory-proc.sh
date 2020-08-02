#!/bin/bash

# Filename: long-running-memory-proc.sh
# Revision: 1.0
# Auther: chenshiyang
# Date: 2020-08-02
# Description: 检查高内存消耗进程在 Linux 上运行了多长时间

ps -eo pid,user,ppid,%mem,%cpu,cmd --sort=-%mem | head | tail -n +2 | awk '{print $1}' > /tmp/long-running-processes-1.txt
echo "--------------------------------------------------"
echo "UName     PID  CMD          Process_Running_Time"
echo "--------------------------------------------------"
for userid in `cat /tmp/long-running-processes-1.txt`
do
username=$(ps -u -p $userid | tail -1 | awk '{print $1}')
pruntime=$(ps -p $userid -o etime | tail -1)
ocmd=$(ps -p $userid | tail -1 | awk '{print $4}')
echo "$username $userid $ocmd $pruntime"
done | column -t
echo "--------------------------------------------------"