#!/bin/bash

# 使用 nohup 启动 WeChat，并将输出重定向到 /dev/null
nohup /Applications/WeChat.app/Contents/MacOS/WeChat > /dev/null 2>&1 &
