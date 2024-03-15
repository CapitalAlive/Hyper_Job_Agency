from django import forms


class NewEntry(forms.Form):
    description = forms.CharField(
        label="Enter the description here:"
    )
