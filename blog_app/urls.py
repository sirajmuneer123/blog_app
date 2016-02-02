from django.conf.urls import patterns, url
from blog_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^read_more/(?P<blog_title_slug>[\w\-]+)/$', views.read_more, name='read_more'),
        url(r'^add_blog/$', views.add_blog, name='add_blog'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^delete_post/(?P<id>\d+)/$', views.delete_post, name='delete_new'),
        url(r'^blog_edit/(?P<blog_title_slug>[\w\-]+)/$', views.blog_edit, name='blog_edit'),

        )