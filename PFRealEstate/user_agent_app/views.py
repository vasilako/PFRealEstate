from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic as generic_views
from django.contrib.auth import views as auth_views


class SignUpView(generic_views.CreateView):
    form_class = auth_forms.UserCreationForm
    template_name = 'user_ageng/signUp.html'

class SignInView(auth_views.LoginView):
    template_name = 'user_ageng/signIn.html'

class SignInView(auth_views.LogoutView):
    next_page = reverse_lazy('index')

