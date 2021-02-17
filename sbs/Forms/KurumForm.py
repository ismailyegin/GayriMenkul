from django import forms
from django.forms import ModelForm

from sbs.models.Gkurum import Gkurum


class KurumForm(ModelForm):
    class Meta:
        model = Gkurum
        fields = ('name',)
        labels = {'name': 'Tanımı', }
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),

        }
