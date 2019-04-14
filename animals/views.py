from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal
from django.core.serializers import serialize
from .forms import AnimalForm

# Create your views here.


def serialized_data(data):
    try:
        return serialize("json", data)
    except Exception as exe:
        return serialize("json", [data])


def get_all_animals(request):
    name = request.GET.get("name")
    if name:
        animal = Animal.objects.all().filter(name=name)
        return HttpResponse(serialized_data(animal))
    animals = Animal.objects.all()
    return HttpResponse(serialized_data(animals))


def get_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return HttpResponse(serialized_data(animal))


def get_all_dogs(requst):
    dogs = Animal.objects.filter(kind="D")
    return HttpResponse(serialized_data(dogs))


def order_animals(request):
    animals = Animal.objects.all().order_by("-age")
    return HttpResponse(serialized_data(animals))


def create_animal(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    kind = request.GET.get("kind")
    image_url = request.GET.get("image_url")
    breed = request.GET.get("breed")
    description = request.GET.get("description")
    animal = Animal(
        name=name,
        description=description,
        age=age,
        kind=kind,
        image_url=image_url,
        breed=breed,
    )
    animal.save()
    return HttpResponse(
        f"Animal of kind {animal.kind} with name {animal.name} saved to DB"
    )


def edit_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    old_name = animal.name
    name = request.GET.get("name")
    animal.name = name
    animal.save()
    return HttpResponse(f"Name of the animal changed from {old_name} to {name}")


def delete(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    a_id = animal_id
    animal.delete()
    return HttpResponse(f"animal with id {a_id} deleted form DB")


def create_animal_form(request):
    if request.method == "GET":
        form = AnimalForm()
        context = {"form": form}
        return render(request, "create.html", context)
    elif request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('not Created')


