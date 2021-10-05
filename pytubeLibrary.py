#pip install pytube


# named as pytube.py , then error
# The circular import error happens because you named your script pytube.py.
# Python prioritises modules in the working directory so you are trying to import your script pytube recursively.

# 1. Search for youtube videos related to a topic
# 2. Search all the videos related to a channel
# 3. Open the video to play (video by video)
# 4. Download a Youtube video
# 5. Download the Youtube Video's audio. -check whether we can do it.
# 6. Download the Youtube Video's subtitle.

def search_video(keyword = "Miracle Schedule Whatsapp message using python "):
    from pytube import Search
    import pywhatkit as py
    yt_watch = "https://www.youtube.com/watch?v="

    # 1. Search for youtube videos related to a topic
    search = Search(keyword)
    yt_videos= search.results
    num = len(yt_videos)
    i=0
    while i<num:
        command = input("Press Enter to play the a video / Type Exit and press Enter to stop search: ")
        if command.lower()=="exit":
            print("Bye")
            break
        else:
            yt_object = yt_videos[i]
            data = "Title: "+str(yt_object.title) +"\n"+ "Duration: "+str(round(yt_object.length/60,2))+" min" + "\n"+"Author: "+str(yt_object.author) # use print(dir(yt_object)) to view all attributes and methods
            url =yt_watch+yt_object.video_id
            py.playonyt(url)
            print(str(i)+"Playing url: "+url+"\n"+data)
            i+=1
            if i==num:
                i=0
                yt_videos= search.get_next_results()
                num = len(yt_videos)
# search_video()

def download_video(url):
    import pytube
    from pytube import Playlist,YouTube

    try :
        yt = YouTube(url) # or can use a youtube object directly.
    except pytube.exceptions.VideoUnavailable:
        print("Video Unavailable")
    else:
        stream  = yt.streams 
        #.get_by_itag(134) # Itag is a youtube is a static youtube video format
        #youtube format identifier code = 134 means mp4 in 360p resolution
        # print("Size: "+str(stream.filesize))
        vid = stream.filter(progressive=True,res = "360p", file_extension = "mp4").first()
        print("Size: "+str(round(vid.filesize/2**20,2))+" MB")
        filepath = vid.download()
        print("Saved in: "+ filepath)
    return filepath

# download_video("https://youtu.be/JqyIzFXm9vk")

def download_audio_track(url):
    from pytube import YouTube
    import os
    yt = YouTube(url) # or can use a youtube object directly.
    stream  = yt.streams.filter(only_audio=True ).first()
    # print("Size: "+str(round(vid.filesize/2**20,2))+" MB")
    filepath = stream.download()

    # Pytube does not support "mp3" format but you can download audio in webm format
    # so use os module for conversion
    base, ext = os.path.splitext(filepath)
    audio_file = base + '.mp3'
    os.rename(filepath, audio_file)
    print("Saved in: "+ audio_file)

# download_audio_track("https://youtu.be/JqyIzFXm9vk")

#  ...........................................................
#  Check error in download_captions(url):
#  Solution : https://stackoverflow.com/questions/68780808/xml-to-srt-conversion-not-working-after-installing-pytube #change caption.py sourcecode file
def download_captions(url):
    from pytube import YouTube
    yt = YouTube(url)
    print("All Avaible Captions : \n",yt.captions)
    en_caption_data = yt.captions['a.en']
    print("\nCaption Data in SRT Format: \n")
    srt_format = en_caption_data.xml_caption_to_srt(en_caption_data.xml_captions)
    print(srt_format)

download_captions("https://youtu.be/JqyIzFXm9vk")
# ............................................................

def download_from_playlist(url_playlist):
    from pytube import Playlist,YouTube
    playlist = Playlist(url_playlist)
    print("Playlist Title: "+playlist.title+"\n")

    video_urls = playlist.video_urls

    for i in range(len(playlist.videos)):
        video = playlist.videos[i]
        print("Title: "+video.title)
        print("URL: "+video_urls[i])
        # download_video(video.watch_url)
        # download_audio_track(video.watch_url)
        print()

# download_from_playlist("https://youtube.com/playlist?list=PLEw03wP6R0QCwyRl4yGHgowPzG9VIYD0q")

def download_from_channel(url_channel):
    from pytube import Channel,YouTube
    channel = Channel(url_channel)
    print("Channel Name: "+channel.channel_name+"\n")

    video_urls = channel.video_urls

    for i in range(len(channel.videos)):
        video = channel.videos[i]
        print("Title: "+video.title)
        print("URL: "+video_urls[i])
        # download_video(video.watch_url)
        # download_audio_track(video.watch_url)
        print()

# download_from_channel("https://www.youtube.com/channel/UC23wTY7YzLCla5Qg3IWauMw")



