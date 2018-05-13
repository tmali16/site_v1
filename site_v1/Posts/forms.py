from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from Posts.models import *


class pForm(forms.ModelForm):
    name = forms.CharField(required=False, label='Имя',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control form-control-sm inline', 'placeholder': 'Имя'}))
    phone = forms.CharField(required=False, label='Номер телефона',
                            widget=forms.TextInput(
                                attrs={'class': 'form-control form-control-sm', 'placeholder': 'Номер телефона'}))
    age = forms.CharField(required=False, label='Возраст', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Возраст'}))
    height = forms.CharField(required=False, label='Рост', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Рост'}))
    weight = forms.CharField(required=False, label='Вес', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Вес'}))
    boob = forms.CharField(required=False, label='Грудь', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'placeholder': 'Грудь'}))
    note = forms.CharField(required=False, label='описание',
                           widget=forms.Textarea(
                               attrs={'class': 'form-control form-control-sm', 'rows': '4', 'placeholder': 'описание'}))
    eye = forms.ModelChoiceField(queryset=eyes.objects.all(), required=False, label='глаза',
                                 widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    types = forms.ModelChoiceField(queryset=types.objects.all(), required=False, label='Тип',
                                   widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    hair = forms.ModelChoiceField(queryset=haire.objects.all(), required=False, label='Волосы',
                                  widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    image_1 = forms.ImageField(required=True, label='Фото 1')
    image_2 = forms.ImageField(required=False, label='Фото 2')
    image_3 = forms.ImageField(required=False, label='Фото 3')
    image_4 = forms.ImageField(required=False, label='Фото 4')
    image_5 = forms.ImageField(required=False, label='Фото 5')

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(pForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = [
            'name',
            'phone',
            'age',
            'height',
            'weight',
            'boob',
            'note',
            'eye',
            'types',
            'hair',
            'image_1',
            'image_2',
            'image_3',
            'image_4',
            'image_5'
        ]


