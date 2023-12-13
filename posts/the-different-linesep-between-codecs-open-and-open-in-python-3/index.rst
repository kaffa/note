.. title: The different linesep between codecs open and open in python 3
.. slug: the-different-linesep-between-codecs-open-and-open-in-python-3
.. date: 2023-12-13 20:01:17 UTC+08:00
.. tags: python,linesep,newline
.. category: Tips
.. link: 
.. description: Python 中写文件 codecs open 和内置 open 函数之间的差异
.. type: text


文件分隔符之回车换行的故事
==================================================

最初的打字机上，将打字位置 Carriage 从行末移动到行首叫做 Carriage Return，既CR，既回车，将纸张上滚一行，叫做换行 Linefeed。

来到计算机时代，分别为这两种操作都定义了 ASCII 码

1. ASCII \\n: CR，Carriage Return，UNIX 上是行分隔符，newline，取第一个字；macOS 也采用了此换行符；

2. ASCII \\r: LF，Linefeed，Classic Mac OS 中，文件换行符是这个；

3. ASCII \\r\\n: CRLF，Carriage Return & Linefeed，Windows 最晚出现，为在 Windows 上能显示 Unix 和 Apple Mac OS 文件内容，弄出一个兼容的。


Python 世界的换行
==================================================

为兼容各平台差异，Python 的 os 模块中弄出多个属性来处理，比如

- linesep 行分隔符
- sep 文件路径名分割符
- pathsep 文件路径分隔符
- curdir 当前工作目录
- pardir 父目录

os 模块是处理好了这件事，但其它模块却不一定。


Python 2 的写文件
==================================================

1. open()，可能最早从 c 语言 fopen 学习的，未考虑编码参数
2. codecs.open()，支持编码参数
3. io.open()，支持编码参数的 open()，推荐使用


Python 3 的写文件
==================================================

1. open()，修正了 Python 2 时代的设计遗漏，支持 encoding 和 newline 参数
2. codecs.open()，在读写文件时不推荐使用了，且此模块方法在 Windows 下有坑，文件换行符会弄成 LF
   

不同平台的差异随处可见
==================================================

一定程度上反映了，人各有各的思想，分久必合，当人们无法忍受差异时，就会发展为统一。
