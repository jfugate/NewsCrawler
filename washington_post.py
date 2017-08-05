import urllib3, requests, json, BeautifulSoup, os

def the_washington_post():
	news_source="the-washington-post"
	http_connect = requests.get("https://newsapi.org/v1/articles?source=" + news_source + "&apiKey=") #+ os.envrion['API_KEY']).read()
	json_response = json.loads(http_connect.text)
	for i in range(0, len(json_response['articles'])):
		title = json_response['articles'][i]['title']
		author = json_response['articles'][i]['author']
		url = json_response['articles'][i]['url']
		description = json_response['articles'][i]['description']
		publish_time = json_response['articles'][i]['publishedAt']
		print title + "\n" + author + "\n" + description + "\n" + url + "\n" + publish_time

the_washington_post()
