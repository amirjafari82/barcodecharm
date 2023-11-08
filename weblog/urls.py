from django.urls import path, re_path
from . import views

app_name = 'weblog'
urlpatterns = [
    path('',views.WeblogView.as_view(),name='weblog'),
    re_path(r'(?P<slug>[^/]+)/?$',views.ArticleView.as_view(),name='article'),
]