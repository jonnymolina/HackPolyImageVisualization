from clarifai.client import ClarifaiApi
import urllib.request

class Functions:
	
	def __init__(self):
		self.clarifai_api = ClarifaiApi()
		print("initialized")

	def get_tags(self, url):
		result = self.clarifai_api.tag_image_urls('http://www.gettyimages.ca/gi-resources/images/Homepage/Category-Creative/UK/UK_Creative_462809583.jpg')
		return result["results"][0]["result"]["tag"]["classes"]


	def get_image(self, url):
		pass

	def load(self, url):
		pass

Functions().get_tags("ddd")