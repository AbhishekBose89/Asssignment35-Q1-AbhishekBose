from django.urls import path
from .views import MyCartView, SearchView, CartView, SearchViewId, CheckoutView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("cart/products/", MyCartView.as_view(), name="show_all_products'"),
    path(
        "cart/products/<int:product_id>/search/",
        SearchViewId.as_view(),
        name="search_product_by_id",
    ),
    path(
        "cart/products/search/",
        SearchView.as_view(),
        name="search_product_by_name",
    ),
    path("cart/product/add/", csrf_exempt(CartView.as_view()), name="add_to_cart"),
    path(
        "cart/products/<int:product_id>/delete",
        csrf_exempt(CheckoutView.as_view()),
        name="delete_product",
    ),
]
