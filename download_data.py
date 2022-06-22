import os
from storage_handling import StorageHandler

def run():

    os.makedirs('download')

    storage = StorageHandler('cred.json', 'bills')

    storage.photo_download()

if __name__ == '__main__':
    run()