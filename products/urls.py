from django.urls import path, re_path
from . import views

app_name = 'products'
urlpatterns = [
    path('',views.ProductList.as_view(),name='products'),
    re_path(r'(?P<slug>[^/]+)/?$',views.ProductDetail.as_view(),name='detail'),
    path('delete-comment/<int:comment_id>/',views.DeleteUserComment.as_view(),name='delete-comment'),
]
