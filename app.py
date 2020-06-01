from flask import Flask, render_template, request
from googleapiclient.discovery import build
import os
import json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if (request.method == 'POST'):
<<<<<<< HEAD
        youtube = build('youtube', 'v3', developerKey = os.environ.get('YT'))
||||||| 4c8cea6
        api_key = 'AIzaSyA8hURwcnKk-2jGHgKuGshvJwfUgajyMT4'
        youtube = build('youtube', 'v3', developerKey = api_key)
=======
        youtube = build('youtube', 'v3', developerKey = api_key)
>>>>>>> 0f746c1ca4d9715a045d9ac2d95715f65dce246c
        data = dict()
        
        def get_channel_details(url):

            url = url[24:]

            if(url[0]=='c'):
                id = url[8:]
                req = youtube.channels().list(
                    part = 'statistics',
                    id = id
                    )

                response = req.execute()
                return response

            else:
                user = url[5:]
                req = youtube.channels().list(
                    part = 'statistics',
                    forUsername = user
                    )

                response = req.execute()
                return response

        URL = request.form['query']
        data.update({'search' : URL})
        data.update({'statistics':get_channel_details(URL)})

        cid = get_channel_details(URL)['items'][0]['id']

        #playlistinfo--------------------------------
        req = youtube.playlists().list(
                part = 'snippet',
                channelId = cid,
                maxResults = 20
                )

        data.update({'playlistInfo': req.execute()})

        #channelinfo---------------------------
        req = youtube.channels().list(
            part = 'snippet',
            id = cid
            )

        data.update({'channelInfo': req.execute()})
        
        # print(json.dumps(data, sort_keys=True, indent=4))
        return render_template('main.html', data=data)

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
