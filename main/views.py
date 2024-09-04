from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152052',
        'name': 'Alyssa Layla Sasti',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)

# Create your views here.
