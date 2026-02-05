from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),
    path('healthyz/' , views.app_live, name='app_live'),
    path('readyz/' , views.app_ready, name='app_ready'),
]