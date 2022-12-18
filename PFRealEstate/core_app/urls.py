from django.urls import path

from PFRealEstate.core_app.views import indexView, RegisterView

urlpatterns = [
    path('', indexView.as_view(), name = 'index page'),
    path('register/', RegisterView.as_view(), name = 'register page'),


]

