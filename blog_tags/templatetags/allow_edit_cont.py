from django import template
from django.utils.safestring import mark_safe

register=template.Library()


@register.filter
def allow_reg_tags(text):
    text=text.replace("&","&amp;").replace('<','&lt;').replace('>','&gt;').replace('"','&quot;').replace("'","&#39;").replace('&lt;b&gt;',
        '<b>').replace('&lt;/b&gt;','</b>').replace('&lt;i&gt;','<i>').replace('&lt;/i&gt;','</i>').replace('&lt;br&gt;','<br>').replace('&lt;u&gt;','<u>').replace('&lt;/u&gt;',
        '</u>')
    op_tags={'<b>':text.count('<b>'),'<i>':text.count('<i>'),'<u>':text.count('<u>')}
    for tag in op_tags.keys():
        cl_tag=tag[:1]+'/'+tag[1:]
        cl_tag_num=text.count(cl_tag)
        n=op_tags[tag]-cl_tag_num
        if n>0: text+=cl_tag*n
    return mark_safe(text)

