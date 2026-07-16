#!/usr/bin/env bash

###### pipes, '|' #######
# redirects stout to the next command's stdin
# ex. ls -l | grep "secret"

ls *.txt | grep e

## command composition
# use of && and || operators
# they are the AND and OR operators respectively, but for 
# chaining commands
#   command1 && command2, command2 will be executed if command1
#   exit'ed with a success status
#   example:  mkdir projects && cd projects
# command1 || command2, command2 will only execute if command1 exit'ed
#   with a failure status (non-zero)
#   example: ping -c google.com || echo "Internet is down"

mkdir projects && cd projects
pwd
echo "Going 1 directory up"
cd ..
pwd

ls glennj.txt 2>/dev/null || echo "glenn.txt does not exist"



##Operator,Name,What it does
# |,Pipe,Feeds stdout of Left into stdin of Right.
# |&,Pipe Both,Feeds both stdout and stderr of Left into stdin of Right.
# &&,Logical AND,Runs Right only if Left succeeded (Exit Code 0).
# ||,Logical OR,Runs Right only if Left failed (Exit Code = 0).
# ;,Semicolon,"Runs Left, then runs Right (ignores success/failure)."
# <(),Process Sub,Makes a command's output behave like a readable file.
#      -ex: diff <(ls engineering-reboot) <(ls development-workspace)


