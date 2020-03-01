from django import forms
from .models import ProductModel

class ProductForm(forms.ModelForm):
    No = forms.IntegerField(min_value=101)
    class Meta:
        model = ProductModel
        fields = '__all__'

    def clean_Price(self):
        Price = self.cleaned_data['Price']
        if Price >= 1000:
            return Price
        else:
            raise forms.ValidationError('Price Minimum of Rs:1000/- are allowed...!!')