from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('restricted-content/', views.restricted_content, name='restricted_content'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]
