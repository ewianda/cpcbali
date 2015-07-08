from models import *
from dbindexer.lookups import StandardLookup
from dbindexer.api import register_index

register_index(Boban, {'email': 'iexact',
                         'last_name':  'icontains',
                           })
