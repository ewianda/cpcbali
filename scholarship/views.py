from django.shortcuts import render
from scholarship.forms import ScholarshipForm
from django.views.generic.edit import CreateView
from scholarship.models import Scholarship

from django.http import HttpResponseRedirect


class ScholarshipCreateView(CreateView):
    template_name = 'scholarship/scholarship.html'
    model = Scholarship
    success_url = '/'
    form_class =ScholarshipForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ScholarshipCreateView, self).form_valid(form)
