from django.urls import path

from PFRealEstate.core_app.views import indexView

urlpatterns = [
    path('', indexView.as_view(), name = 'index page'),

]