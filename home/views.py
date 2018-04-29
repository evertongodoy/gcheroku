from django.shortcuts import render, redirect
# Secao 4, Video 24
from django.contrib.auth import logout


# Criado na Secao 4, video 24
def home(request):
    return render(request, 'home.html')

# Criado na Secao 4, video 24
def my_logout(request):
    logout(request)
    # Secao 4, video 24
    # nao vai renderizar de novo o template
       # return render(request, 'home.html')
    # entao, redireciona
    return redirect('home')