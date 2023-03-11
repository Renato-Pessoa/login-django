from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def sign_in(request):

    if str(request.method) == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse(f'Olá, {username}')
        
        else:
            return HttpResponse("Usuário não cadastrado")

    return render(request, 'core/signIn.html')

def sign_up(request):

    if str(request.method) == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email =  request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        user = User.objects.filter(username=username).first()

        if password == confirm_password and not user:
            user = User.objects.create_user(first_name=name, username=username, email=email, password=password)

            user.save()

            return redirect('sign_in')

    return render(request, 'core/signUp.html')
