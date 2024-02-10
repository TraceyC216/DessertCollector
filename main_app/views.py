from django.shortcuts import render, redirect
from .models import Dessert
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .form import ProcessForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def desserts_index(request):
    desserts = Dessert.objects.all()
    return render(request, 'desserts/index.html', {'desserts': desserts})

def desserts_detail(request, dessert_id):
    dessert = Dessert.objects.get(id=dessert_id)
    process_form = ProcessForm()
    return render(request, 'desserts/detail.html', {'dessert': dessert, 'process_form': process_form})

class DessertCreate(CreateView):
    model = Dessert
    fields = '__all__'
    success_url = '/desserts/'

class DessertUpdate(UpdateView):
    model = Dessert
    fields = ['name','description', 'allergens']

class DessertDelete(DeleteView):
    model = Dessert
    success_url = '/desserts/'

def add_step(request, dessert_id):
    form = ProcessForm(request.POST)

    if form.is_valid():
        new_step = form.save(commit=False)
        new_step.dessert_id = dessert_id 
        new_step.save()
    return redirect('detail', dessert_id=dessert_id)  
