from django import forms
from django.forms import inlineformset_factory

from PFRealEstate.property_app.models import Property_mod, Images_mod


class PropertyCreateOrUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropertyCreateOrUpdateForm, self).__init__(*args, **kwargs)

        self.fields['operation'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['owner'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Property_mod
        exclude = ('user_agent',)




class ImagesCreateForm(forms.ModelForm):


    class Meta:
        model = Images_mod
        fields = '__all__'
