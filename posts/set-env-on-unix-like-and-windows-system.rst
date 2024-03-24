.. title: Set Env on Unix-like and Windows System
.. slug: set-env-on-unix-like-and-windows-system
.. date: 2024-03-24 11:21:08 UTC+08:00
.. tags: env 
.. category: tip 
.. link: 
.. description: 本篇描述增加环境变量的通用方法。
.. type: text


## 在类Unix系统上

类Unix：指 Linux macOS FreeBSD 等

环境配置文件：用来放置命令行的文件

比如在 bash，可以放在 ~/.profile，在 zsh，则是 .zshrc。

例如，以下命令用来添加GO环境变量

::bash

    export GOPATH=$HOME/go
    export PATH=$PATH:$GOPATH/bin


如果需要立刻生效，还需要执行 source 命令。

## 在 Windows 系统

可以在命令行运行::cmd

    setx GOPATH $USERPROFILE%\go
    setx path "%path%;%USERPROFILE%\bin"

运行上述命令，然后关闭当前命令提示符窗口，重新打开一个新的，更改才会生效。
