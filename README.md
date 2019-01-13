# Youtube_Stats

This is a basic Flask app that will return stats from a given video ID such as views, likes etc and the video thumbnail.

<h3>Setting up Youtube API access</h3>

Go to <a href="https://console.developers.google.com">Google Develope Console</a> using any Google account.

In the top right of the screen click <i>'Select project'</i> then 'New project', give it any name then hit 'Create'

When you are in the Dashboard of your project click ' + Enable APIs and Services ' search for 'YouTube Data API v3' click its icon and then the 'Enable' button.

Back at the Dashboard click 'Credentials' at the bottom of the left sidebar menu, click 'Create credentials' and then select 'API Key' from the dropdown menu.

Copy this API key and create a new file in your directory called keys.py like this:

API_KEY="YOUR API KEY HERE"


<h3>Local Installation & setup</h3>

<b>Create a Python3 virual environment</b>

```
virtualenv -p python3 envname
```

<b>Install all requirements (needs pip)</b>

```pip install -r requirements.txt```

<b>In the same directory as run.py:</b>

```export FLASK_APP=run.py

flask run
```

<b>Then go to 127.0.0.1:5000 in your browser</b>


