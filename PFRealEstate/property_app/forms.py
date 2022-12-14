from django import forms

from PFRealEstate.property_app.models import Property_mod, Images_mod


class PropertyCreateOrUpdateForm(forms.ModelForm):

    class Meta:
        model = Property_mod
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title of the property'}),
            'price': forms.TextInput(attrs={'placeholder': 'Enter price of the property'}),
        }


class ImagesCreateForm(forms.ModelForm):

    class Meta:
        model = Images_mod
        fields = '__all__'
