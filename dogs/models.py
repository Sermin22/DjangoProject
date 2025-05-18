from django.db import models
from django.db.models import TextField, SET_NULL


class Breed(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название породы", help_text="Введите название породы"
    )
    description = TextField(
        verbose_name="Описание породы",
        help_text="Укажите описание породы",
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Dog(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Кличка собаки", help_text="Введите кличку собаки"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=SET_NULL,
        verbose_name="Порода собаки",
        help_text="Введите породу собаки",
        blank=True,
        null=True,
        related_name='dogs'
    )
    photo = models.ImageField(
        upload_to="dogs/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="загрузите фото собаки",
    )
    born_date = models.CharField(
        blank=True,
        null=True,
        verbose_name="Дата рождения",
        help_text="Введите дату рождения",
   )
    views_count = models.PositiveIntegerField(
        verbose_name="Всего просмотров",
        default=0,
    )

    def __str__(self):
        return f"{self.name} {self.breed}"

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ["breed", "name"]
