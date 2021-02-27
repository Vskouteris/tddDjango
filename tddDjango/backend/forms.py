from django import forms
from django.forms import ModelForm

from .models import *

class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = "__all__"

class ParameterForm(forms.ModelForm):
    class Meta:
        model = Parameter
        fields = "__all__"

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = "__all__"