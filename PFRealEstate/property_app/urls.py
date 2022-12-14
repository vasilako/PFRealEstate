from django.urls import path

from PFRealEstate.property_app.views import PropertyDetailView, NewPropertyCreateView, PropertyListlView, \
    PropertyDeletelView, PropertyUpdateView

urlpatterns = [
    path('list-properties/', PropertyListlView.as_view(), name ='list property'),
    path('create/', NewPropertyCreateView.as_view(), name = 'create property'),
    path('details/<slug:slug>', PropertyDetailView.as_view(), name = 'detail property'),
    path('update/<slug:slug>', PropertyUpdateView.as_view(), name = 'update property'),
    path('delete/<slug:slug>', PropertyDeletelView.as_view(), name = 'delete property'),

]