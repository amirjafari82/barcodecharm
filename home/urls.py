from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('aboutme/',views.AboutMe.as_view(),name='aboutme'),
]