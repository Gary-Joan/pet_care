from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, UserProfileForm, form_doctor_grade

@login_required
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        form_doctor = form_doctor_grade()
    else:
        username = 'No esta logeado'

    context = {'username': username, 'form_doctor': form_doctor}
    return  render(request, 'pet_care/user/cliente.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('log:perfil')

    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return  render(request, 'register.html', context)


def get_grade_doctor(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = form_doctor_grade(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('log:perfil')

    # if a GET (or any other method) we'll create a blank form
    else:
        form_doctor = form_doctor_grade()

    return render(request, 'pet_care/user/cliente.html', {'form_doctor': form_doctor})