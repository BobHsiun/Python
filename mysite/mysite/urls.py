"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views  # new
from addview import views as add_test
from vartest import views as test_var


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^111$', learn_views.index),  # new
    url(r'^add/$', add_test.index,name='index'),  # add
    url(r'^add/(\d+)/(\d+)/$', add_test.add,name='add'),  # add
    url(r'^$', learn_views.home,name='home'),  # home
    url(r'^home$', test_var.home2,name='home2'),  # home
    url(r'^forms$', 'tools.views.index', name='home'),
]
