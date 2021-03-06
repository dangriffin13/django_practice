"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import (hello, null, current_datetime, hours_ahead, ops_tool, meta, display_meta,
    contact)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', null),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^sparta/$', ops_tool),
    url(r'^meta/$', meta),
    url(r'^meta_table/$', display_meta),
    url(r'^contact/$', contact),
    url(r'^', include('books.urls')) #include books app
    
]
