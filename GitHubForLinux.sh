#!/usr/bin/env bash

cd /root/DjangoProject

git add -A .

git commit -m "$(date +%Y-%m-%d\ %H:%M:%S)"

git push DjangoApps master
