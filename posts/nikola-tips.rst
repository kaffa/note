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
