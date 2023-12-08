.. title: SecureCRT 中 Emacs 向上翻页快捷键 Alt+V 失效
.. slug: securecrt-emacs-alt-v-not-work
.. date: 2023-12-02 08:09:47 UTC+08:00
.. tags: securecrt, emacs 
.. category: Tips
.. link: 
.. description: 
.. type: text

问题现象
==================================================

无论怎么配置 Options 中 Emacs 的配置，M-v 都无法向上滚屏。

配置位置：Menu「Options」-> Edit Default Session... -> Dialog「Session Options - Default」 -> Tree「Category」-> Emulation -> Emacs -> CheckBox「Use ALT as meta key」

尝试修改各相关配置无效。

尝试搜索关键字，Google 中似乎类似问题很少人问。


解决方法
==================================================

因为 Google 搜索关键字 SecureCRT Emacs ALT-V 没有类似提问，所以怀疑我的现象是特例 <-- 想到这一点非常重要。

特例说明，问题产生条件是我独有的，很大可能是我的环境引入的，就是说，不是内因，而是外因，是由于 SecureCRT 之外的程序导致的。

想到这一点后，我尝试逐个关闭电脑相关程序来排除，终于当我关闭「富途牛牛」时，在 Emacs 中，Alt+V 或说 M-v 生效了，可以成功向上滚动。

再查看「富途牛牛」的快捷键清单中，是截屏直播的快捷键。同理还有全屏直播 Alt+C，以及快捷键 Ctrl+1，Alt+1 也显示被其他软件占用。

不知是不是因为富途牛牛的产品经理视角狭隘，或者开发人员用的都是 macOS，要不怎么会设计出这些明显冲突的全局快捷键。


