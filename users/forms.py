from django import forms
from django.core.exceptions import ValidationError

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': ''
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': ''
        })
    )


class SignupForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        error_messages={
            'required': 'Field cannot be empty'
        },
        help_text=('Min. 4 Caracteres. Não deve contar espaços'),
        widget=forms.TextInput(
            attrs={'placeholder': ''}
        ),
        label=("Username")
    )
    password = forms.CharField(
        required=True,
        error_messages={
            'required': 'Field cannot be empty'
        },
        help_text=(
            'Digite uma senha forte, contendo 8 cacteres, números, caracteres maiúsculos e minúsculos.'  # noqa
        ),
        label=('Password'),
        widget=forms.PasswordInput(
            attrs={'placeholder': ''}
        ),
    )
    password2 = forms.CharField(
        required=True,
        error_messages={
            'required': 'Field cannot be empty'
        },
        help_text=(
            'Digite uma senha forte, contendo 8 cacteres, números, caracteres maiúsculos e minúsculos.'  # noqa
        ),
        label=('Repeat Passowrd'),
        widget=forms.PasswordInput(
            attrs={'placeholder': ''}
        ),
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username',
            'email', 'password', 'password2'
        ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': ''}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': ''}
            ),
            'username': forms.TextInput(
                attrs={'placeholder': ''}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': ''}
            ),
        }
        error_messages = {
            'email': {
                'required': 'Este campo não pode estar vazio',
                'invalid': 'Digite um email válido'
            }
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

        def clean_email(self):
            email = self.cleaned_data['email']
            exists = User.objects.filter(email=email).exists()

            if exists:
                raise forms.ValidationError(
                    'Este email já existe', code='invalid',
                )

            return email

        def clean_username(self):
            username = self.cleaned_data['username']
            exists = User.objects.filter(email=username).exists()

            if exists:
                raise forms.ValidationError(
                    'Este usuário já existe', code='invalid',
                )

            return username

        def clean(self):
            cleaned_data = super().clean()

            password = cleaned_data['password']
            password2 = cleaned_data['password2']

            if password != password2:
                password_confirmation_error = ValidationError(
                    'Password and password2 must be equal',
                    code='invalid'
                )
                raise ValidationError({
                    'password': password_confirmation_error,
                    'password2': [
                        password_confirmation_error,
                    ],
                })
