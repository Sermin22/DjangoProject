from django.shortcuts import render

# Create your views here.
# students/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def about(request):
    return render(request, 'students/about.html')


def contact(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'students/contact.html')


def student_list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students/student_list.html', context)


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {'student': student}
    return render(request, 'students/student_detail.html', context)


# def example_view(request):
#     return render(request, 'app/example.html')
#
#
# def show_data(request):
#     if request.method == 'GET':
#         return render(request, 'app/data.html')
#
#
# def submit_data(request):
#     if request.method == 'POST':
#         # Обработка данных формы
#         return HttpResponse("Данные отправлены!")
#
#
# def show_item(request, item_id):
#     # Логика для обработки данных элемента с указанным ID
#     return render(request, 'app/item.html', {'item_id': item_id})

