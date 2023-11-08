from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('send-code/',views.SendCode.as_view(),name='send-code'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogout.as_view(),name='logout'),
    path('profile/<int:user_id>',views.ProfileView.as_view(),name='profile'),
    path('change-password/<int:user_id>',views.ChangePassword.as_view(),name='change-password'),
    path('edit-profile/<int:user_id>',views.EditUserProfile.as_view(),name='edit-profile'),
    path('edit-order/<int:order_id>',views.EditOrder.as_view(),name='edit-order'),
    path('order-detail/<int:order_id>',views.SeeOrderDetail.as_view(),name='order-detail'),
]