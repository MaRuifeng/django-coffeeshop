from django import forms
from .models import Category, DrinkType, Size

class OrderForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select")
    drink_type = forms.ModelChoiceField(queryset=DrinkType.objects.none(), empty_label="Select")
    size = forms.ModelChoiceField(queryset=Size.objects.none(), empty_label="Select")
    quantity = forms.IntegerField(min_value = 1)


class FilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="All", required=False)
    size = forms.ModelChoiceField(queryset=Size.objects.all(), empty_label="All", required=False)
