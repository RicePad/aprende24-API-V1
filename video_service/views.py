from django.views.generic import TemplateView
import requests
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse



cloudfare_headers = { 'Content-Type': 'application/json',
                      'X-Auth-Key' : CLOUDFARE_API,
                      'X-Auth-Email': CLOUDFARE_USER ,}

def get_cloudaflare_info():

    api_url = "{0}zones/{1}/media".format(CLOUDFARE_BASE_URL, CLOUDFARE_ZONE_ID)

    response = requests.get(api_url, headers=cloudfare_headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

cloudflare_account_info = get_cloudaflare_info()

def list_all_cloudfare_data(request):
    cloudflare_info = cloudflare_account_info['result']
    print("type:", type(cloudflare_info))
    return render(request, "cloudflare_list.html", {"cloudflare_info": cloudflare_info})

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"
