from multiprocessing import context
from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    notes = Notes.objects.all()
    people = People.objects.all()
    
    
    
    context = {'notes': notes, 'people':people}
    
    return render(request, 'index.html', context)


def newNote(request, pk):
    note = Notes.objects.get(id=pk)    
    context = {'note':note}
    
    
    return render(request, 'newNote.html', context)