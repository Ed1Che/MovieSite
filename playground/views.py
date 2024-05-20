from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Suggestion
# Create your views here.

def Home(request):
    return render (request, 'home.html')

def motivational(request):
    return render (request, 'motiv.html' )

def love(request):
    return render (request, 'love.html' )

def inspire(request):
    return render (request, 'inspire.html' )

def funny(request):
    return render (request, 'funny.html' )

def show_popup_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        genre = request.POST.get('genre')
        
        suggestion = Suggestion.objects.create(Title=title, Director=director, genre=genre)
        return JsonResponse({'success': True})
    return render(request, 'suggestion.html')

def movie_list(request):
    movies = Suggestion.objects.all()
    return render(request, 'movieList.html', {'movies': movies})