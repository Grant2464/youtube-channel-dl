import urllib.request
import json
import utube-dl
def dl_all(channel):
    api_key="AIzaSyB6jkQbOG741dxY78RUaeyrqjt9vkeqRWY"
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername="+channel+"&key="+api_key).read()
    json_data=json.loads(data)
    playlist = json_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    json_url="https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId="+playlist+"&key="+api_key+"&pageToken="
    data = urllib.request.urlopen(json_url).read()
    json_data=json.loads(data)
    i=0
    j=0
    total= json_data['pageInfo']['totalResults']
    print("Loading "+str(total)+" videos...")
    while (i<51):
        if(total-j>50):
            nextpagetoken = json_data['nextPageToken']
        if(j==total):
            break
        videoid = json_data['items'][i]['snippet']['resourceId']['videoId']
        url = "https://www.youtube.com/watch?v="+videoid
        download.download(url)
        print("Download " + str(j+1)+"/" + str(total)+" done")
        i+=1
        j+=1
        if(i==50):
            data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=UU6nSFpj9HTCZ5t-N3Rm3-HA&key="+api_key+"&pageToken="+nextpagetoken).read()
            json_data=json.loads(data)
            i=0
