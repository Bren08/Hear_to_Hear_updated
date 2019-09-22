from django.conf.urls import url
from .views import all_accessories

urlpatterns = [
    url(r'^$', all_accessories, name='accessories'),
]