# storage_handling.py
import firebase_admin
from firebase_admin import credentials, storage
import os
import logging

logging.basicConfig(level=logging.ERROR)  # Configure logging

class StorageHandler:
    """Handles interactions with Google Cloud Storage."""

    def __init__(self, cred_path, bucket_name):
        """
        Initializes the StorageHandler.

        Args:
            cred_path (str): Path to the Firebase credentials JSON file.
            bucket_name (str): Name of the Google Cloud Storage bucket.
        """
        self.cred_path = cred_path
        self.bucket_name = bucket_name
        self.storage_client = None
        self.authenticate()

    def authenticate(self):
        """
        Authenticates with Google Cloud Storage and initializes the client.

        This function sets the environment variable for Google credentials,
        initializes the Firebase app with storage capabilities, and creates
        a Google Cloud Storage client.
        """
        try:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.cred_path
            cred = credentials.Certificate(self.cred_path)
            self.app = firebase_admin.initialize_app(cred, {'storageBucket': self.bucket_name})
            self.storage_client = storage.storage.Client()
        except Exception as e:
            logging.error(f"Error authenticating with Google Cloud Storage: {e}")
            raise

    def photo_download(self, directory='download', prefix='bills'):
        """
        Downloads blobs from the specified bucket and prefix to a local directory.

        Args:
            directory (str): The local directory to download the blobs to.
            prefix (str): The prefix of the blobs to download.

        This function retrieves a list of blobs from the specified Google Cloud Storage
        bucket with the given prefix. It then downloads each blob to the specified
        local directory, naming the files sequentially.
        """
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)

            blobs = self.storage_client.list_blobs(self.bucket_name, prefix=prefix)

            n = 0
            for blob in blobs:
                file_path = os.path.join(directory, f"{n}.jpg")
                blob.download_to_filename(file_path, checksum=None)
                n += 1
                print(f"Downloaded {n} files to: {directory}")

        except Exception as e:
            logging.error(f"Error downloading files: {e}")
            raise