from django.urls import path
from . import views
 
urlpatterns = [
  path('add-to-cart/', views.addToCart,name="add-to-cart"),
  path('', views.cart, name="cart"),
  path('checkout/', views.checkout,name="checkout"),
]