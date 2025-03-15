import os
from storage_handling import StorageHandler
import logging

logging.basicConfig(level=logging.ERROR)

def run():
    """
    Downloads files from a Google Cloud Storage bucket.

    This function creates a StorageHandler instance, authenticates with Google Cloud Storage,
    and then calls the photo_download method to download files from the specified bucket.
    """
    try:
        storage_handler = StorageHandler('cred.json', 'YourPage.appspot.com') # MODIFY TO YOUR BUCKET NAME.
        storage_handler.photo_download()
    except Exception as e:
        logging.error(f"An error occurred during download: {e}")

if __name__ == '__main__':
    run()