# youtube-channel-dl
This script uses the Youtube Data Api and youtube-dl to download all videos on a youtube channel. Requires the json, urllib.request, youtube_dl packages. It is also necessary to specify your Youtube Data Api key (follow these instructions: https://developers.google.com/youtube/registering_an_application#Create_API_Keys) in the channel_list and channel-dl files.
  
Use channel_list.list_all(<Channel name>) to output the titles and links to all videos on the given channel to a text file. Use channel-dl.dl_all(<Channel name>) to download all videos from the given channel (WARNING: This can take a long time).
