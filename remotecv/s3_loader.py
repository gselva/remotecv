import os
from boto.s3.connection import S3Connection
from boto.s3.bucket import Bucket
from boto.s3.key import Key

def load_sync(path):
    bucket_name, bucket_path = _get_bucket(path)
    bucket_loader = Bucket(connection=get_connection(),name=bucket_name)

    file_key = bucket_loader.get_key(bucket_path)
    return file_key.read()
    
    
def get_connection():
    conn = S3Connection(os.getenv('AWS_ACCESS_KEY_ID', None), os.getenv('AWS_SECRET_ACCESS_KEY', None))

    return conn    

def _get_bucket(url):
    """
    Returns a tuple containing bucket name and bucket path.
    url: A string of the format /bucket.name/file/path/in/bucket
    """

    url_by_piece = url.lstrip("/").split("/")
    bucket_name = url_by_piece[0]
    bucket_path = "/".join(url_by_piece[1:])
    return bucket_name, bucket_path