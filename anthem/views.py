from anthem.models import Anthem
from django.views.generic.detail import DetailView
# Create your views here.
class AnthemDetailView(DetailView):
    model = Anthem
    