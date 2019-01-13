

from flask import render_template

from app import app 

import requests, json

import keys
API_KEY = keys.API_KEY

parameters = {'part': 'statistics', 'id': 'qKJWsh6fjhI',
			'key': API_KEY}

parameters_thumbs = {'part': 'snippet', 'id': 'qKJWsh6fjhI',
			'key': API_KEY}

headers = {'Content-Type': 'application/json'}

url = 'https://www.googleapis.com/youtube/v3/videos'

ret_stats = requests.get(url, params=parameters, headers=headers)

ret_thumbs = requests.get(url, params=parameters_thumbs, headers=headers)

@app.route('/')
def index():

	stats_data = json.loads(ret_stats.text)

	thumbs_data = json.loads(ret_thumbs.text)

	viewCount = int(stats_data['items'][0]['statistics']['viewCount'])

	likeCount = int(stats_data['items'][0]['statistics']['likeCount'])

	dislikeCount = int(stats_data['items'][0]['statistics']['dislikeCount'])

	videoThumb = thumbs_data['items'][0]['snippet']['thumbnails']['standard']['url']

	if likeCount >= dislikeCount:

		likesRatio = (dislikeCount / likeCount * 100)
		likesRatio = round(100 - likesRatio)
		

	else:
		likesRatio = (dislikeCount / likeCount * 100)
		likesRatio = round(100 - likesRatio)
		


	return render_template('index.html', viewCount=viewCount, likeCount=likeCount, dislikeCount=dislikeCount,
	 videoThumb=videoThumb, likesRatio=likesRatio)



