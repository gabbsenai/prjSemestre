from django.urls import path
from .views import EditProfileView, LoginView, LogoutView, ProfileView
from setup import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/', ProfileView.as_view(), name='profile'),
    path('editarperfil/', EditProfileView.as_view(), name='edit_profile'),
]