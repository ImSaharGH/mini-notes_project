from django.shortcuts import render



def Notes_list_view(request):
    return render (request , 'notes/notes_list.html')
