.. title: SecureCRT 中 Emacs 或 Vim 方向键变成 ABCD 的解决方法
.. slug: solution-to-arrow-keys-changed-into-abcd-in-securecrt-emacs-vim
.. date: 2023-11-25 07:25:01 UTC+08:00
.. tags: securecrt
.. category: Tips
.. link: 
.. description: 解决SecureCRT中的方向键变成ABCD的问题。 
.. type: text


问题现象
----------
在 SecureCRT 中使用 Emacs 或 Vim 方向键变成 ABCD，看起来是键盘的模式导致的。

解决方法
----------
   
1. 打开菜单 Options -> Edit Default Session...
2. 在打开的窗口 Session Options - Default 中，点击左侧 Terminal -> Emulation -> Modes
3. 右侧的 Emulation Modes 下，Numeric keypad 和 Application keypad 单选框组中，选择 Application keypad。
4. 保存
