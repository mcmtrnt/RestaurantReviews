# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1605735924.4843574
_enable_loop = True
_template_filename = 'C:/Users/Trent/Documents/1. MISM (Semester 1)/LING 581/RestaurantReviews/restaurant/homepage/templates/index.charts.html'
_template_uri = '/homepage/templates/index.charts.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        genSentVader = context.get('genSentVader', UNDEFINED)
        foodQualSentVader = context.get('foodQualSentVader', UNDEFINED)
        name = context.get('name', UNDEFINED)
        self = context.get('self', UNDEFINED)
        commonFoods = context.get('commonFoods', UNDEFINED)
        covidSentVader = context.get('covidSentVader', UNDEFINED)
        custServSentVader = context.get('custServSentVader', UNDEFINED)
        column = context.get('column', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<div class="subtitle">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(name))
        __M_writer('</div>\r\n\r\n        <select id="dropdown')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(column))
        __M_writer('">\r\n            <option>Chick-fil-A</option>\r\n            <option>Cheesecake Factory</option>\r\n            <option>Wallabys</option>\r\n        </select>\r\n        <div id="btn" class="btn" onclick="restaurant(')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(column))
        __M_writer(')">Go</div>\r\n\r\n        <div class="content">\r\n            <h2>General Sentiment</h2>\r\n            <div class="score">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(genSentVader))
        __M_writer('</div>\r\n        </div>\r\n            <progress max="1" value=')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(genSentVader))
        __M_writer('></progress>\r\n\r\n        <div class="content">\r\n            <h2>Customer Service</h2>\r\n            <div class="score">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(custServSentVader))
        __M_writer('</div>\r\n        </div>\r\n            <progress max="1" value=')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(custServSentVader))
        __M_writer('></progress>\r\n\r\n        <div class="content">\r\n            <h2>Food Quality</h2>\r\n            <div class="score">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(foodQualSentVader))
        __M_writer('</div>\r\n        </div>\r\n            <progress max="1" value=')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(foodQualSentVader))
        __M_writer('></progress>\r\n\r\n        <div class="content">\r\n            <h2>Covid Safety</h2>\r\n            <div class="score">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(covidSentVader))
        __M_writer('</div>\r\n        </div>\r\n            <progress max="1" value=')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(covidSentVader))
        __M_writer('></progress>\r\n        \r\n        <div class="content">Food Mentions:</div>\r\n')
        for f in commonFoods:
            __M_writer('            <li>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(f[0]))
            __M_writer(': ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(f[1]))
            __M_writer('</li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/Documents/1. MISM (Semester 1)/LING 581/RestaurantReviews/restaurant/homepage/templates/index.charts.html", "uri": "/homepage/templates/index.charts.html", "source_encoding": "utf-8", "line_map": {"18": 0, "31": 1, "32": 1, "33": 1, "34": 3, "35": 3, "36": 8, "37": 8, "38": 12, "39": 12, "40": 14, "41": 14, "42": 18, "43": 18, "44": 20, "45": 20, "46": 24, "47": 24, "48": 26, "49": 26, "50": 30, "51": 30, "52": 32, "53": 32, "54": 35, "55": 36, "56": 36, "57": 36, "58": 36, "59": 36, "65": 59}}
__M_END_METADATA
"""
