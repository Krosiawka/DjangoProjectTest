
from django.conf.urls import url, include
import views

urlpatterns = [

    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
]
