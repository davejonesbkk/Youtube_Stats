# Sample Python code for user authorization

import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

key = 'AIzaSyBAlaQHho3gk14fcIwcarJfGkxthsoXFl0'

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def channels_list_by_username(service, **kwargs):
  results = service.channels().list(
    **kwargs
  ).execute()
  
  print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
       (results['items'][0]['id'],
        results['items'][0]['snippet']['title'],
        results['items'][0]['statistics']['viewCount']))

  

def videos_by_username(service, **kwargs):
  video_results = service.videos().list(
    **kwargs
  ).execute()

  print(video_results['items'][0]['id'],
        video_results['items'][0]['snippet']['title'],
        video_results['items'][0]['snippet']['description'])
        

def get_ratings(service, **kwargs):
  ratings = service.videos().getRating(
    **kwargs
).execute()

  print(ratings['items'][0]['rating'])


def get_stats(service, **kwargs):
  stats = service.videos().list(
    **kwargs
  ).execute()

  print(stats['items'][0]['id'],
        stats['items'][0]['statistics']['viewCount'],
        stats['items'][0]['statistics']['likeCount'],
        stats['items'][0]['statistics']['dislikeCount'])



if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
  channels_list_by_username(service,
      part='snippet,contentDetails,statistics',
      forUsername='GoogleDevelopers')

  videos_by_username(service, 
      part='snippet', id='e5QInAMqEKw', maxResults=5)

  get_ratings(service, id='e5QInAMqEKw')

  get_stats(service, part='statistics', id='e5QInAMqEKw')



