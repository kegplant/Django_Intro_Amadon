from django.conf.urls import url
from . import views #this line is new! #imports views.py from current folder
urlpatterns=[
    url(r'^$', views.index),#this line has changed!,
    url(r'^buy$',views.buy),
    url(r'^checkout$',views.checkout),
    url(r'^clear$',views.clear),
]