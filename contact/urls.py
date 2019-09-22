from django.conf.urls import url, include
from django.contrib import admin
from .views import contactview

urlpatterns = [
    url(r'^$', contactview, name='contact'),
]
