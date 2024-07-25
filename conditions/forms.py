from django import forms
from .models import Locations

class InputLocation(forms.ModelForm):

    class Meta:
        model = Locations
        fields = '__all__'