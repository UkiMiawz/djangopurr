from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'TestingIdea.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
                       url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
                       )
