from django.forms import ModelForm 
from django import forms
from .models import Contact ,Commentaire 


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = '__all__'


class PurchaseForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)        

