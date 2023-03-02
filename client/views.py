from django.shortcuts import render
from django.http import HttpResponse
from .models import Client

# Create your views here.
def client(request, pk):
    client=Client.objects.gets(id=pk)
    context={'client': client}
    return render(request, 'client.html', context)
