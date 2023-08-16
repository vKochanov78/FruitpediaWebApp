from django.shortcuts import render, redirect
from .forms import (ProfileForm,
                    FruitCreationForm,)

from Fruitpedia.web.models import Fruit, Profile


def index_view(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, 'web/index.html', context)


def dashboard_view(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()
    context = {'profile': profile, "fruits": fruits}
    return render(request, 'web/dashboard.html', context)


def fruit_create_view(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        fruit_form = FruitCreationForm(request.POST)
        if fruit_form.is_valid():
            fruit_form.save()
            return redirect('dashboard')
    else:
        fruit_form = FruitCreationForm()

    context = {'profile': profile, 'fruit_form': fruit_form}
    return render(request, 'web/create-fruit.html', context)


def fruit_details_view(request, fruit_id):
    profile = Profile.objects.first()
    fruits = Fruit.objects.get(id=fruit_id)
    context = {'fruits': fruits, 'profile': profile}
    return render(request, 'web/details-fruit.html', context)


def fruit_edit_view(request, fruit_id):
    profile = Profile.objects.first()
    fruits = Fruit.objects.get(id=fruit_id)
    context = {'fruits': fruits, 'profile': profile}
    return render(request, 'web/edit-fruit.html', context)


def fruit_delete_view(request, fruit_id):
    profile = Profile.objects.first()
    fruits = Fruit.objects.get(id=fruit_id)
    context = {'fruits': fruits, 'profile': profile}
    fruits.delete()
    return render(request, 'web/delete-fruit.html', context)


def profile_create_view(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm()
    profile = Profile.objects.first()
    context = {
        "profile": profile,
        "form": form,
    }

    return render(request, 'web/create-profile.html', context)


def profile_details_view(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, 'web/details-profile.html', context)


def profile_edit_view(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, 'web/edit-profile.html', context)


def profile_delete_view(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, 'web/delete-profile.html', context)
