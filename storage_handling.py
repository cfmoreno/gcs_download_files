import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import os

class StorageHandler:

	def __init__(self, cred, bucket_name):
		#set the environ
		os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred    
		#get credentials
		self.cred = credentials.Certificate(cred)
		#get bucket name
		self.bucket_name = bucket_name
		#call Authenticate function 
		self.authenticate()

	def authenticate(self):
		self.storage_client = storage.storage.Client()	
		#initialize the firebase_admin
		firebase_admin.initialize_app(self.cred, {'storageBucket': self.bucket_name})
		# initialize storage client
		self.storage_client = storage.storage.Client()

	# function that downloads selfies to directory, the directory can be especified and the user could also be especified
	def photo_download(self, directory = 'download'):

		# get all the blobs
		self.blobs = self.storage_client.list_blobs('YourPage.appspot.com', prefix = 'bills')

		n=0

		for blob in self.blobs:
			blob.download_to_filename(directory + '/'+ str(n)+'.jpg',checksum = None)
			n = n + 1
			print('I have downloaded',str(n),'files and stored them in:',directory)



	

	





