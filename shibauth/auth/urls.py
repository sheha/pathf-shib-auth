
from django.conf.urls import url
from . import views

# adding a URL called /home
urlpatterns = [url(r'^$', views.home, name='home'), ]
