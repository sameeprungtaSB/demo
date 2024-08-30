# login/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import LoginForm
from .models import User
from .forms import RegistrationForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email, password=password)
                # Set the user session
                request.session['user_email'] = user.email
                # Redirect to the home page
                return redirect('home')
            except User.DoesNotExist:
                return JsonResponse({'error': 'Invalid email or password'}, status=400)
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})

def home_view(request):
    return render(request, 'login/home.html')

# login/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import LoginForm, RegistrationForm
from .models import User

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']

            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already registered'}, status=400)

            User.create(email=email, username=username, password=password, phone_number=phone_number)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'login/register.html', {'form': form})
