# youtube-dl
This script uses the Youtube Data Api and youtube-dl to download all videos on a youtube channel. Requires the json, urllib.request, youtube_dl packages. It is also necessary to specify your Youtube Data Api key (follow these instructions: https://developers.google.com/youtube/registering_an_application#Create_API_Keys).
  
Initialize the code with "from youtube import youtube". Use youtube.dl(<"Video url">) to download the given youtube video. Use youtube.dl_all(<"Channel name">) to download all videos from the given channel (WARNING: This can take a long time).
