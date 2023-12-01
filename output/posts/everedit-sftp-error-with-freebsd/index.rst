.. title: EverEdit SFTP Error With FreeBSD
.. slug: everedit-sftp-error-with-freebsd
.. date: 2023-12-01 11:09:38 UTC+08:00
.. tags: libcurl,freebsd
.. category: Notes 
.. link: 
.. description: 
.. type: text


问题现象
==================================================

EverEdit 4 内置 SFTP 插件连接 FreeBSD 13.2 SSH 时，提示如下::

  [23:19:56]:Hostname was found in DNS cache
  [23:19:56]:  Trying 192.168.2.81...
  [23:19:56]:Adding handle: conn: 0x22356d0cfa0
  [23:19:56]:Adding handle: send: 0
  [23:19:56]:Adding handle: recv: 0
  [23:19:56]:Curl_addHandleToPipeline: length: 1
  [23:19:56]:- Conn 1 (0x22356d0cfa0) send_pipe: 1, recv_pipe: 0
  [23:19:56]:Connected to 192.168.2.81 (192.168.2.81) port 22 (#1)
  [23:19:56]:Failure establishing ssh session
  [23:19:56]:Closing connection 1

而使用其他 SFTP 客户端是完全正常的。



解决方法
==================================================


已提交给作者，还没找出解决办法。

在网上查找说是连接不上 FreeBSD 13.2 的 sftp，可能与 libcurl 有关。

但还没有时间写代码来调试。

待ee作者更新后，我再咨询。


参考
==================================================

1. https://curl.se/libcurl/c/sftpget.html
2. https://curl-users.cool.haxx.narkive.com/ppppPXNc/curl-sftp-failure-establishing-ssh-session
   
