
from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^articles/all/$', views.articles),
    url(r'^articles/get/(?P<article_id>\d+)/$', views.article), #?P<...>\d+ it`s number var
    url(r'^articles/addlike/(?P<article_id>\d+)/(?P<page_number>\d+)/$', views.addlike),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment),
    url(r'^page/(\d+)/$', views.articles),
    url(r'^', views.articles),
]
