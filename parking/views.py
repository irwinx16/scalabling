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

            #call chicago api
            url = 'https://data.cityofchicago.org/resource/u9xt-hiju.json?'

            #pass params for api
            params = dict(street_direction=addr[1], street_name=addr[2],street_type=addr[3])

            #get and save response in json
            res = requests.get(url, params=params).json()

            for field in res:
                if (int(field['address_range_low']) <= int(addr[0]) and int(field['address_range_high']) >= int(addr[0]) ):
                    print(field)

            context = {
            'st_num': addr[0],
            'st_dir': addr[1],
            'st_name': addr[2],
            'st_type': addr[3]
            }


            template = loader.get_template('thanks.html')

            return HttpResponse(template.render(context, request))

    else:
        form = AddressForm()

    return render(request, 'form.html', {'form':form})
