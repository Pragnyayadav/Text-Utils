from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def results(request):
    djtext = request.GET.get('text','default')
    djtext = djtext.upper()
    nfa = {'text':djtext}
    return render(request, 'results.html', nfa)