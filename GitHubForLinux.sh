#!/usr/bin/env bash

if [ ! -d .git -a ! -f manage.py ];then
    echo 'Warning:The Work Directory Is Wrong. Please Check It and Retry!'
else
    git add -A .
    git commit -m "$(date +%Y-%m-%d\ %H:%M:%S)"
    git push DjangoApps master
fi
