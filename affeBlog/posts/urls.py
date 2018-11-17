from django.contrib import admin
from django.urls import  path

from posts import views
urlpatterns = [
    path('create/', views.post_create),
    path('detail/', views.post_detail),
    path('list/', views.post_list),
    path('update/', views.post_update),
    path('delete/', views.post_delete),
    ## path(r'^create$', views.post_home),
]
