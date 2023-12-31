from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
	# Login page.
    path('',
    	auth_views.LoginView.as_view(template_name='users/login.html'),
    	name='login'),
    # path('login/',
    # 	auth_views.LoginView.as_view(template_name='users/login.html'),
    # 	name='login'),
    path('logout', views.logout_views, name="logout"),
    path('register/', views.register, name='register')
]