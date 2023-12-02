.. title: Nikola Tips
.. slug: nikola-tips
.. date: 2023-11-27 19:34:15 UTC+08:00
.. tags: nikola
.. category: Tips
.. link: 
.. description: 这篇记录 Nikola 使用的小技巧
.. type: text

Nikola Tips
====================


1. Nikola serve 自动刷新的命令行怎么写？
--------------------------------------------------

.. code-block :: shell

  nikola auto

即使 **conf.py** 中已绑定非127.0.0.1的地址，上面的命令也只会在127.0.0.1启动调试。

没有去看源代码，可能这样实现从安全角度存在一定的合理性。

如果需要任意主机都能获得访问，可使用 -a 参数指定地址0.0.0.0

.. code-block :: shell

  nikola auto -a0.0.0.0
   

2. Nikola Theme 如何定制 css
--------------------------------------------------

如果在模板中有代码

.. code-block :: html+mako
  
  %if has_custom_css:
    <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">
  %endif

因此，增加 /assets/css/custom.css 文件即可。


3. Nikola 如何推送到 GitHub
--------------------------------------------------

先设置好 git 推送

.. code-block :: sh

  git config --global --add safe.directory /usr/home/kaffa/web/note.tt4e.com
  git config --global user.email "kaffacoffee@outlook.com"
  git config --global user.name "Kaffa"


将以下内容保存为 aio.sh 脚本

.. code-block :: sh

  #!/bin/bash
  #
  # nikola output push to github
  cd ~/web/note.tt4e.com/
  nikola build
  git add .
  git commit -am 'Kaffa'
  git push

先 su 到 root 用户，然后运行以下命令，再 su 会当前用户

.. code-block :: sh 

  chown -R kaffa:wheel .git
  chmod -R 777 ./aio.sh

如果遇到错误提示 Unable to create ** /.git/index.lock: Permission denied，则需要

.. code-block :: sh

  chown -R kaffa:wheel .git  

其中 用户名和所属组，可以用 groups 命令查看。

完成书上步骤后，则每次可以运行 aio.sh 来推送 GitHub，GitHub 收到推送后，会使用 GitHub Action 来处理发布。


使用以上方法是有效的，但却说明没有认真读 nikola 文档。

Nikola 官方支持推送到 GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`官方文档 <https://getnikola.com/handbook.html#toc-entry-60>`_


解释一下：

1. GITHUB_DEPLOY_BRANCH：发布分支，是 Nikola 产生的 HTML 文件，建议命名为 src。
2. GITHUB_SOURCE_BRANCH：源码分支，建议在 GitHub 上设置为默认分支，建议命名为 main，而不是 master[#fn1]_。
3. GITHUB_REMOTE_NAME：远程仓库名；
4. GITHUB_COMMIT_SOURCE：True，发布时会自动提交 src 分支。

补充：

采用这种方法时，Github Pages 的 Build and deployment 一节，source 下拉框中，要选择 Deploy from a branch，而不是 GitHub Actions。

.. code-block ::


脚注
==================================================
[#fn1] master：类似 master，slave 这样带有种族歧视色彩的词，在编程世界中将不再继续使用，现有使用也逐步 `重命名 <https://github.com/github/renaming>`_。
