.. title: 「'ssh'不是内部或外部命令，也不是可运行的程序或批处理文件」的解决方法
.. slug: ssh-is-not-recognized-as-an-internal-or-external-command
.. date: 2023-11-27 13:17:12 UTC+08:00
.. tags: openssh, ssh
.. category: Tips
.. link: 
.. description: 
.. type: text


问题现象
====================

当在 `Windows Terminal <https://github.com/microsoft/terminal>`_ 中运行 *ssh* 命令时，终端中提示：

.. code-block:: text
                
  'ssh'不是内部或外部命令，也不是可运行的程序或批处理文件

English Version

.. code-block:: text

  'ssh' is not recognized as an internal or external command, operable program or batch file.

解决方法
====================

在 Windows 设置中安装 OpenSSH 客户端，且在环境变量 PATH 中加入：

.. code-block:: text

  C:\Windows\System32\OpenSSH
  
验证方法：检查以上目录中是否有 ssh.exe 文件。


