.. title: Reset Ubuntu Linux Password
.. slug: reset-ubuntu-linux-password
.. date: 2024-02-08 06:47:39 UTC+08:00
.. tags: ubuntu 
.. category: Tips
.. link: 
.. description: 
.. type: text

前提
==================================================

须具有本地权限，通俗的说就是，需要肉身在服务器旁边。


步骤
==================================================

1. 启动服务器时按住 Shift 键，会进入 GNU GRUB  version x.yz... 界面
2. 在 GNU GRUB  version x.yz... 界面下方至少会出现以下选项：

   - Ubuntu
   - \*Advanced options for Ubuntu

   选择 Advanced options for Ubuntu，按回车键；

3. 出现新的选项：

   - Ubuntu, with Linux ...
   - \*Ubuntu, with Linux ... (recovery mode)

   选择带有 (recovery mode) 的一行，按回车键；

4. 系统会显示一些输出并跳转到 Recovery Menu 菜单界面，选项如下：

   - resume
   - clean
   - dpkg
   - failsafeX
   - fsck
   - grub
   - network
   - root
   - system-summary

   选择 root，按回车键

5. 重新 mount 具有写权限的 root，运行命令：::

    mount -rw -o remount /

6. 使用 ``ls /home`` 命令可以查看用户名，假设是 USER1，则使用如下命令重置密码::

    passwd USER1

7. 根据命令提示，你可以完成密码修改，然后退出到 Recovery Menu，选择 resume 重启，然后就可以使用上一步修改的新密码进入系统了。
   

   
