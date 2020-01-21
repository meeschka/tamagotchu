from django.shortcuts import render
from .models import Pet
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
    return render(request, 'pets/details.html', {'pet': pet})