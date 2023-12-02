# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1701540145.309563
_enable_loop = True
_template_filename = 'themes/carpet/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_header', 'html_search', 'html_site_header', 'html_site_title', 'html_navigation_links', 'html_translation_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
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


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        def html_translation_header():
            return render_html_translation_header(context)
        def html_navigation_links():
            return render_html_navigation_links(context)
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        def html_site_title():
            return render_html_site_title(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="hero-head">\n  <header  id="header" class="nav">\n    <div class="container">\n')
        if logo_url or show_blog_title or len(translations) > 1:
            __M_writer('      <div class="nav-left">\n        ')
            __M_writer(str(html_site_title()))
            __M_writer('\n        ')
            __M_writer(str(html_translation_header()))
            __M_writer('\n      </div>\n')
        __M_writer('      ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n      ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n    </div>\n  </header>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_search(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if search_form:
            __M_writer('  <section class="hero is-primary">\n    <div class="hero-body">\n      <div class="container">\n        <div class="content searchform" role="search">  \n          ')
            __M_writer(str(search_form))
            __M_writer('\n        </div>\n      </div>\n    </div>\n  </section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if logo_url or show_blog_title:
            __M_writer('  <span class="level is-mobile">\n')
        __M_writer('\n')
        if logo_url:
            __M_writer('  <span class="level-item image is-24x24 site-image">\n    <img id="logo" class="site-logo" src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('">\n  </span>\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('  <span id="blog-title" class="level-item site-title">')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</span>\n')
        elif logo_url:
            __M_writer('  <span id="blog-title" class="level-item site-title visuallyhidden">')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</span>\n')
        __M_writer('\n')
        if logo_url or show_blog_title:
            __M_writer('  </span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        carpet__unlink_blog_brand = _import_ns.get('carpet__unlink_blog_brand', context.get('carpet__unlink_blog_brand', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        def html_site_header():
            return render_html_site_header(context)
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<div class="nav-item is-brand">\n  <h1 id="brand" class="site-header">\n')
        if carpet__unlink_blog_brand:
            __M_writer('      ')
            __M_writer(str(html_site_header()))
            __M_writer('\n')
        else:
            __M_writer('      <a href="')
            __M_writer(str(abs_link(_link("root", None, lang))))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('" rel="home">\n        ')
            __M_writer(str(html_site_header()))
            __M_writer('\n      </a>\n')
        __M_writer('  </h1>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<!-- This "nav-toggle" hamburger menu is only visible on mobile -->\n<!-- You need JavaScript to toggle the "is-active" class on "nav-menu" -->\n<span id="nav-toggle-burger" class="nav-toggle">\n  <span></span>\n  <span></span>\n  <span></span>\n</span>\n<div id="menu" class="nav-right nav-menu">\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('    <span class="nav-item is-active">')
                __M_writer(str(text))
                __M_writer('</span>\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer('        <a class="nav-item has-text-right is-active" title="')
                        __M_writer(str(text))
                        __M_writer('" href="')
                        __M_writer(str(permalink))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer(' <span class="sr-only">')
                        __M_writer(str(messages("(active)", lang)))
                        __M_writer('</span></a>\n')
                    else:
                        __M_writer('        <a class="nav-item has-text-right" title="')
                        __M_writer(str(text))
                        __M_writer('" href="')
                        __M_writer(str(suburl))
                        __M_writer('">')
                        __M_writer(str(text))
                        __M_writer('</a>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('      <a class="nav-item is-active" title="')
                    __M_writer(str(text))
                    __M_writer('" href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer(' <span class="sr-only">')
                    __M_writer(str(messages("(active)", lang)))
                    __M_writer('</span></a>\n')
                else:
                    __M_writer('      <a class="nav-item" title="')
                    __M_writer(str(text))
                    __M_writer('" href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a>\n')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n</div>\n<script type="text/javascript">\ndocument.getElementById(\'nav-toggle-burger\').onclick = function() {\n  var myMenu = document.getElementById(\'menu\');\n  var className = \' \' + myMenu.className + \' \';\n  var IS_ACTIVE_CLASS = \'is-active\';\n  if ( ~className.indexOf(\' \' + IS_ACTIVE_CLASS + \' \') ) {\n    myMenu.className = className.replace(\' \' + IS_ACTIVE_CLASS + \' \', \' \');\n  } else {\n    myMenu.className += \' \' + IS_ACTIVE_CLASS;\n  }\n}\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('  <div id="toptranslations" class="nav-item">\n    <h2>')
            __M_writer(str(messages("Languages:")))
            __M_writer('</h2>\n    ')
            __M_writer(str(base.html_translations()))
            __M_writer('\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/carpet/templates/base_header.tmpl", "uri": "base_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 19, "35": 33, "36": 55, "37": 69, "38": 113, "39": 122, "45": 4, "62": 4, "63": 8, "64": 9, "65": 10, "66": 10, "67": 11, "68": 11, "69": 14, "70": 14, "71": 14, "72": 15, "73": 15, "79": 21, "86": 21, "87": 22, "88": 23, "89": 27, "90": 27, "96": 35, "105": 35, "106": 36, "107": 37, "108": 39, "109": 40, "110": 41, "111": 42, "112": 42, "113": 42, "114": 42, "115": 45, "116": 46, "117": 47, "118": 47, "119": 47, "120": 48, "121": 49, "122": 49, "123": 49, "124": 51, "125": 52, "126": 53, "132": 57, "145": 57, "146": 60, "147": 61, "148": 61, "149": 61, "150": 62, "151": 63, "152": 63, "153": 63, "154": 63, "155": 63, "156": 64, "157": 64, "158": 67, "164": 71, "178": 71, "179": 80, "180": 81, "181": 82, "182": 82, "183": 82, "184": 83, "185": 84, "186": 85, "187": 85, "188": 85, "189": 85, "190": 85, "191": 85, "192": 85, "193": 85, "194": 85, "195": 86, "196": 87, "197": 87, "198": 87, "199": 87, "200": 87, "201": 87, "202": 87, "203": 90, "204": 91, "205": 92, "206": 92, "207": 92, "208": 92, "209": 92, "210": 92, "211": 92, "212": 92, "213": 92, "214": 93, "215": 94, "216": 94, "217": 94, "218": 94, "219": 94, "220": 94, "221": 94, "222": 98, "223": 98, "224": 99, "225": 99, "231": 115, "241": 115, "242": 116, "243": 117, "244": 118, "245": 118, "246": 119, "247": 119, "253": 247}}
__M_END_METADATA
"""
