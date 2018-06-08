from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Не правельный логин или пароль")

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label="Имя полльзователя", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Почта-Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    email2 = forms.EmailField(label='Повтор Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Еще раз пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            'password2'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        username = self.cleaned_data.get('username')
        if email != email2:
            raise forms.ValidationError("E-mail не совпадает")
        email_as = User.objects.filter(email=email)
        if email_as.exists():
            raise forms.ValidationError("Данный E-mail уже используется")

        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Пароль не совпадает")
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("Данное имя пользователя используется, выберите другую")
        return super(UserRegisterForm, self).clean(*args, **kwargs)

