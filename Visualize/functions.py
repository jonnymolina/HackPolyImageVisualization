from clarifai.client import ClarifaiApi
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import json
class Functions:
	
	def __init__(self):
		self.clarifai_api = ClarifaiApi()
		print("initialized")

	def get_tags(self, url):
		result = self.clarifai_api.tag_image_urls(url)
		tags = result["results"][0]["result"]["tag"]["classes"]
		conf_intervals = result["results"][0]["result"]["tag"]["probs"]

		return get_tag_sets(tags, conf_intervals)

	def get_tag_sets(tags, conf_intervals):

		size = len([x for x in conf_intervals if x > 0.90])
		tag_sets = []

		for i in range(size - int(size/3)):
			tag_sets.append((tuple(tags[i:i + int(size/3)])))

		return tag_sets		

	def get_image_url(self, tags):
		url = "https://api.datamarket.azure.com/Bing/Search/v1/Image?$format=json&Query=%27"+ "%20".join(tags) +"%27"
		print(url)
		authent = HTTPBasicAuth("rushil9","4MJB6yiLpF5H2qI+RTkLfomBbLHNYTVdfccpC73YlK0")
		response = requests.get(url, auth = authent).text
		response = eval(response)
		targ_url = response["d"]["results"][0]["MediaUrl"]
		return targ_url

	def load(self, url):
		tag_sets = get_tags(self, url)
		image_urls = []
		for tag in tag_sets:
			image_urls.append(get_image_url(tag))

		return image_urls
		

#print(Functions().get_tags("http://dreamatico.com/data_images/animals/animals-4.jpg"))
print(Functions().get_image_url( tags=["fuzzy", "cats", "cute"]))