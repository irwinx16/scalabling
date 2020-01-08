from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import AddressForm

def get_address(request):

    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():

            addr = form.cleaned_data['add_field']

            context = {
            'address': addr
            }

            template = loader.get_template('thanks.html')

            return HttpResponse(template.render(context, request))

    else:
        form = AddressForm()

    return render(request, 'form.html', {'form':form})
