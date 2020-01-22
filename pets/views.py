from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Pet
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pets_index(request):
    pets = Pet.objects.all()
    return render(request, 'pets/index.html', {'pets': pets})

def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    form = FeedingForm()
    return render(request, 'pets/details.html', {'pet': pet, 'feeding_form': form})

def add_feeding(request, pet_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pet_id = pet_id
        new_feeding.save()
    return redirect('details', pet_id=pet_id)


class PetCreate(CreateView):
    model = Pet
    fields = '__all__'
    success_url = '/pets/'

class PetUpdate(UpdateView):
    model = Pet
    fields = ['breed', 'description', 'age']

class PetDelete(DeleteView):
    model = Pet
    success_url = '/pets/'
