from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
        'nom':'KENGNI',
        'prenom':'Hippolyte'
    }
    return render(request, 'index.html', context)