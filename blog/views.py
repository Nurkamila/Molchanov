from django.shortcuts import render
from django.http import HttpResponse

def posts_list(request):
    n = ['Aika', 'Baika', 'Maika']
    return render(request, 'blog/index.html', context={'names': n})