from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Pet, Toy, PetPhoto, ToyPhoto
from .forms import FeedingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'seicollectorproject'

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
    not_toys = Toy.objects.exclude(id__in = pet.toys.all().values_list('id'))
    return render(request, 'pets/details.html', {'pet': pet, 'feeding_form': form, 'toys': not_toys})

def add_feeding(request, pet_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pet_id = pet_id
        new_feeding.save()
    return redirect('details', pet_id=pet_id)
def add_toy(request, pet_id, toy_id):
    Pet.objects.get(id=pet_id).toys.add(toy_id)
    return redirect('details', pet_id=pet_id)

def remove_toy(request, pet_id, toy_id):
    Pet.objects.get(id=pet_id).toys.remove(toy_id)
    return redirect('details', pet_id=pet_id)

def add_pet_photo(request, pet_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.')]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = PetPhoto(url=url, pet_id=pet_id, s3key=key)
            photo.save()
        except:
            print('An error occured uploading file to S3')
    return redirect('details', pet_id=pet_id)

def add_toy_photo(request, toy_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, toy_id=toy_id, s3key=key)
            photo.save()
        except:
            print('An error occured while uploading file to S3')
    return redirect('toys_detail', toy_id=toy_id)

class ToyList(ListView):
    model=Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields= '__all__'
    success_url = '/toys/'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

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
