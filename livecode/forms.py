from django import forms

from .models import Shop

class InputShop(forms.ModelForm):

    class Meta:
        model = Shop
        fields = ('item', 'photo','harga','deskripsi',)

