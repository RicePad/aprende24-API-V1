import tus
from tusclient import client
import os


def upload_video():
    CLOUDFARE_USER = "hello@jonali.me"
    CLOUDFARE_API = "8cf79442d02535ab732745c9f6bd115fde2ef"
    CLOUDFARE_ZONE_ID = "03ebb1e08cc581768d70970176d4f2a7"
    CLOUDFARE_BASE_URL = "https://api.cloudflare.com/client/v4/"

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
