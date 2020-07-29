from django import forms
from .models import Account,Article

class ItemForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'