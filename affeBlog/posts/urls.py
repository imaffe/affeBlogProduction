from django.contrib import admin
from django.urls import  path

from posts import views


urlpatterns = [
    path(r'^$', views.post_list, name='list'),
    path(r'^create/$', views.post_create),
    path(r'^(?P<slug>[\w-]+)/$', views.PostDetailView.as_view(), name='detail'),
    path(r'^(?P<slug>[\w-]+)/edit/$', views.post_update, name='update'),
    path(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]