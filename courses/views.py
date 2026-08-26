from django.shortcuts import render
from .models import Course

def home(request):
    show = Course.objects.all()

    return render(request, 'index.html', {'tasks': show}) 

def profile(request):
    title = 'Профиль пользователя'
    skils = ['django', 'sql', 'html']
    user = {'name': 'alia', 'age': 22}
    location = ('ufa', 'russia')

    info = {
        'title': title,
        'skils': skils,
        'user': user,
        'location': location
    }

    return render(request, 'profile.html', info)