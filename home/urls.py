from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from home import views

urlpatterns = patterns('',

url(r'^$', views.home,name="home"),
url(r'^robots\.txt$' , TemplateView.as_view(template_name="robot.html", content_type='text/plain')),
url(r'^anthems/$', TemplateView.as_view(template_name="home/anthem.html"),name="anthem"),
url(r'^thank-you-for-your-contributions/$', TemplateView.as_view(template_name="home/thank_you.html"),name="thanks"),

#url(r'^scholarships$', TemplateView.as_view(template_name="home/scholarship.html"),name="scholarship"),
url(r'^boban-world-wide/$', TemplateView.as_view(template_name="home/boban_world_wide.html"),name="boban-world-wide"),
url(r'^where-they-are/$', views.AchievementListView.as_view(template_name="home/where_they_are.html"),name="where-they-are"),

url(r'^batch/(?P<class_of>[\w-]+)/$', views.batch_view,name="batch"),

     
url(r'^contact$', views.contact_form,name="contact"),
)

