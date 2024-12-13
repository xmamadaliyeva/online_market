from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from store.views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/<slug:slug>/', product, name='product_detail'),
    path('single/<int:pk>/', single, name='single'),
]
