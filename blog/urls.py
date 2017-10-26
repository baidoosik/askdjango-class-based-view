from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^greeting/$', views.greeting, name='greeting'),
    url(r'^greeting2/$', views.greeting2, name='greeting'),
    url(r'^greeting3/$', views.greeting3, name='greeting'),
]