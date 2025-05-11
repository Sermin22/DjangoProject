from django.shortcuts import render, get_object_or_404
from dogs.models import Dog, Breed


def base(request):
    return render(request, 'base.html')


def dogs_list(request):
    dogs = Dog.objects.all()
    context = {"dogs": dogs}
    return render(request, 'dogs_list.html', context)


def dogs_detail(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    breed_dog = get_object_or_404(Breed, name=dog.breed)
    context = {
        "dog": dog,
        "breed_dog": breed_dog,
    }
    return render(request, 'dogs_detail.html', context)

