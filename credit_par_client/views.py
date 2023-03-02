from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from .models import Clients
from .forms import ClientsForm

# Create your views here.
def clients(request, pk):
    form=ClientsForm()
    if request.method=='POST':
        form=ClientsForm(request.POST, instance=clients)
        if form.is_valid():
            form.save()
    clients=Clients.objects.gets(id=pk)
    context={'clients': clients}
    return render(request, 'clients.html', context)

class ClientsUpdateView(UpdateView):
    model=Clients
    fields=['amount_paid']
    template_name='amountpaid.html'
    success_url='/'