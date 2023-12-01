.. title: 琅環笔记
.. slug: lang-huan-notes
.. date: 2023-11-25 07:18:29 UTC+08:00
.. tags: nikola
.. category: Notes
.. link: 
.. description: 琅環笔记的内容范围 
.. type: text

   

笔记有什么内容？
====================

- 主要内容为编程语言、数据库、操作系统、算法、计算机科学相关内容
- 开发中遇到的坑和 Tips
- 开发手册或开发文档中有的，但不好找的内容
- 文档中没提到，源码中有的内容
  
   
我为何选 Nikola？
====================

- 优点

  1. 支持 rst 格式，还支持 Org mode；
  2. 以 Python 开发，模板并不绑定 Jinja2 或 Mako，都支持；
  3. 支持的格式有
   
     - reStructuredText (default and pre-configured)
     - Markdown (pre-configured since v7.8.7)
     - Jupyter Notebook
     - HTML
     - PHP
     - anything Pandoc supports (including Textile, DocBook, LaTeX, MediaWiki, TWiki, OPML, Emacs Org-Mode, txt2tags, Microsoft Word .docx, EPUB, Haddock markup)

     如果包含插件的格式，还支持

     - AsciiDoc
     - BBCode
     - CommonMark
     - IRC logs
     - Markmin
     - MediaWiki (smc.mw)
     - Misaka
     - ODT
     - Emacs Org-Mode
     - reST with HTML 5 output
     - Textile
     - txt2tags
     - CreoleWiki
     - WordPress posts

  4. 由于 rst 的优势，天然支持混合词法分析器的代码高亮，比如 html+mako
  5. Nikola 名字取得好

     
-  缺点

   1. 主题的设计的感觉，不如 Hugo 的丰富
   2. 安装过程有小坑（等再次安装时会写一篇笔记记录）
    
.. image:: /images/nikola.jpg
    :alt: Nikola
    :width: 400px
    :height: 400px
    :class: ml-5
            
