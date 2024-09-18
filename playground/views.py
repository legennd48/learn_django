from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greeting(request):
    return render(request, 'greeting.html', {'name': 'Django'}, status=200)