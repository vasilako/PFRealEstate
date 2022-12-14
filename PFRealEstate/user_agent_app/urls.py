from django.urls import path, include

from PFRealEstate.user_agent_app.views import SignInView, SignOutView, SignUpCreateView, UserDeleteView, UserDetailsView

urlpatterns = [
    path('signin/', SignInView.as_view(), name = 'sign in'),
    path('signout/', SignOutView.as_view(), name = 'sign out'),


    path('signup/', SignUpCreateView.as_view(), name ='sign up'),
    path('id/<int:pk>/', include([
        path('details/', UserDetailsView.as_view(), name='user details'),
        path('edit/', SignOutView.as_view(), name = 'user edit'),
        path('delete/', UserDeleteView.as_view(), name = 'user delete'),
        ]))
    ]
