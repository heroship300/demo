from django.urls import path
from . import views

# Tạo đường dẫn để hiển thị ở views

urlpatterns = [
    path("register",views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout", views.logout, name="logout"),
    ]