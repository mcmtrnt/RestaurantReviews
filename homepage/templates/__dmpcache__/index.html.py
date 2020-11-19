# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1605735505.0008328
_enable_loop = True
_template_filename = 'C:/Users/Trent/Documents/1. MISM (Semester 1)/LING 581/RestaurantReviews/restaurant/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        genSentVader = context.get('genSentVader', UNDEFINED)
        foodQualSentVader = context.get('foodQualSentVader', UNDEFINED)
        self = context.get('self', UNDEFINED)
        commonFoods = context.get('commonFoods', UNDEFINED)
        covidSentVader = context.get('covidSentVader', UNDEFINED)
        custServSentVader = context.get('custServSentVader', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        genSentVader = context.get('genSentVader', UNDEFINED)
        foodQualSentVader = context.get('foodQualSentVader', UNDEFINED)
        self = context.get('self', UNDEFINED)
        commonFoods = context.get('commonFoods', UNDEFINED)
        covidSentVader = context.get('covidSentVader', UNDEFINED)
        custServSentVader = context.get('custServSentVader', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div id="restaurant1" class="restaurant">\r\n        <div class="subtitle">Chick Fil A</div>\r\n\r\n        <select id="dropdown1">\r\n            <option>Chick-fil-A</option>\r\n            <option>Cheesecake Factory</option>\r\n            <option>Wallabys</option>\r\n        </select>\r\n        <div id="btn" class="btn" onclick="restaurant(1)">Go</div>\r\n\r\n        <div class="content">\r\n            <h2>General Sentiment</h2>\r\n            <div class="score">')
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
        __M_writer('    </div>\r\n\r\n\r\n    <div id="restaurant2" class="restaurant">\r\n        <div class="subtitle">Chick Fil A</div>\r\n\r\n        <select id="dropdown2">\r\n            <option>Chick-fil-A</option>\r\n            <option>Cheesecake Factory</option>\r\n            <option>Wallabys</option>\r\n        </select>\r\n        <div id="btn" class="btn" onclick="restaurant(2)">Go</div>\r\n\r\n        <div class="content">\r\n            <h2>General Sentiment</h2>\r\n            <div class="score">')
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
        __M_writer('\r\n    </div>\r\n\r\n\r\n\r\n\r\n    \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Trent/Documents/1. MISM (Semester 1)/LING 581/RestaurantReviews/restaurant/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 91, "53": 3, "65": 3, "66": 17, "67": 17, "68": 19, "69": 19, "70": 23, "71": 23, "72": 25, "73": 25, "74": 29, "75": 29, "76": 31, "77": 31, "78": 35, "79": 35, "80": 37, "81": 37, "82": 40, "83": 41, "84": 41, "85": 41, "86": 41, "87": 41, "88": 43, "89": 58, "90": 58, "91": 60, "92": 60, "93": 64, "94": 64, "95": 66, "96": 66, "97": 70, "98": 70, "99": 72, "100": 72, "101": 76, "102": 76, "103": 78, "104": 78, "105": 81, "106": 82, "107": 82, "108": 82, "109": 82, "110": 82, "111": 84, "117": 111}}
__M_END_METADATA
"""
