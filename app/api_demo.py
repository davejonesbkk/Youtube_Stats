import requests, json

parameters = {'part': 'statistics', 'id': '40ZsvfOT5g8',
			'key': 'AIzaSyBAlaQHho3gk14fcIwcarJfGkxthsoXFl0'}

parameters_thumbs = {'part': 'snippet', 'id': 'qKJWsh6fjhI',
			'key': 'AIzaSyBAlaQHho3gk14fcIwcarJfGkxthsoXFl0'}

headers = {'Content-Type': 'application/json'}

#url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={VIDEO_ID}&key={API_KEY}'

url = 'https://www.googleapis.com/youtube/v3/videos'

#ret = requests.get(url, params=parameters, headers=headers)

ret_thumbs = requests.get(url, params=parameters_thumbs, headers=headers)

#print(ret_thumbs.status_code)

#print(ret_thumbs.text)

#print(ret.status_code)

#print(ret.text)

#data = json.loads(ret.text)

thumbs_data = json.loads(ret_thumbs.text)

videoThumb = thumbs_data['items'][0]['snippet']['thumbnails']['standard']['url']

print(videoThumb)

#print('The view count is ', data['items'][0]['statistics']['viewCount'])
#print('The number of likes is ', data['items'][0]['statistics']['likeCount'])