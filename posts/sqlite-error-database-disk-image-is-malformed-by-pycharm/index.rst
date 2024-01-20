.. title: SQLite Error database disk image is malformed by PyCharm
.. slug: sqlite-error-database-disk-image-is-malformed-by-pycharm
.. date: 2023-12-13 21:14:50 UTC+08:00
.. tags: pycharm,sqlite
.. category: Tips
.. link: 
.. description: 
.. type: text


大多数 Tips 背后总能找到一个设计错误
==================================================

Tips 之所以让人眼前一亮，那是因为这个 Tips 的结构不寻常。

大体上，是因为设计者没有想到，或者想到了，但没有设计好导致的。


比如下面这个：


database disk image is malformed
==================================================

SQLite 提示 "database disk image is malformed"

看起来很惊悚，说是数据库磁盘镜像畸形了。

第一感觉似乎是磁盘硬件坏道了？


问题重现
==================================================

当我在 PyCharm 中选中了项目的根目录后，在菜单 File -> File Properties -> Line Separators 的切换后，SQLite 数据库文件报错了；

我进行这个操作的主要原因是，每当我添加文件到 git 时，以 LF 为分隔符的 sitemap.xml 文件总是有一个 warning；

而这个报错的主要原因，被证明是一个 Python 2 的遗留问题导致的。


.. code-block :: bash

   >git add .  
   warning: LF will be replaced by CRLF in docs/sitemap.xml.
   The file will have its original line endings in your working directory

问题原因
==================================================

没有充分证实，但非常有可能是 LF 到 CRLF 的替换损坏了 SQLite 的数据库文件。

你想问问 PyCharm，你怎么这么蠢？

PyCharm 可能会说，怪我干什么，我只是个工具！

但我认为吧，PyCharm 确实有理由识别这是一个数据库文件吧，毕竟你是可以直接打开浏览和处理的。

好在此处，是之用到 SQLite 作为数据生成的本地缓存，且在 GitHub 上有备份，于是拿了一份下来本地覆盖既修复了。
