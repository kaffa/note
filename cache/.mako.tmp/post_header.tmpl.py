# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1701541317.6379173
_enable_loop = True
_template_filename = 'themes/carpet/templates/post_header.tmpl'
_template_uri = 'post_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_title', 'html_translations', 'html_sourcelink', 'html_post_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

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
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('  <h1 class="title is-1 p-name entry-title" itemprop="headline name">\n    <a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a>\n  </h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(post.translated_to) > 1:
            __M_writer('  <div class="metadata posttranslations translations">\n    <h2 class="subtitle is-2 posttranslations-intro">')
            __M_writer(str(messages("Also available in:")))
            __M_writer('</h2>\n')
            for langname in sorted(translations):
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('        <p><a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a></p>\n')
            __M_writer('  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('  <div class="level-item">\n    <p class="sourceline">\n      <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n    </p>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_post_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        post = context.get('post', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def html_sourcelink():
            return render_html_sourcelink(context)
        def html_translations(post):
            return render_html_translations(context,post)
        def html_title():
            return render_html_title(context)
        __M_writer = context.writer()
        __M_writer('\n<header class="heading">\n  ')
        __M_writer(str(html_title()))
        __M_writer('\n  <div class="level metadata">\n    \n    <div class="level-left">\n      <div class="level-item">\n        <p class="byline author vcard">\n          <span class="byline-name fn">\n')
        if author_pages_generated:
            __M_writer('              <a href="')
            __M_writer(str(_link('author', post.author())))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('</a>\n')
        else:
            __M_writer('              ')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('\n')
        __M_writer('          </span>\n        </p>\n      </div>\n    </div>\n    \n    <div class="level-right">\n      <div class="level-item">\n        <p class="dateline">\n          <a href="')
        __M_writer(str(post.permalink()))
        __M_writer('" rel="bookmark">\n            <time class="published dt-published" datetime="')
        __M_writer(str(post.formatted_date('webiso')))
        __M_writer('" itemprop="datePublished" title="')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('">')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('</time>\n          </a>\n        </p>\n      </div>\n      \n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        <div class="level-item">\n          <p class="commentline">')
            __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
            __M_writer('</p>\n        </div>\n')
        __M_writer('      \n      ')
        __M_writer(str(html_sourcelink()))
        __M_writer('\n      \n')
        if post.meta('link'):
            __M_writer('        <div class="level-item">\n          <p class="linkline">\n            <a href="')
            __M_writer(str(post.meta('link')))
            __M_writer('">')
            __M_writer(str(messages("Original site")))
            __M_writer('</a>\n          </p>\n        </div>\n')
        if post.description():
            __M_writer('        <meta name="description" itemprop="description" content="')
            __M_writer(filters.html_escape(str(post.description())))
            __M_writer('">\n')
        __M_writer('    </div>\n  </div>\n  ')
        __M_writer(str(html_translations(post)))
        __M_writer('\n</header>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/carpet/templates/post_header.tmpl", "uri": "post_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 0, "34": 2, "35": 3, "36": 11, "37": 24, "38": 34, "39": 86, "45": 5, "51": 5, "52": 6, "53": 7, "54": 8, "55": 8, "56": 8, "57": 8, "63": 13, "72": 13, "73": 14, "74": 15, "75": 16, "76": 16, "77": 17, "78": 18, "79": 19, "80": 19, "81": 19, "82": 19, "83": 19, "84": 19, "85": 19, "86": 22, "92": 26, "99": 26, "100": 27, "101": 28, "102": 30, "103": 30, "104": 30, "105": 30, "111": 36, "128": 36, "129": 38, "130": 38, "131": 45, "132": 46, "133": 46, "134": 46, "135": 46, "136": 46, "137": 47, "138": 48, "139": 48, "140": 48, "141": 50, "142": 58, "143": 58, "144": 59, "145": 59, "146": 59, "147": 59, "148": 59, "149": 59, "150": 64, "151": 65, "152": 66, "153": 66, "154": 69, "155": 70, "156": 70, "157": 72, "158": 73, "159": 75, "160": 75, "161": 75, "162": 75, "163": 79, "164": 80, "165": 80, "166": 80, "167": 82, "168": 84, "169": 84, "175": 169}}
__M_END_METADATA
"""
