from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("category/", csrf_exempt(CategoryView.as_view()), name="category"),
    path("product/", csrf_exempt(ProductView.as_view()), name="product"),
]
