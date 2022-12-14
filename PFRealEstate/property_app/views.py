from django.contrib.auth import get_user_model

from django.forms import inlineformset_factory
from django.http import request
from django.shortcuts import redirect, render
from django.utils.text import slugify
from django.views import generic as generic_views
from PFRealEstate.property_app.forms import PropertyCreateOrUpdateForm
from PFRealEstate.property_app.models import Property_mod, Images_mod

UserModel = get_user_model()

class NewPropertyCreateView(generic_views.CreateView):
    template_name = 'propeties/propety_create.html'
    model = Property_mod
    form_class = PropertyCreateOrUpdateForm

    ImageInlineFormset = inlineformset_factory(
    parent_model= Property_mod,
    model= Images_mod,
    fields=('filename',),
    can_delete=False,
    )

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=True)
            self.object.slug = slugify(f'id-{self.object.id}-{self.object.title}')
            self.object = form.save(commit=True)
        else:
            print(form.errors)

        current_property = Property_mod.objects.get(id=self.object.pk)
        print(current_property)
        formset = self.ImageInlineFormset(self.request.POST or None,
                                          self.request.FILES or None,
                                          instance=current_property)
        if formset.is_valid():
            self.object = formset.save()
        return redirect('detail property', current_property.slug)

    def form_invalid(self, form):
        formset = self.ImageInlineFormset(self.request.POST or None, self.request.FILES or None, self.object.pk)
        return render(request, 'propeties/propety_create.html', formset)


    def get_context_data(self, **kwargs):
        ctx = super(NewPropertyCreateView, self).get_context_data(**kwargs)
        ctx['formset'] = self.ImageInlineFormset
        return ctx

class PropertyListlView(generic_views.ListView):
    template_name = 'propeties/property_list.html'
    model = Property_mod
    context_object_name = 'property_list'
    paginate_by = 6


class PropertyDetailView(generic_views.DetailView):
    template_name = 'propeties/propety_details.html'
    model = Property_mod
    context_object_name = 'property_detail'

    def get_context_data(self, **kwargs):
        context_object_name = super(PropertyDetailView, self).get_context_data(**kwargs)
        context_object_name['images'] = Images_mod.objects.all().filter(to_property_id=self.object.id)
        return context_object_name


class PropertyUpdateView(generic_views.UpdateView):
    template_name = 'propeties/propety_update.html'
    model = Property_mod
    context_object_name = 'property_details'


class PropertyDeletelView(generic_views.DeleteView):
    model = Property_mod
    template_name = 'propeties/delete_property.html'
    success_url = '/property/list-properties/'






