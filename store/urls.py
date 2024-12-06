from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from store.views import home, product

urlpatterns = [
    path('', home, name = 'name'),
    path('products/<slug>/',product,name='products'),
]