from django.urls import path

from . import views

app_name = 'users'


urlpatterns = [
    path('', views.login_view, name='login'),
    path('restricted-content/', views.restricted_content, name='restricted_content'),
    path('logout/', views.logout_view, name='logout'),
    path('token/', views.get_token, name='token'),
    path('protected/', views.protected_endpoint, name='protected')

]
