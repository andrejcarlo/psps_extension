import os
import cloudinary
from cloudinary.api import delete_resources_by_tag, resources_by_tag
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

# import keys
from config import config

cloudinary.config(
  cloud_name = config['cloud_name'],  
  api_key = config['api_key'],  
  api_secret = config['api_secret']  
)

DEFAULT_TAG = "python_sample_basic"

path = 'cow_photos'
files = os.listdir(path)

def rename_dataset():
    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))
        
def dump_response(response):
    print("Upload response:")
    for key in sorted(response.keys()):
        print("  %s: %s" % (key, response[key]))


def upload_test():
    print("--- Upload a local file with custom public ID")
    response = upload(
        "albert_apollo/0.jpg",
        tags=DEFAULT_TAG,
        public_id="psps_id",
    )
    dump_response(response)
    url, options = cloudinary_url(
        response['public_id'],
        format=response['format'],
        crop="fit"
    )
    print("Fit into 200x150 url: " + url)
    print("")

def upload_dataset():
    for index, file in enumerate(files):
        psps_object = os.path.join(path, file)
        print("Uploading ", psps_object)
        upload(
            psps_object,
            folder="cow",
            overwrite = True,
            public_id=index,
            unique_filename=False,
        )

upload_dataset()