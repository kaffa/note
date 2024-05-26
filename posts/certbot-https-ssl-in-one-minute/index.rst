.. title: certbot 一分钟搞定 https 的 ssl 证书申请
.. slug: certbot-https-ssl-in-one-minute
.. date: 2024-05-27 03:29:32 UTC+08:00
.. tags: certbot 
.. category: Tips
.. link: 
.. description: 本文讲解如何最快申请 ssl 证书，certbot 是个造福大家的项目。
.. type: text

不要去某云手动申请免费证书，再等待不知道多久，再下载配置证书了。

这个过程已经被 certbot 项目自动化了，ssl 作为互联网基础设施的一部分，这本该是被简单解决和处理的事。

certbot 项目由此而生。


Ubuntu 为例
====================

::

   sudo apt-get install certbot
   sudo apt-get install python3-certbot-apache
   sudo certbot --apache

如果使用的是 nginx 则::

   sudo certbot --nginx


按提示输入即可，秒通，连Web服务器都不用手动重启。
