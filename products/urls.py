from django.urls import path
from products.views import product_details_view, product_create_view, product_delete_view, product_list

app_name = 'product'
urlpatterns = [
    
    path('list', product_list),
    path('<int:id>', product_details_view, name='product-details'),
    path('<int:id>/delete/', product_delete_view),
    path('create/', product_create_view)
]
