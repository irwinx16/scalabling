from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import AddressForm
import requests

def get_address(request):

    if request.method == 'POST':
        form = AddressForm(request.POST)

        if form.is_valid():
            #clean the data
            data = form.cleaned_data['add_field']
            addr = data.upper().split(' ')

            url = 'https://data.cityofchicago.org/resource/u9xt-hiju.json?'
            params = dict(street_direction='W', street_name='DIVISION',street_type='ST')
            res = requests.get(url, params=params).json()

            print(res)

            context = {
            'st_num': addr[0],
            'st_dir': addr[1],
            'st_name': addr[2],
            'st_type': addr[3]
            }
            breakpoint()

            template = loader.get_template('thanks.html')

            return HttpResponse(template.render(context, request))

    else:
        form = AddressForm()

    return render(request, 'form.html', {'form':form})
