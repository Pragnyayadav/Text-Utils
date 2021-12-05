from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def results(request):
    text = request.GET.get('text','default')
    uppertext = text.upper()
    lowertext = text.lower()
    counttext = len(text)
    wordcounttext = text.count(' ') + 1
    nfa = {
        'text': text,
        'uppertext':uppertext,
        'lowertext':lowertext,
        'counttext':counttext,
        'wordcounttext':wordcounttext
        }
    
    return render(request, 'results.html', nfa)