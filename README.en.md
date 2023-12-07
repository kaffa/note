这个目录包含琅環笔记的网站源码。

Nikola GitHub Deploy 推荐做法是分为 main 分支和 src 分支，src 分支是「马戏团后台」，src 分支的 output 目录作为 main 分支。

GitHub Pages 每次发布 main 分支，关于这种做法的评价，我放在：

https://note.tt4e.com/posts/nikola-tips/#nikola-github


This folder contains the source used to generate a static site using Nikola.

Installation and documentation at https://getnikola.com/

Configuration file for the site is ``conf.py``.

To build the site::

    nikola build

To see it::

    nikola serve -b

To check all available commands::

    nikola help
