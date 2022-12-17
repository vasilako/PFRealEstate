from django import forms
from django.forms import inlineformset_factory

from PFRealEstate.property_app.models import Property_mod, Images_mod


class PropertyCreateOrUpdateForm(forms.ModelForm):
    class Meta:
        model = Property_mod
        exclude = ('user_agent',)

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title of the property'}),
        }


class ImagesCreateForm(forms.ModelForm):

    class Meta:
        model = Images_mod
        fields = '__all__'
