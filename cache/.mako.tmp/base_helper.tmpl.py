# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1701540146.3465395
_enable_loop = True
_template_filename = 'themes/carpet/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'late_load_css', 'preload_stylesheets', 'html_stylesheets', 'html_feedlinks', 'html_translations', 'late_load_js']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        url_type = context.get('url_type', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        carpet__head_prefix = context.get('carpet__head_prefix', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        title = context.get('title', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        def late_load_css():
            return render_late_load_css(context)
        comment_system = context.get('comment_system', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        description = context.get('description', UNDEFINED)
        carpet__late_load_css = context.get('carpet__late_load_css', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        is_rtl = context.get('is_rtl', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n')
        if carpet__head_prefix:
            __M_writer('    ')
            __M_writer(str(carpet__head_prefix))
            __M_writer('\n')
        __M_writer('  <meta charset="utf-8">\n  \n')
        if use_base_tag:
            __M_writer('    <base href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('  \n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('  \n  <meta name="viewport" content="width=device-width">\n  \n')
        if title == blog_title:
            __M_writer('    <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('    <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n  <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\n  <meta name="generator" content="Nikola (getnikola.com)">\n  ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n  <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('      <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('    <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('    <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        __M_writer('  \n')
        if nextlink:
            __M_writer('    <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('  \n')
        if not carpet__late_load_css:
            __M_writer('    ')
            __M_writer(str(html_stylesheets()))
            __M_writer('\n')
        __M_writer('\n  ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('    <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('    <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n  ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        if carpet__late_load_css:
            __M_writer('    ')
            __M_writer(str(late_load_css()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_css(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def preload_stylesheets():
            return render_preload_stylesheets(context)
        def html_stylesheets():
            return render_html_stylesheets(context)
        __M_writer = context.writer()
        __M_writer('\n  ')
        __M_writer(str(preload_stylesheets()))
        __M_writer('\n  <noscript id="deferred-styles">\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n  </noscript>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_preload_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('    <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n      href="/assets/css/all.css">\n')
            else:
                __M_writer('    <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n      href="/assets/css/all-nocdn.css">\n')
        else:
            __M_writer('  <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n    href="/assets/css/rst.css">\n  <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n    href="/assets/css/code.css">\n  <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n    href="/assets/css/font-awesome.css">\n  <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n    href="/assets/css/styles.css">\n')
            if has_custom_css:
                __M_writer('    <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n      href="/assets/css/custom.css">\n')
        if needs_ipython_css:
            __M_writer('  <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n    href="/assets/css/ipython.min.css">\n  <link rel="preload" type="text/css" as="style" onload="this.rel=\'stylesheet\'"\n    href="/assets/css/nikola_ipython.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('    <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('    <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('  <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n  <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n  <link href="/assets/css/font-awesome.css" rel="stylesheet" type="text/css">\n  <link href="/assets/css/styles.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('    <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('  <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n  <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('  ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('      <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('    <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('      <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('    <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="level translations">\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('      <div class="level-item has-text-centered">\n        <a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a>\n      </div>\n')
        __M_writer('</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        carpet__late_load_css = context.get('carpet__late_load_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if carpet__late_load_css:
            __M_writer('    <script>!function(e){"use strict";var t=function(t,n,r){function o(e){return i.body?e():void setTimeout(function(){o(e)})}function a(){d.addEventListener&&d.removeEventListener("load",a),d.media=r||"all"}var l,i=e.document,d=i.createElement("link");if(n)l=n;else{var s=(i.body||i.getElementsByTagName("head")[0]).childNodes;l=s[s.length-1]}var u=i.styleSheets;d.rel="stylesheet",d.href=t,d.media="only x",o(function(){l.parentNode.insertBefore(d,n?l:l.nextSibling)});var f=function(e){for(var t=d.href,n=u.length;n--;)if(u[n].href===t)return e();setTimeout(function(){f(e)})};return d.addEventListener&&d.addEventListener("load",a),d.onloadcssdefined=f,f(a),d};"undefined"!=typeof exports?exports.loadCSS=t:e.loadCSS=t}("undefined"!=typeof global?global:this),function(e){if(e.loadCSS){var t=loadCSS.relpreload={};if(t.support=function(){try{return e.document.createElement("link").relList.supports("preload")}catch(e){return!1}},t.poly=function(){for(var t=e.document.getElementsByTagName("link"),n=0;n<t.length;n++){var r=t[n];"preload"===r.rel&&"style"===r.getAttribute("as")&&(e.loadCSS(r.href,r),r.rel=null)}},!t.support()){t.poly();var n=e.setInterval(t.poly,300);e.addEventListener&&e.addEventListener("load",function(){t.poly(),e.clearInterval(n)}),e.attachEvent&&e.attachEvent("onload",function(){e.clearInterval(n)})}}}(this);</script>\n')
        __M_writer('  ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/carpet/templates/base_helper.tmpl", "uri": "base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 82, "23": 89, "24": 120, "25": 142, "26": 165, "27": 177, "28": 184, "34": 3, "67": 3, "68": 6, "69": 7, "70": 8, "71": 10, "72": 11, "73": 13, "74": 14, "75": 15, "76": 17, "77": 18, "78": 21, "79": 21, "80": 21, "81": 23, "82": 24, "83": 24, "84": 24, "85": 26, "86": 28, "87": 29, "88": 29, "89": 29, "90": 31, "91": 32, "92": 33, "93": 33, "94": 33, "95": 35, "96": 38, "97": 39, "98": 39, "99": 39, "100": 40, "101": 41, "102": 41, "103": 41, "104": 41, "105": 41, "106": 43, "107": 44, "108": 44, "109": 46, "110": 46, "111": 47, "112": 47, "113": 49, "114": 50, "115": 51, "116": 51, "117": 51, "118": 51, "119": 51, "120": 51, "121": 51, "122": 54, "123": 55, "124": 56, "125": 56, "126": 56, "127": 58, "128": 59, "129": 60, "130": 60, "131": 60, "132": 62, "133": 63, "134": 64, "135": 64, "136": 64, "137": 66, "138": 67, "139": 68, "140": 68, "141": 68, "142": 70, "143": 71, "144": 71, "145": 72, "146": 73, "147": 74, "148": 75, "149": 75, "150": 75, "151": 77, "152": 78, "153": 78, "154": 79, "155": 80, "156": 80, "157": 80, "163": 84, "171": 84, "172": 85, "173": 85, "174": 87, "175": 87, "181": 91, "189": 91, "190": 92, "191": 93, "192": 94, "193": 96, "194": 97, "195": 100, "196": 101, "197": 109, "198": 110, "199": 114, "200": 115, "206": 122, "214": 122, "215": 123, "216": 124, "217": 125, "218": 126, "219": 127, "220": 129, "221": 130, "222": 134, "223": 135, "224": 138, "225": 139, "231": 144, "242": 144, "243": 145, "244": 146, "245": 146, "246": 146, "247": 147, "248": 148, "249": 149, "250": 150, "251": 150, "252": 150, "253": 150, "254": 150, "255": 152, "256": 153, "257": 153, "258": 153, "259": 156, "260": 157, "261": 158, "262": 159, "263": 159, "264": 159, "265": 159, "266": 159, "267": 161, "268": 162, "269": 162, "270": 162, "276": 167, "286": 167, "287": 169, "288": 170, "289": 171, "290": 172, "291": 172, "292": 172, "293": 172, "294": 172, "295": 172, "296": 176, "302": 179, "308": 179, "309": 180, "310": 181, "311": 183, "312": 183, "313": 183, "319": 313}}
__M_END_METADATA
"""
