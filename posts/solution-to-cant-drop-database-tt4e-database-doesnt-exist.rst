.. title: Solution to Can't drop database 'tt4e'; database doesn't exist
.. slug: solution-to-cant-drop-database-tt4e-database-doesnt-exist
.. date: 2024-05-27 01:23:39 UTC+08:00
.. tags: mysql
.. category: Tips
.. link: 
.. description: 本文解决在 mysql 中 show databases 可以显示但 drop database 却失败的情况
.. type: text



问题现象
==========

一台服务器上，有一个数据库怎么也删不掉，但可以显示。


::
   
    MariaDB [(none)]> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              |
    | performance_schema |
    | sys                |
    | xxx                |
    +--------------------+
    5 rows in set (0.002 sec)

    MariaDB [(none)]> drop database xxx;
    ERROR 1008 (HY000): Can't drop database 'xxx'; database doesn't exist


问题解决
==========

1. 用 ps aux 查看进程，发现 mariadbd 进程，发现未使用配置文件，则使用的默认路径配置；
2. 查看默认配置文件::
   
   cat /etc/mysql/mariadb.cnf
   cat /etc/mysql/mariadb.conf.d/50-server.cnf 

3. 发现默认配置文件中未指定数据路径，则进入默认数据路径，并查看文件权限，发现 xxx 的所有者是 root 用户::

   cd /var/lib/mysql/
   ls -l   
   
   
4. 猜测是使用了不同的用户创建的数据库导致没有权限，执行 cat /etc/passwd 查看用户，发现 mysql 用户；
5. 于是将 xxx 目录和下面文件的所有者修改为 mysql

   sudo chown mysql:mysql xxx/
   cd xxx/
   ls
   sudo chown mysql:mysql db.opt
6. 执行 systemctl restart mysql 重启服务，进入 mysql 命令行客户端，再次执行 drop database xxx 即成功删除。
