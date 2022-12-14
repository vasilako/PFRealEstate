from django.forms import inlineformset_factory

from PFRealEstate.property_app.forms import ImagesCreateForm
from PFRealEstate.property_app.models import Property_mod, Images_mod


'''
This FormSet is for Images_mod to Property_mod,
because in the Images_mod model,
the field "to_property" is Foreign Key
'''
ImageFormSet = inlineformset_factory(
        parent_model=Property_mod,
        model=Images_mod,
        form=ImagesCreateForm,
        extra=1,
        can_delete=True,
        can_delete_extra=True,
    )




# class PropertyInline():
#     '''
#     Esta clase es base para las clases create y update.
#     '''
#     model = Property_mod
#     form_class = PropertyCreateOrUpdateForm
#     template_name = 'propeties/propety_create_or_update.html'
#
#     def form_valid(self, form):
#         '''
#         Para validar el formulario primero se le pasa el FormSet
#         get_named_formsets(): devuelve todos los FormSet,
#         despues la all(), comprueba si todos los campos son validos y guarda la formma si es asi,
#         en caso contrario devuelve la forma
#         '''
#         named_formsets = self.get_named_formsets()
#         if not all((x.is_valid() for x in named_formsets.values())):
#             return self.render_to_response(self.get_context_data(form=form))
#         self.object = form.save()
#
#         # for every formset, attempt to find a specific formset save function
#         # otherwise, just save.
#         for name, formset in named_formsets.items():
#             formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
#             if formset_save_func is not None:
#                 formset_save_func(formset)
#             else:
#                 formset.save()
#         return redirect('index page')
#
#     def formset_images_valid(self, formset):
#         """
#         Hook for custom formset saving. Useful if you have multiple formsets
#         """
#         images = formset.save(commit=False)  # self.save_formset(formset, contact)
#         # add this 2 lines, if you have can_delete=True parameter
#         # set in inlineformset_factory func
#         for obj in formset.deleted_objects:
#             obj.delete()
#         for filename in images:
#             filename.to_property = self.object  # TODO ojo con esto filename and to_property
#             filename.save()
#
#
# class PropertyCreateView(PropertyInline, generic_views.CreateView):
#     def get_context_data(self, **kwargs):
#         ctx = super(PropertyCreateView, self).get_context_data(**kwargs)
#         ctx['named_formsets'] = self.get_named_formsets()
#         return ctx
#
#     def get_named_formsets(self):
#         if self.request.method == "GET":
#             return {
#                 'images': ImageFormSet(prefix='images'),
#             }
#         else:
#             return {
#                 'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, prefix='images'),
#             }
#

'''
---------------------------------------------------------

    template_name = 'propeties/propety_create.html'
    model = Property_mod
    form_class = PropertyCreateOrUpdateForm

    image_inlines = ImageFormSet

    # fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('index page')

    # def get_success_url(self):
    #     return reverse_lazy(
    #         'detail property',
    #         kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        ctx = self.get_context_data()
        self.image_inlines = ctx['inlines']
        print(f'el contexto {ctx}')
        print(f'inlines contenido {self.image_inlines}')
        if form.is_valid():
            print(form.cleaned_data)
        if self.image_inlines.is_valid():
            print(self.image_inlines.cleaned_data)
            print('-------------')
            print(self.image_inlines.data)
        else:
            print(self.image_inlines.cleaned_data)
            print(self.image_inlines.data)
        # if inlines.is_valid() and form.is_valid():
        #     self.object = form.save()
        #     return redirect(self.get_success_url())
        #TODO aqui falla la vilidadcion del formulario las imagenes no entran en cleand_data

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form))


    def get_context_data(self, **kwargs):
        ctx = super(PropertyCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = PropertyCreateOrUpdateForm(self.request.POST)
            ctx['inlines'] = self.image_inlines(self.request.POST, self.request.FILES)
        else:
            ctx['form'] = PropertyCreateOrUpdateForm()
            ctx['inlines'] = self.image_inlines()
        return ctx


---------------------------------------------------------
'''