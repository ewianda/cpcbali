from django import template
from django import forms
register = template.Library()
import json

@register.filter
def select_options(boundfield):
    """Return True if this field is a ChoiceField (or subclass)."""
    options = []
    if isinstance(boundfield.field, forms.ChoiceField):
     dict_list =  dict(getattr(boundfield.field, "choices", dict([]))).items()
     for ke,val in dict_list:
          data = {}
          data['value'] = ke
          data['text'] = val
          options.append(data)
    return json.dumps(options)

