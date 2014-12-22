from django import template

register = template.Library()

@register.inclusion_tag('column.html')
def column_tag(objects):
    total = objects.count()
    col_one =objects[0:(total/2)]
    col_two =objects[(total/2):]
    return {'col_one':col_one,'col_two':col_two}





