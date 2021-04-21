from django.urls import path
from .views import Index, Register, Login, Logout
urlpatterns = [
    path('', Index, name="index"),
    path('register', Register, name="register"),
    path('login', Login, name="login"),
    path('logout', Logout, name="logout")
]