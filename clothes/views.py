from django.shortcuts import render, redirect

from clothes.forms import ShirtForm, DressForm
from clothes.models import Shirt, Dress

# Create your views here.
def shirt(request):
    if request.method == 'POST':
        form = ShirtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shirt')
    else:
        form = ShirtForm()
    return render(request, 'shirt.html',{'form': form})

def dress(request):
    if request.method == 'POST':
        form = DressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dress')
    else:
        form = DressForm()
    return render(request, 'dress.html',{'form': form})

def dresslist(request):
    dresss = Dress.objects.all()
    return render(request, 'dresslist.html',{'dresss': dresss})


def shirtlist(request):
    shirts = Shirt.objects.all()
    return render(request, 'shirtlist.html',{'shirts': shirts})