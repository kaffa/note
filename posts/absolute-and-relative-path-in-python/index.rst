.. title: Absolute and Relative Path in Python
.. slug: absolute-and-relative-path-in-python
.. date: 2023-12-07 08:12:45 UTC+08:00
.. tags: python,path
.. category: Tips
.. link: 
.. description: 本文说明 python 中获取绝对路径和相对路径时需要注意的点。
.. type: text



1. os.path.isabs()
==================================================
   
os.path.isabs() 的行为是：如果路径以 / 开头，或者在非类 Unix 平台上，以盘符跟一个 os.sep 开头，就返回 True；否则，就返回 False

这里要注意的是在 Windows 上，是支持两种斜线符号的，一种是Windows的斜线，但需要双写以转义 '\\'，另一种是类似 Unix 反写 '/'。

看如下代码，在 Windows 下的返回结果

.. code-block :: python

    Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import os
    >>> os.path.isabs('c:/abc')
    True
    >>> os.path.isabs('/abc')
    True
    >>> os.path.isabs('c:\abc') # 未转义，错误
    False
    >>> os.path.isabs('c:/abc')
    True
    >>> os.path.isabs('c:\\abc')
    True
    >>> os.path.isabs('\\abc')
    True
    >>> os.path.isabs('abc')                                                                                                                                                                                                                                 
    False
    

所以说，实际上这个方法在 Windows 并不好用，试着查看源代码，但实现并不是 Python 的，似乎有 macpath,posixpath,ntpath，但 ntpath 在 Windows 上返回就是上述值。



2. pathlib.Path().is_absolute() 在 Windows 上更好用
====================================================================================================

实际上判断是否绝对路径时，应该使用以下代码

.. code-block :: python

    import pathlib
    pathlib.Path('/abc').is_absolute()


    
