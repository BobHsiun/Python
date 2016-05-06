from django.conf.urls import url
from . import views


app_name = 'learn'
urlpatterns = [
    url(r'^$', views.home(), name='homepage'),
]