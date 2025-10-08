from django.shortcuts import render, HttpResponse

def start(request):
    return render(request, 'index.html', {})