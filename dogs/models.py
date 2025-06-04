from django.db import models
from django.db.models import TextField, SET_NULL
from users.models import CustomUser


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
        on_delete=models.SET_NULL,
        verbose_name="Порода собаки",
        help_text="Введите породу собаки",
        blank=True,
        null=True,
        related_name='dogs'
    )
    description = TextField(
        verbose_name="Описание собаки",
        help_text="Укажите описание собаки",
        blank=True,
        null=True,
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
    owner = models.ForeignKey(
        CustomUser,
        verbose_name='Владелец',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.name} {self.breed}"

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ["breed", "name"]
        permissions = [
            ("can_edit_breed", "Can edit breed"),
            ("can_edit_description", "Can edit description"),
        ]


class Parent(models.Model):
    dog = models.ForeignKey(
        Dog,
        related_name="parents",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Собака",
    )
    name = models.CharField(
        max_length=100, verbose_name="Кличка собаки", help_text="Введите кличку собаки"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        verbose_name="Порода собаки",
        help_text="Введите породу собаки",
        blank=True,
        null=True,
        related_name='parent_dogs'
    )
    year_born = models.PositiveIntegerField(
        verbose_name="Год рождения",
        help_text="Укажите год рождения",
        default=0,
        blank=True,
        null=True,
    )
    def __str__(self):
        return f"{self.name} {self.breed}"

    class Meta:
        verbose_name = "Собака родитель"
        verbose_name_plural = "Собаки родители"
        ordering = ["breed", "name"]