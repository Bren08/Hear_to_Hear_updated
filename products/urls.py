from django.conf.urls import url, include
from .views import all_products
from .views import all_addons

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^addons', all_addons, name='addons'),
]