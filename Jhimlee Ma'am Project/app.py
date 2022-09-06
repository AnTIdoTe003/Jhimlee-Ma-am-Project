# pip install --upgrade google-api-python-client
# pip install --upgrade google-cloud-storage

try:
    from google.cloud import storage
    import google.cloud.storage
    import json
    import os
    import sys
except Exception as e:
    print("Error : {} ".format(e))

PATH = os.path.join(os.getcwd(), 'project_name.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = PATH

storage_client = storage.Client(PATH)

storage_client

bucket = storage_client.get_bucket('myfirst-bucket')

import pandas as pd
import io
from io import BytesIO

df = pd.read_csv(
    io.BytesIO(
        bucket.blob(blob_name='app_protoype - Sheet1.csv').download_as_string()
    ),
    encoding='UTF-8',
    sep=',')
df.head(1)
