from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, MyModel
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from students.forms import StudentForm


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


class StudentCreateView(CreateView):
    model = Student
    # Вместо fields указываем
    form_class = StudentForm

    # fields = ['first_name', 'last_name', 'email', 'year', 'enrollment_date']  # Поля модели, которые будут
    # # включены в форму
    template_name = 'students/student_form.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = reverse_lazy('students:student_list')  # URL, на который будет перенаправлен пользователь
    # после успешной отправки формы


class StudentUpdateView(UpdateView):
    model = Student
    # Вместо fields указываем
    form_class = StudentForm
    # fields = ['first_name', 'last_name', 'email', 'year', 'enrollment_date']  # Поля модели, которые будут
    # # включены в форму
    template_name = 'students/student_form.html'  # Шаблон, который будет использоваться для отображения формы
    success_url = reverse_lazy('students:student_list')  # URL, на который будет перенаправлен пользователь
    # после успешной отправки формы


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('students:student_list')


class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelListView(ListView):
    model = MyModel
    template_name = 'students/mymodel_list.html'
    context_object_name = 'mymodels'


class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'students/mymodel_detail.html'
    context_object_name = 'mymodel'


class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'students/mymodel_confirm_delete.html'
    success_url = reverse_lazy('students:mymodel_list')


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

