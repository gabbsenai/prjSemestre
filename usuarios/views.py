from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, TemplateView
from django.contrib.auth.models import User
from usuarios.forms import EditProfileForm

class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  

class LogoutView(LogoutView):
    next_page = reverse_lazy('login') 

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user