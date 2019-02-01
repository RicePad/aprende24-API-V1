import requests
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


cloudfare_headers = { 'Content-Type': 'application/json',
                      'X-Auth-Key' : CLOUDFARE_API,
                      'X-Auth-Email': CLOUDFARE_USER ,
}

def get_cloudaflare_info():

    api_url = "{0}zones/{1}/media".format(CLOUDFARE_BASE_URL, CLOUDFARE_ZONE_ID)
    # api_url = "{0}accounts?page=1&per_page=20&direction=desc".format(CLOUDFARE_BASE_URL)


    response = requests.get(api_url, headers=cloudfare_headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

cloudfare_account_info = get_cloudaflare_info()

# if cloudfare_account_info is not None:
#     # print("Here's your info: ")
#     for k, v in cloudfare_account_info['result'][0].items():
#         print('{0}:{1}'.format(k, v))
#
# else:
#     print('[!] Request Failed')

# jsonToDictionary = json.dumps(cloudfare_account_info)
# print(jsonToDictionary)

def list_all_cloudfare_data(requests):
    cloudfare_info = json.dumps(cloudfare_account_info)
    return render(request, "cloudflare_list.html", {"cloudfare_info": cloudfare_info})
