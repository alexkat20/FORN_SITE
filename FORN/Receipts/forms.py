from .models import Receipt

from django import forms


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        exclude = ('pub_date',)
