from django.conf.urls import include, url, re_path  # noqa
from django.urls import path
from django.shortcuts import redirect
from django.views.generic import TemplateView
from users import views

app_name = 'users'

urlpatterns = [       
    path("login/", views.login, name='login'),
    path('logout/', TemplateView.as_view(template_name='index.html'), name='logout'), 
    path('user/', views.SocialUserViewSet.as_view({'get': 'retrieve'}), name='get_user'),
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')), 
]
