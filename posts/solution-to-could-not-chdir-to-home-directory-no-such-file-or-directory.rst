.. title: Solution to "Could not chdir to home directory No such file or directory"
.. slug: solution-to-could-not-chdir-to-home-directory-no-such-file-or-directory
.. date: 2024-02-28 22:52:30 UTC+08:00
.. tags: freebsd,zfs,mount 
.. category: Tips
.. link: 
.. description: 当在 FreeBSD 系统中，用户目录丢失的处理
.. type: text


两种登录模式
==================================================

1. 多用户登录模式，可读写全部文件。
2. 单用户登录模式，只可操作根目录下的文件，只能读操作。常用来检查和修复文件系统。


问题现象
==================================================

当开机后，系统提示 "Cound not chdir to home directory /home/your_username No such file or directory"

此时，尝试执行 ``ls /home`` 会发现一无所获，表现为你的用户目录丢失了，非常惊悚。


产生原因
==================================================

1. 黑客获得了你的系统权限，强制删除了你的用户目录。这一般是瞎扯的。
2. 用户创建目录和 zfs 挂载的先后顺序问题。

   详细来说，zfs 是一种高级文件系统，比如可以按需增加容量。

   通常我们会将用户目录放到 zfs 的池中管理，挂载点的对应关系在 zfs 的 dataset 中保存。


   此时，如果用户在 zfs 挂载 /usr/home 以前 (/home 是 /usr/home 的硬连接)，在目录 /home 下创建了目录，再挂载 zfs 的目录时，会覆盖 /home 目录。

   这里怎么理解？就好比目录和文件是对象，挂载点可以是层叠结构，后挂载的目录会指向同样的挂载点，而系统在挂载后，只会显示最后的挂载。

   此时，先前的目录和文件并没有丢失，只是被遮蔽了。


怎么处理
==================================================

进入单用户登录模式登录，尝试执行 ``ls /home`` ，一般会看到「丢失的」目录。

确认这一点后，可以重新进入多用户模式，先用 unmount 命令强制停止挂载 /home 目录

.. code-block:: sh

    zfs unmount zroot/usr/home


问题发现和解决过程
==================================================

我在 https://forums.freebsd.org/threads/lost-home-directory.89382/ 看到，问题可能与 ZFS 有关，在没有思路时，我请教了 OpenAI 的 ChatGPT 3.5，效果好的可怕。

我的提示语如下：『你是协助我工作的精通FreeBSD系统的专家，此时我遇到一个问题向你请教。我的用户名是 xyz，当我从 multiple user mode 登录系统时，/home 和 /usr/home 下找不到 xyz 目录，但当我从 Single user mode 登录系统时，/home 和 /usr/home 下存在 xyz 目录，既存在 /home/xyz 和 /usr/home/xyz，请问现在如何做才可实现，当重启进入 multiple user mode 时依然看到 xyz 目录。我不清楚导致这个现象的原因是什么，可能是因为VPC异常关机，而我的 FreeBSD 是安装在 vpc 上的。』

结果 ChatGPT 给与了初步判断，并给了我处理步骤和命令提示，我继续执行它给的命令，并将结果告诉它，它便接着提示，大约通过十多轮对话，它帮我找到了 zfs 和 mount 的原因，也让我理解了为什么会出现这样的问题。

ChatGPT 真的可以，这里它做到了。

1. 帮助我弥补专业知识不足；
2. 教这些专业知识，让我理解；
3. 就问题给出解答步骤，并可以交互式推进；

所以，我说它真的不错，至少在缺少领域知识的场景下，提高了问题解决的可能性，并缩短了问题解决的时间。

但，这里应看到的时，我们有一个共识：基于 FreeBSD 的存在和表现，它并不会出现无端丢失目录和文件的问题，如果你怀疑，就是在怀疑世界上聪明人的数量，及它们为热爱事物所付出的努力。

如果遇到 FreeBSD 的类似问题，你有此怀疑，这说明，你的思维方式不在正途，你不对劲。
