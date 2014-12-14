from django.shortcuts import render
from users.models import Boban
from django.views.generic.list import ListView

class MemoireList(ListView):
    model = Boban
    template_name = "memoire/memoire.html"
    paginate_by = 25
    context_object_name = 'boban_list'
    
