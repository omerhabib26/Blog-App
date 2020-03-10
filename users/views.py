from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, ProfileRegistrationForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        # profile_form = ProfileRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            profile = Profile(user=user, account_type=user_form.cleaned_data['type'])
            profile.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('blog-home')

    else:
        user_form = RegistrationForm()
        # profile_form = ProfileRegistrationForm()

    context = {'user_form': user_form}
    return render(request, 'users/register.html', context)
