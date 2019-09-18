from django.conf.urls import url, include
from .views import all_extras

urlpatterns = [
    url(r'^$', all_extras, name='extras'),
]