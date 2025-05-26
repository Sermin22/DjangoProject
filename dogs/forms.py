from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from django.utils import timezone
from dogs.models import Dog, Parent


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class DogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Dog
        exclude = ("views_count",)


class ParentForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"

    def clean_year_born(self):
        year_born = self.cleaned_data.get('year_born')
        current_year = timezone.now().year
        time_delta = current_year - year_born
        if time_delta >= 30:
            raise ValidationError('Собак-родитель не может быть старше более чем на 30 лет')
        return year_born

