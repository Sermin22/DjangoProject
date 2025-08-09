from django import forms
from .models import Author, Book
from django.core.exceptions import ValidationError


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите фамилию'
        })
        self.fields['birth_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите дату рождения в формате "2025-12-31"'
        })

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name').lower()  # Приводим имя к нижнему регистру
        last_name = cleaned_data.get('last_name').lower()   # Приводим фамилию к нижнему регистру

        if Author.objects.filter(first_name__iexact=first_name, last_name__iexact=last_name).exists():
            # Метод __iexact является специальным синтаксисом Django ORM, позволяющим проводить
            # сравнение строковых значений без учета регистра символов
            # exists() — это метод для проверки существования какого-то ресурса, файла, директории
            # или другого объекта.
            raise ValidationError('Автор с таким именем и фамилией уже существует.')
            # raise forms.ValidationError('Автор с таким именем и фамилией уже существует.')  # Якобы так лучше,
            # следовало из вопросов к уроку
        return cleaned_data


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название книги'
        })
        self.fields['publication_date'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите дату публикации в формате "2025-12-31'
        })
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['author'].label = 'Автор'

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title').lower()  # Приводим имя к нижнему регистру

        if Book.objects.filter(title__iexact=title).exists():
            # Метод __iexact является специальным синтаксисом Django ORM, позволяющим проводить
            # сравнение строковых значений без учета регистра символов
            # exists() — это метод для проверки существования какого-то ресурса, файла, директории
            # или другого объекта.
            #
            # raise ValidationError('Книга с таким названием уже существует.')
            raise forms.ValidationError('Книга с таким названием уже существует.')  # Якобы так лучше,
            # следовало из вопросов к уроку
        return cleaned_data
