from django.shortcuts import render
from .models import Notes



def Notes_list_view(request):
    notes = Notes.objects.all()
    context = {
        'notes_list' : notes , 
    }
    return render (request , 'notes/notes_list.html' , context)
