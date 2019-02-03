from tusclient import client
import os


CLOUDFARE_USER = os.getenv("CLOUDFARE_USER")
CLOUDFARE_API = os.getenv("CLOUDFARE_API")
CLOUDFARE_ZONE_ID = os.getenv("CLOUDFARE_ZONE_ID")
CLOUDFARE_BASE_URL = os.getenv("CLOUDFARE_BASE_URL")



def upload_video():
    CLOUDFARE_USER = os.getenv("CLOUDFARE_USER")
    CLOUDFARE_API = os.getenv("CLOUDFARE_API")
    CLOUDFARE_ZONE_ID = os.getenv("CLOUDFARE_ZONE_ID")
    CLOUDFARE_BASE_URL = os.getenv("CLOUDFARE_BASE_URL")

    cloudflare_headers = {
                          'X-Auth-Key' : CLOUDFARE_API,
                          'X-Auth-Email': CLOUDFARE_USER,
                          'Tus-Resumable': '1.0.0',
                          'Upload-Length': '900000000',}

    # Set Authorization headers if it is required
    # by the tus server.
    # my_client = client.TusClient('https://api.cloudflare.com/client/v4/zones/03ebb1e08cc581768d70970176d4f2a7/media',
    #                              headers={'X-Auth-Email': CLOUDFARE_USER,})

    my_client = client.TusClient('http://master.tus.io/files/')


    # Set more headers.
    # my_client.set_headers({
    #                        'X-Auth-Key': CLOUDFARE_API,
    #                        'Tus-Resumable': '1.0.0',
    #                        'Upload-Length': '900000000',
    #
    #                        })
    # CHOOESE VIDEO FILE TO UPLOAD INTO CLIENT
    uploader = my_client.uploader('proposal.mp4', chunk_size=5242880)
    print(uploader)

    # Upload a chunk i.e 200 bytes.

    # Uploads the entire file.
    # This uploads chunk by chunk.
    uploader.upload()
    print(uploader)

    uploader.upload(stop_at=1000)


video = upload_video()
