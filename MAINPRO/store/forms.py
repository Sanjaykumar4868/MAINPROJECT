from django import forms

from . models import Product, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name','address','zipcode','city')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title','description','price','image','image1','image2','image3','image4',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'p-2 border border-gray-200'
            }),
            'title': forms.TextInput(attrs={
                'class': 'p-2 border border-gray-200'
            }),
             'description': forms.Textarea(attrs={
                'class': 'p-4 border border-gray-200'
            }),
             'price': forms.TextInput(attrs={
                'class': 'p-2 border border-gray-200'
            }),
             'image': forms.FileInput(attrs={
                'class': 'p-3 border border-gray-200'
            }),
            'image1': forms.FileInput(attrs={
                'class': 'p-3 border border-gray-200'
            }),
            'image2': forms.FileInput(attrs={
                'class': 'p-3 border border-gray-200'
            }),
             'image3': forms.FileInput(attrs={
                'class': 'p-3 border border-gray-200'
            }),
             'image4': forms.FileInput(attrs={
                'class': 'p-3 border border-gray-200'
            }),

        }
