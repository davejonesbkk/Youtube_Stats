import requests, json

import keys
API_KEY = keys.API_KEY

parameters = {'part': 'statistics', 'id': 'qKJWsh6fjhI',
			'key': API_KEY}

parameters_thumbs = {'part': 'snippet', 'id': 'qKJWsh6fjhI',
			'key': API_KEY}

headers = {'Content-Type': 'application/json'}

#url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={VIDEO_ID}&key={API_KEY}'

url = 'https://www.googleapis.com/youtube/v3/videos'

ret = requests.get(url, params=parameters, headers=headers)

ret_thumbs = requests.get(url, params=parameters_thumbs, headers=headers)

#Get the HTTP status code of the video thumbnail
#print(ret_thumbs.status_code)

#Get all text, data & tags for the thumbnail
#print(ret_thumbs.text)

#Get the video status code
#print(ret.status_code)

#Get the all details for the video
#print(ret.text)

data = json.loads(ret.text)

print(data)

thumbs_data = json.loads(ret_thumbs.text)

#print(thumbs_data)

videoThumb = thumbs_data['items'][0]['snippet']['thumbnails']['standard']['url']

#print(videoThumb)

view_count = int(data['items'][0]['statistics']['viewCount'])
print('The view count is ', view_count)

likes_count = int(data['items'][0]['statistics']['likeCount'])
print('The number of likes is ', likes_count)

dislikes_count = int(data['items'][0]['statistics']['dislikeCount'])
print('The number of likes is ', dislikes_count)

if likes_count >= dislikes_count:

	likes_ratio = (dislikes_count / likes_count * 100)
	likes_ratio = 100 - likes_ratio
	print('Like to dislike ratio is ', round(likes_ratio),"% positive" )

else:
	likes_ratio = (likes_count / dislikes_count * 100)
	likes_ratio = 100 - likes_ratio
	print('Like to dislike ratio is ', round(likes_ratio),"% positive" )
