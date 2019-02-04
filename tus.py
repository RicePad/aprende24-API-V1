import tus
from tusclient import client
import os





FILE_PATH = "/Users/jonathan/Desktop/docker_apps/aprende24/content/"
SINGLE_FILE_PATH = "/Users/jonathan/Desktop/docker_apps/aprende24/content/proposal.mp4"

TUS_ENDPOINT = "https://api.cloudflare.com/client/v4/zones/{0}/media".format(CLOUDFARE_ZONE_ID)
HEADERS = {'X-Auth-Key': CLOUDFARE_API,
           'X-Auth-Email': CLOUDFARE_USER}


CHUNK_SIZE = 5242880

my_client = client.TusClient(TUS_ENDPOINT,
                              headers=HEADERS)

uploader = my_client.uploader(SINGLE_FILE_PATH, chunk_size=CHUNK_SIZE)
uploader.upload()
print(uploader)

# for filename in FILE_PATH :
#     my_client = client.TusClient(TUS_ENDPOINT,
#                                   headers=HEADERS)
#     CHUNK_SIZE = 5242880
#
#     if filename.endswith(FILE"*.mp4"):
#         uploader = my_client.uploader(filename, chunk_size=CHUNK_SIZE)
#         uploader.upload()
#         print(uploader)
#     else:
#         print(uploader)
