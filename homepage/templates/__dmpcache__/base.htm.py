# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1601519179.6240678
_enable_loop = True
_template_filename = 'C:/Users/Trent/Documents/1. MISM (Semester 1)/LING 581/RestaurantReviews/restaurant/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>Restaurant Reviews</title>\r\n\r\n        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n\r\n        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n    </head>\r\n    <body>\r\n\r\n        <header>\r\n            <div class="title">Restaurant Reviews</div>\r\n        </header>\r\n\r\n        <main>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n        </main>\r\n\r\n        <footer>\r\n            <div><a href="http://doconix.github.io/django-mako-plus/">Online Documentation</a></div>\r\n            <div><a href="https://github.com/doconix/django-mako-plus/">DMP on GitHub</a></div>\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n                Site content goes here in sub-templates.\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/Documents/1. MISM (Semester 1)/LING 581/RestaurantReviews/restaurant/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "26": 2, "27": 12, "28": 12, "33": 24, "39": 22, "45": 22, "51": 45}}
__M_END_METADATA
"""
