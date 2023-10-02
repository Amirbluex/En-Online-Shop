from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("detail", views.CartDetailView.as_view(), name="cart_detail"),
    path("add/<int:pk>", views.CartAddView.as_view(), name="cart_add"),
    path("remove/<str:id>", views.CartRemoveView.as_view(), name="cart_remove"),
    path("order/<int:pk>", views.OrderDetailView.as_view(), name="order_detail"),
    path("order/add", views.OrderCreationView.as_view(), name="order_creation"),
    path("applydiscount/<int:pk>", views.ApplyDiscountView.as_view(), name="apply_discount"),
]

