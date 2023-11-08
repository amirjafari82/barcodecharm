from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('<int:user_id>/',views.OrderView.as_view(),name='order'),
    path('cancel-order/<int:order_id>/',views.CancelOrder.as_view(),name='cancel-order'),
    path('continue-order/<int:order_id>/',views.ContinueOrder.as_view(),name='continue-order'),
    path('<int:user_id>/verify/', views.verify , name='verify'),
]
