

# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
##from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

from forum.models import Topic


class TopicDetailView(DetailView):
    model =Topic
      
    
    
class TopicListView(ListView):
    model = Topic