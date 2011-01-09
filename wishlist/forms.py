from django import forms
from wishlist.models import Item

class AddItem(forms.ModelForm):
    """
    A model form for adding an Item
    """
    class Meta:
        model = Item

class DeleteItem(forms.Form):
    """
    A form for deleting an item.
    """
    confirm = forms.CharField(widget=forms.HiddenInput, initial=True)
