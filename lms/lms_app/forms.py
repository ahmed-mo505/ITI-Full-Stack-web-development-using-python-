# from django import forms
# from .models import *

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#         }


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = [
#             'title',
#             'author',
#             'cover_image',
#             'author_image',
#             'pages',
#             'price',
#             'rent_price',
#             'rent_period',
#             'total_rent',
#             'state',
#             'category',
#         ]
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.TextInput(attrs={'class': 'form-control'}),
#             'cover_image' : forms.FileInput(attrs={'class': 'form-control'}),
#             'author_image': forms.FileInput(attrs={'class': 'form-control'}),
#             'pages': forms.NumberInput(attrs={'class': 'form-control'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control'}),
#             'rent_price': forms.NumberInput(attrs={'class': 'form-form-control', id:'rentalprice'}),
#             'rent_period': forms.NumberInput(attrs={'class': 'form-form-control',id:'rentaldays'}),
#             'total_rent': forms.NumberInput(attrs={'class': 'form-control',id:'totalrental'}),
#             'state': forms.Select(attrs={'class': 'form-form-control'}),
#             'category': forms.Select(attrs={'class': 'form-form-control'}),
#         }


from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'cover_image',
            'author_image',
            'pages',
            'price',
            'rent_price',
            'rent_period',
            'total_rent',
            'state',
            'category',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'author_image': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rent_price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rentalprice'}),
            'rent_period': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rentaldays'}),
            'total_rent': forms.NumberInput(attrs={'class': 'form-control', 'id': 'totalrental'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
