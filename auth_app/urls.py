from django.urls import path 
from . import views

app_name = 'auth_app'


urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]