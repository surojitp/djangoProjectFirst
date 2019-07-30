from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
class RowProductForm(forms.Form):
    title = forms.CharField(
                            label='',
                            widget=forms.TextInput(attrs={
                                "placeholder": "Title",
                                "class": "one two"
                                })
                        )
    description = forms.CharField(
                            required=False,
                            widget=forms.Textarea(attrs={
                                "placeholder": "Your description",
                                "id": "some-id",
                                "rows":20,
                                "cols": 30
                            })
                        )
    price = forms.DecimalField(initial=99.99)