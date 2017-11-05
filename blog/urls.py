from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^greeting/$', views.greeting, name='greeting'),
    url(r'^greeting2/$', views.greeting2, name='greeting'),
    url(r'^greeting3/$', views.greeting3, name='greeting'),
    url(r'^post/edit/(?P<pk>\d+)/$', views.post_edit, name='post_edit'),
    url(r'^post/list/$', views.post_list, name='post_list'),
    url(r'^post/detail/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new')
]