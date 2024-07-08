.. title: 解决 CSS fixed 网页元素挡住锚链的问题
.. slug: solution-for-html-anchor-element-linked-to-css-fixed-elements
.. date: 2024-07-09 00:25:17 UTC+08:00
.. tags: css
.. category: Tips
.. link: 
.. description: 
.. type: text

解决方案
====================

问题描述
--------------------

如果网页顶部元素使用 CSS fixed 固定在顶部，当点击链接的锚链时，网页会滚动到顶部，锚链元素则会被这个顶部固定元素遮挡。

解决方案一种
--------------------

解决方式有多种，我认为侵入较少的方式是在元素之上插入一个用来校准位置的隐藏元素。

这里假设需要校准滚动的是脚注元素 .footnote


::

    .footnote-target {
      position: relative;
      top: -5rem; /* negative value of the fixed html element height */
      height: 0;
      overflow: hidden;
    }

::

    $(function(){
      $('.footnote').before(function(i) {
        return '<a class="footnote-target" name="' + this.id + '"></a>';
      }).removeAttr('id');
    });
