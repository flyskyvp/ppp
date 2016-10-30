from django.conf.urls import patterns, url
from blog import views

 
urlpatterns = patterns('',
    # url(r'^$', views.login, name='login'),
    # url(r'^register/$',views.register,name = 'register'),
    # url(r'login/$', views.login, name='login'),
    # url(r'logout/$', views.logout, name='logout'),

    url(r'^$', views.index, name='index'),
)