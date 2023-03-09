from django import forms


class CartAddForm(forms.Form):
    Quantity = forms.IntegerField(min_value=1,max_value=9)
    