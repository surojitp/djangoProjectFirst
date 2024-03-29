from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
                            label='',
                            widget=forms.TextInput(attrs={
                                "placeholder": "Title",
                                "class": "one two"
                                })
                        )
    # email = forms.EmailField()
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
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')
    #     if not 'CFE' in 'title':
    #         raise forms.ValidationError('This is not a valid title')
    #     if not 'news' in 'title':
    #         raise forms.ValidationError('This is not a valid title')
    #     return title
    
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     if not email.endswith('edu'):
    #         raise forms.ValidationError('Not a valid email')
    #     return email

            

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