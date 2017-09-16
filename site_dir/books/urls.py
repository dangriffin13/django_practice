#books/urls.py

from django.conf.urls import include, url
from books import views

urlpatterns = [
	url(r'^search_form/$', views.search_form)
]