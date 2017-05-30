import urllib.request
import json
def list_all(channel):
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
    filename=channel+" - "+str(total)+".txt"
    f = open(filename, 'w', encoding='utf-8')

    while (i<51):
        if(total-j>50):
            nextpagetoken = json_data['nextPageToken']
        if(j==total):
            f.close()
            print("Done")
            break
        videoid = json_data['items'][i]['snippet']['resourceId']['videoId']
        url = "https://www.youtube.com/watch?v="+videoid
        title=json_data['items'][i]['snippet']['title']
        all_info = str(j)+title+" /---\ "+url+'\n'
        f.write(   str(all_info)    )
        i+=1
        j+=1
        if(i==50):
            data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=UU6nSFpj9HTCZ5t-N3Rm3-HA&key="+api_key+"&pageToken="+nextpagetoken).read()
            json_data=json.loads(data)
            i=0

