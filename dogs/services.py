from django.core.cache import cache
from config.settings import CACHE_ENABLED
from dogs.models import Dog


def get_dogs_from_cache():
    '''Получает данные из кеша. Если кеш пуст, то получает данные из БД'''

    if not CACHE_ENABLED:
        return Dog.objects.all()
    key = "dogs_list"
    dogs = cache.get(key)
    if dogs is not None:
        return dogs
    dogs = Dog.objects.all()
    cache.set(key, dogs, 20)
    return dogs