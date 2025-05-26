from django.contrib import admin
from .models import Dog, Breed, Parent


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'breed', 'born_date')
    list_filter = ('breed',)
    search_fields = ('name',)


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'breed', 'year_born')
