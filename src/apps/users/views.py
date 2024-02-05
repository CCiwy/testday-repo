from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('restricted-content/')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'login.html')


@login_required
def restricted_content(request):
    context = {'email': request.user.email}
    return render(request, 'restricted_content.html', context) 
