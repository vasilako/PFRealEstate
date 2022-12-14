
from django.contrib.auth import views as auth_views, get_user_model, login, authenticate
from django.contrib.auth.decorators import login_required
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

    def get_success_url(self):
        return reverse_lazy('index page')

# TODO esto provoca error cuando lo activo dice  AttributeError: 'function' object has no attribute 'as_view'
# @login_required(login_url='user/signin/')
class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index page')

# @login_required
class UserDetailsView(generic_views.DetailView):
    template_name = 'user_ageng/user_details.html'
    model = UserModel
    context_object_name = 'user_detail'

    def get_context_data(self, **kwargs):
        context_object_name = super(UserDetailsView, self).get_context_data(**kwargs)
        context_object_name['user_properties'] = Property_mod.objects.filter(user_agent=self.object.id)
        return context_object_name

# @login_required
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

# @login_required
class UserDeleteView(generic_views.DeleteView):
    template_name = 'user_ageng/user_delete.html'
    model = UserModel
    success_url = reverse_lazy('index page')





