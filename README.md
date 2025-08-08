## Для запуска проекта на локальной машине через команду
python manage.py runserver 
необходимо:

1. в файле .env:

DATABASE_HOST=localhost
LOCATION=redis://127.0.0.1:6379/1

2. запустить сервис Redis налокальной машине



## Проект завернут в Docker и настроен на развертку на виртуальной машине 
## yandex.cloud


для запуска проекта необходимо:

1. в файле .env:
2. 
DATABASE_HOST=db
LOCATION=redis://redis:6379/1

3. Открыть виртуальную машину по ссылке:
```
https://console.yandex.cloud/folders/b1g3ehj5rm0r5s1p6oac/compute/instance/fv4470m2hiupbd6tnfja/overview
```
4. скопировать там <ssh -l sm-admin 130.193.45.14>
5. открыть командную строку
6. ввести команду <ssh -l sm-admin 130.193.45.14>, это обеспечит вход в ВМ.
8. перейти на проект командой
```
cd DjangoProject
```
9. создать файл .env на ВМ
выполнить команду
```
nano .env
```
скопировать настройки из файла .env в это файл на ВМ

посмтреть файл на ВМ можно командой
```
cat .env
```
10. Примените миграции в контейнере:
```
sudo docker-compose exec web python manage.py migrate
```

11. выполнить команду запустить проект
```
sudo docker-compose up -d
```

Завершить работу
```
sudo docker-compose down
```