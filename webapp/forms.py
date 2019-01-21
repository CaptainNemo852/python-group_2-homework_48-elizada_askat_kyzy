from django import forms
from webapp.models import Food, OrderFood

class OrderFoodForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        exclude = ['order']


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = []


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        exclude = []