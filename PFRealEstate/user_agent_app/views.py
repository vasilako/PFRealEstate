from django.contrib.auth import views as auth_views, get_user_model, login, authenticate
from django.http import HttpRequest

from django.urls import reverse_lazy
from django.views import generic as generic_views

from PFRealEstate.property_app.models import Property_mod
from PFRealEstate.user_agent_app.forms import CustomUserForms

UserModel = get_user_model()

class SignUpCreateView(generic_views.CreateView):
    template_name = 'user_ageng/signUp.html'
    model = UserModel
    form_class = CustomUserForms
    success_url = reverse_lazy('index page')

    def form_valid(self, form):
        valid = super(SignUpCreateView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

class SignInView(auth_views.LoginView):
    template_name = 'user_ageng/signIn.html'

    def get_context_data(self, **kwargs):
        '''
            In order to redirect the hidden field that is sent by the form in the signIn.html.
            Here I must override the get_conxt_data method by returning
            the value captured by self.request.GET.get('next', '/') to the content.
        '''
        context = super(SignInView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index page')


class UserDetailsView(generic_views.DetailView):
    template_name = 'user_ageng/user_details.html'
    model = UserModel
    context_object_name = 'user_detail'

    def get_context_data(self, **kwargs):
        context_object_name = super(UserDetailsView, self).get_context_data(**kwargs)
        context_object_name['user_properties'] = Property_mod.objects.filter(user_agent=self.object.id)
        return context_object_name


class UserEditView(generic_views.UpdateView):
    template_name = 'user_ageng/user_edit.html'
    model = UserModel
    fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'phone_number',
        'profile_image',
    )

    def dispatch(self, request, *args, **kwargs):
        # if the user to update is the same as the user logged in => continue
        return super().dispatch(request, *args, **kwargs)

        # else, 401 authorized

    def get_success_url(self):
        return reverse_lazy(
            'user details',
            kwargs={'pk':self.object.pk}
        )


class UserDeleteView(generic_views.DeleteView):
    template_name = 'user_ageng/user_delete.html'
    model = UserModel
    success_url = reverse_lazy('index page')





