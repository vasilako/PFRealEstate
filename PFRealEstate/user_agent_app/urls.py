from django.contrib.auth.decorators import login_required
from django.urls import path, include

from PFRealEstate.user_agent_app.views import SignInView, SignOutView, SignUpCreateView, UserDeleteView, UserDetailsView, UserEditView

urlpatterns = [
    path('signin/', SignInView.as_view(), name = 'sign in'),
    path('signup/', SignUpCreateView.as_view(), name ='sign up'),
    path('signout/', SignOutView.as_view(), name='sign out'),

    path('id/<int:pk>/', include([
        path('details/', login_required(UserDetailsView.as_view()), name='user details'),
        path('edit/', login_required(UserEditView.as_view()), name = 'user edit'),
        path('delete/', login_required(UserDeleteView.as_view()), name = 'user delete'),
        ]))
    ]
