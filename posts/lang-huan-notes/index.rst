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

     实际上支持的种类就是 pygments 所支持的，Demo 在 http://pygments.org/

     目前可用的如下：

     abap | abnf | ada, ada95, ada2005 | adl | agda | ahk, autohotkey | alloy | ampl | antlr-as, antlr-actionscript | antlr-cpp | antlr-csharp, antlr-c# | antlr-java | antlr-objc | antlr-perl | antlr-python | antlr-ruby, antlr-rb | antlr | apacheconf, aconf, apache | apl | applescript | arduino | as, actionscript | as3, actionscript3 | aspectj | aspx-cs | aspx-vb | asy, asymptote | at, ambienttalk, ambienttalk/2 | autoit | awk, gawk, mawk, nawk | basemake | bash, sh, ksh, shell | bat, batch, dosbatch, winbatch | bbcode | bc | befunge | blitzbasic, b3d, bplus | blitzmax, bmax | bnf | boo | boogie | brainfuck, bf | bro | bugs, winbugs, openbugs | c-objdump | c | ca65 | cadl | camkes, idl4 | cbmbas | ceylon | cfc | cfengine3, cf3 | cfm | cfs | chai, chaiscript | chapel, chpl | cheetah, spitfire | cirru | clay | clean | clojure, clj | clojurescript, cljs | cmake | cobol | cobolfree | coffee-script, coffeescript, coffee | common-lisp, cl, lisp | componentpascal, cp | console, shell-session | control, debcontrol | coq | cpp, c++ | cpp-objdump, c++-objdumb, cxx-objdump | cpsa | crmsh, pcmk | croc | cryptol, cry | csharp, c# | csound, csound-orc | csound-document, csound-csd | csound-score, csound-sco | css+django, css+jinja | css+erb, css+ruby | css+genshitext, css+genshi | css+lasso | css+mako | css+mako | css+mozpreproc | css+myghty | css+php | css+smarty | css | cucumber, gherkin | cuda, cu | cypher | cython, pyx, pyrex | d-objdump | d | dart | delphi, pas, pascal, objectpascal | dg | diff, udiff | django, jinja | docker, dockerfile | doscon | dpatch | dtd | duel, jbst, jsonml+bst | dylan-console, dylan-repl | dylan-lid, lid | dylan | earl-grey, earlgrey, eg | easytrieve | ebnf | ec | ecl | eiffel | elixir, ex, exs | elm | emacs, elisp, emacs-lisp | erb | erl | erlang | evoque | extempore | ezhil | factor | fan | fancy, fy | felix, flx | fish, fishshell | flatline | fortran | fortranfixed | foxpro, vfp, clipper, xbase | fsharp | gap | gas, asm | genshi, kid, xml+genshi, xml+kid | genshitext | glsl | gnuplot | go | golo | gooddata-cl | gosu | groff, nroff, man | groovy | gst | haml | handlebars | haskell, hs | haxeml, hxml | hexdump | hsail, hsa | html+cheetah, html+spitfire, htmlcheetah | html+django, html+jinja, htmldjango | html+evoque | html+genshi, html+kid | html+handlebars | html+lasso | html+mako | html+mako | html+myghty | html+php | html+smarty | html+twig | html+velocity | html | http | hx, haxe, hxsl | hybris, hy | hylang | i6t | idl | idris, idr | iex | igor, igorpro | inform6, i6 | inform7, i7 | ini, cfg, dosini | io | ioke, ik | irc | isabelle | j | jade | jags | jasmin, jasminxt | java | javascript+mozpreproc | jcl | jlcon | js+cheetah, javascript+cheetah, js+spitfire, javascript+spitfire | js+django, javascript+django, js+jinja, javascript+jinja | js+erb, javascript+erb, js+ruby, javascript+ruby | js+genshitext, js+genshi, javascript+genshitext, javascript+genshi | js+lasso, javascript+lasso | js+mako, javascript+mako | js+mako, javascript+mako | js+myghty, javascript+myghty | js+php, javascript+php | js+smarty, javascript+smarty | js, javascript | jsgf | json | jsonld, json-ld | jsp | julia, jl | kal | kconfig, menuconfig, linux-config, kernel-config | koka | kotlin | lagda, literate-agda | lasso, lassoscript | lcry, literate-cryptol, lcryptol | lean | less | lhs, literate-haskell, lhaskell | lidr, literate-idris, lidris | lighty, lighttpd | limbo | liquid | live-script, livescript | llvm | logos | logtalk | lsl | lua | make, makefile, mf, bsdmake | mako | mako | maql | mask | mason | mathematica, mma, nb | matlab | matlabsession | minid | modelica | modula2, m2 | monkey | moocode, moo | moon, moonscript | mozhashpreproc | mozpercentpreproc | mql, mq4, mq5, mql4, mql5 | mscgen, msc | mupad | mxml | myghty | mysql | nasm | ncl | nemerle | nesc | newlisp | newspeak | nginx | nimrod, nim | nit | nixos, nix | nsis, nsi, nsh | numpy | objdump-nasm | objdump | objective-c++, objectivec++, obj-c++, objc++ | objective-c, objectivec, obj-c, objc | objective-j, objectivej, obj-j, objj | ocaml | octave | odin | ooc | opa | openedge, abl, progress | pacmanconf | pan | parasail | pawn | perl, pl | perl6, pl6 | php, php3, php4, php5 | pig | pike | pkgconfig | plpgsql | postgresql, postgres | postscript, postscr | pot, po | pov | powershell, posh, ps1, psm1 | praat | prolog | properties, jproperties | protobuf, proto | ps1con | psql, postgresql-console, postgres-console | puppet | py3tb | pycon | pypylog, pypy | pytb | python, py, sage | python3, py3 | qbasic, basic | qml, qbs | qvto, qvt | racket, rkt | ragel-c | ragel-cpp | ragel-d | ragel-em | ragel-java | ragel-objc | ragel-ruby, ragel-rb | ragel | raw | rb, ruby, duby | rbcon, irb | rconsole, rout | rd | rebol | red, red/system | redcode | registry | resource, resourcebundle | rexx, arexx | rhtml, html+erb, html+ruby | roboconf-graph | roboconf-instances | robotframework | rql | rsl | rst, rest, restructuredtext | rts, trafficscript | rust | sass | sc, supercollider | scala | scaml | scheme, scm | scilab | scss | shen | silver | slim | smali | smalltalk, squeak, st | smarty | sml | snobol | sourceslist, sources.list, debsources | sp | sparql | spec | splus, s, r | sql | sqlite3 | squidconf, squid.conf, squid | ssp | stan | swift | swig | systemverilog, sv | tads3 | tap | tcl | tcsh, csh | tcshcon | tea | termcap | terminfo | terraform, tf | tex, latex | text | thrift | todotxt | trac-wiki, moin | treetop | ts, typescript | turtle | twig | typoscript | typoscriptcssdata | typoscripthtmldata | urbiscript | vala, vapi | vb.net, vbnet | vcl | vclsnippets, vclsnippet | vctreestatus | velocity | verilog, v | vgl | vhdl | vim | wdiff | x10, xten | xml+cheetah, xml+spitfire | xml+django, xml+jinja | xml+erb, xml+ruby | xml+evoque | xml+lasso | xml+mako | xml+mako | xml+myghty | xml+php | xml+smarty | xml+velocity | xml | xquery, xqy, xq, xql, xqm | xslt | xtend | xul+mozpreproc | yaml+jinja, salt, sls | yaml | zephir |


     可以通过以下命令查看

     .. code-block :: sh

       pygmentize -L


     5. Nikola 如果是艾志恒，会不会唱：

        | 在房间里洗个澡
        | 同时在思考其它的jamstack哪个能比我屌
        | Posts keep increasing
        | 你们格式都认不到
        | 我们code好
        | 但目前我还嫌自己PR的少

     
-  缺点

   1. 主题的设计的感觉，不如 Hugo 的丰富
   2. 安装过程有小坑（等再次安装时会写一篇笔记记录）
    
.. image:: /images/nikola.jpg
    :alt: Nikola
    :width: 400px
    :height: 400px
    :class: ml-5
            

