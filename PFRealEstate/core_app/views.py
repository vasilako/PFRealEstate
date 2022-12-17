from django.http import request
from django.shortcuts import render
from django.views import generic as generic_views

from PFRealEstate.property_app.models import Property_mod, Images_mod
from PFRealEstate.user_agent_app.models import UserAgent_mod


# Create your views here.

class indexView(generic_views.TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'My static title'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['properties'] = Property_mod.objects.all()
        context['images'] = Images_mod.objects.all()
        context['user'] = self.request.user

        return context


