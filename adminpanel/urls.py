from django.urls import path
from . import views

app_name = 'adminpanel'
urlpatterns = [
    path('',views.AdminView.as_view(),name='adminpanel'),
    path('add-product/',views.AddProductView.as_view(),name='add-product'),
    path('update-product/<int:pk>',views.EditProdcut.as_view(),name='update-product'),
    path('delete-product/<int:prod_id>',views.DeleteProduct.as_view(),name='delete-product'),
    path('add-article/',views.AddArticle.as_view(),name='add-article'),
    path('update-article/<int:pk>',views.EditArticle.as_view(),name='update-article'),
    path('delete-article/<int:arti_id>',views.DeleteArticle.as_view(),name='delete-article'),
    path('delete-discount/<int:dis_id>',views.DeleteDiscount.as_view(),name='delete-discount'),
    path('orders/',views.AdminOrders.as_view(),name='orders'),
    path('orders/<int:order_id>',views.AdminOrderDetail.as_view(),name='order-detail'),
    path('delete-comment/<int:comment_id>',views.DeleteUserComment.as_view(),name='delete-comment'),
    path('comments/',views.CommentsAdminView.as_view(),name='comments'),
]