from django.urls import path
from . import views
 
urlpatterns = [
  path('', views.home,name="home"),
  path('search', views.search,name="search"),
  path('category-list/',views.category_list,name="category-list"),
  path('brand-list/',views.brand_list, name="brand-list"),
  path('product-list/',views.product_list, name="product-list"),
  path('category-product-list/<int:state_Id>',views.category_product_list, name="category-product-list"),
  path('product-detail/<int:item_Id>', views.product_detail, name="product-detail"),
]




