import tus
from tusclient import client
import os


def upload_video():

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

upload_video()
