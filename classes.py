import urllib3, requests, json, BeautifulSoup, os
class News_Crawler:
	def __init__(self):
		self.nyt_endpoint = "https://newsapi.org/v1/articles?source=" + news_source + "&apiKey=") #+ os.envrion['API_KEY']
		self.twp_endpoint = "https://newsapi.org/v1/articles?source=" + news_source + "&apiKey=") #+ os.envrion['API_KEY']
	def new_york_times(self):
		news_source="the-new-york-times"
		http_connect = requests.get(self.nyt_endpoint).read()
		json_response = json.loads(http_connect.text)
		for i in range(0, len(json_response['articles'])):
			title = json_response['articles'][i]['title']
			author = json_response['articles'][i]['author']
			url = json_response['articles'][i]['url']
			description = json_response['articles'][i]['description']
			publish_time = json_response['articles'][i]['publishedAt']
			print title + "\n" + author + "\n" + description + "\n" + url + "\n" + publish_time

	def the_washington_post(self):
		news_source="the-washington-post"
		http_connect = requests.get(self.twp_endpoint).read()
		json_response = json.loads(http_connect.text)
		for i in range(0, len(json_response['articles'])):
			title = json_response['articles'][i]['title']
			author = json_response['articles'][i]['author']
			url = json_response['articles'][i]['url']
			description = json_response['articles'][i]['description']
			publish_time = json_response['articles'][i]['publishedAt']
			print title + "\n" + author + "\n" + description + "\n" + url + "\n" + publish_time


c = News_Crawler()
c.new_york_times()
c.the_washington_post()
