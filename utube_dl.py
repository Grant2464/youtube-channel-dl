from __future__ import unicode_literals
import youtube_dl

def download(url):
    ydl_opts = {'format': 'best','outtmpl':'%(title)s.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

