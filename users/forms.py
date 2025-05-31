from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import BooleanField
from .models import CustomUser


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class CustomUserCreationForm(StyleFormMixin, UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        help_text='Необязательное поле. Введите ваш номер телефона',

    )
    username = forms.CharField(
        max_length=50,
        required=True,
    )
    usable_password = None

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'phone_number', 'avatar', 'password1', 'password2',]
        # fields = '__all__'  # так в конспекте и получше наверное, сразу все поля

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['phone_number'].label = 'Телефон'
        self.fields['avatar'].label = 'Аватар'

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять только из цифр')
        return phone_number
