from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('<int:user_id>/',views.CartView.as_view(),name='cart'),
    path('add-to-cart/<int:prod_id>',views.AddToCart.as_view(),name='add_to_cart'),
    path('delete-item/<int:prod_id>/',views.RemoveItem.as_view(),name='delete_item_cart'),
]
