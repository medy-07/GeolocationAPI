from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from xml.etree.ElementTree import Element,tostring
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from dict2xml import dict2xml


@api_view([ 'POST'])
def getLatLong(request):
    API_KEY = "API_KEY" #replace API_KEY with API Key   
    requestBody = JSONParser().parse(request)
    print("abcd"+str(requestBody))
    address = requestBody['address']
    output_type = requestBody['output_format']
    print(address) 
    print(output_type)
    
    params = {
        'key' : API_KEY,
        'address' : address
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params).json()
    # response.keys()

    if response['status'] == 'OK':
        geometry= response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']
        dict1= {"coordinates": {"lat":lat, "long":lon}, "address":address}
        data = json.dumps({"coordinates": {"lat":lat, "long":lon}, "address":address})
        if output_type == 'json':
            return HttpResponse(data, content_type='application/json')
        elif output_type == 'xml':
            e = dict2xml(dict1)
            return HttpResponse(e)
    # Create your views here.
