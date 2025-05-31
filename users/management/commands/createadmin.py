from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email='admin@minins.ru',
            first_name='Ser',
            last_name='Min'
        )
        user.set_password('123abc456dfj')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Успешно созданный пользователь-администратор с '
                                             f'электронной почтой {user.email}'))

# создал суперпользователя с помощью кастомной команды:
# python manage.py createadmin
