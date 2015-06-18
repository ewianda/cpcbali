from django.shortcuts import render
from history.models import  History,Principal
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone

# Create your views here.
class HistoryDetailView(DetailView):
      model = History
      def get_context_data(self, **kwargs):
        context = super(HistoryDetailView, self).get_context_data(**kwargs)
        context['history_list'] = History.objects.all()
        return context
    
    
class PrincipalListView(ListView):
     model = Principal 
     def get_context_data(self, **kwargs):
        context = super(PrincipalListView, self).get_context_data(**kwargs)
        context['history_list'] = History.objects.all()
        return context 