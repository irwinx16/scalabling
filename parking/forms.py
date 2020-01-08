from django import forms

class AddressForm(forms.Form):
    add_field = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "123 N Main St"
        })
    )
