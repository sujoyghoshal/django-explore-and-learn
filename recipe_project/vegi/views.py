from django.shortcuts import render, redirect
from .models import Receipe
from .forms import ReceipeForm

def receipes(request):
    if request.method == "POST":
        form = ReceipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ReceipeForm()
    
    recipes = Receipe.objects.all()
    return render(request, 'index.html', {'form': form, 'recipes': recipes})

def delete_recipe(request, id):
    recipe = Receipe.objects.get(id=id)
    recipe.delete()
    return redirect('/')
