from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from dogs.forms import DogForm, ParentForm
from dogs.models import Dog, Parent
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def base(request):
    return render(request, 'dogs/base.html')


class DogListView(ListView):
    model = Dog
    # template_name = 'dogs/dog_list.html'  # можно не указывать, это имя ищет по умолчанию
    # context_object_name = 'dog_list'  # можно не указывать, это имя ище по умолчанию


class DogDetailView(DetailView):
    model = Dog
    # template_name = 'dogs/dog_detail.html'  # можно не указывать, это имя ищет по умолчанию
    # context_object_name = 'dog'  # можно не указывать, это имя ищет по умолчанию

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     obj.views_count += 1
    #     obj.save()
    #
    #     return obj


class DogCreateView(LoginRequiredMixin, CreateView):
    model = Dog
    form_class = DogForm
    # fields = ['name', 'breed', 'photo', 'born_date']
    template_name = 'dogs/dog_form.html' # можно не указывать, это имя ищет по умолчанию
    success_url = reverse_lazy('dogs:dog_list')

    def form_valid(self, form):
        dog = form.save()
        user = self.request.user
        dog.owner = user
        dog.save()
        return super().form_valid(form)


class DogUpdateView(LoginRequiredMixin, UpdateView):
    model = Dog
    form_class = DogForm
    # fields = ['name', 'breed', 'photo', 'born_date']
    template_name = 'dogs/dog_form.html' # можно не указывать, это имя ищет по умолчанию
    success_url = reverse_lazy('dogs:dog_list')

    def get_success_url(self):
        return reverse('dogs:dog_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        DogFormset = inlineformset_factory(Dog, Parent, ParentForm, extra=1)
        if self.request.method == 'POST':
            context_data["formset"] = DogFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = DogFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class DogDeleteView(LoginRequiredMixin, DeleteView):
    model = Dog
    template_name = 'dogs/dog_confirm_delete.html' # можно не указывать, это имя ищет по умолчанию
    success_url = reverse_lazy('dogs:dog_list')


# def dogs_list(request):
#     dogs = Dog.objects.all()
#     context = {"dogs": dogs}
#     return render(request, 'dogs/dog_list.html', context)


# def dogs_detail(request, pk):
#     dog = get_object_or_404(Dog, pk=pk)
#     breed_dog = get_object_or_404(Breed, name=dog.breed)
#     context = {
#         "dog": dog,
#         "breed_dog": breed_dog,
#     }
#     return render(request, 'dogs/dogs_detail.html', context)

