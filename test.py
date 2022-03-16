import requests
from lxml import html
import os
StreamerStatus = []
StreamerStatus2 = []
def setYTName(theName):
    global yt_name
    yt_name = theName
def removeStatusFiles():
    try:
        if os.path.exists("streamers_twitch_status.txt"):
            os.remove("streamers_twitch_status.txt")
        if os.path.exists("streamers_youtube_status.txt"):
            os.remove("streamers_youtube_status.txt")
    except Exception as e:
        print(e)
    return
def TwitchStreamerList(file_path):
    if file_path == '' or None:
        print("Error: No streamer list selected.")
        return
    try:
        textData=open(file_path,"r")
        list1 = textData.read().split('\n')
        for i in range(len(list1)):
            streamer = list1[i]
            X = CheckTwitchStream(streamer)
            if X == True:
                StreamerStatus.append(streamer + " : ONLINE")
            else:
                StreamerStatus.append(streamer + " : OFFLINE")
        with open("streamers_twitch_status.txt","a") as file1:
            file1.write("[Twitch Streamer Status]\n")
            for row in StreamerStatus:
                s = "".join(map(str, row))
                file1.write(s+'\n')
            file1.close()
    except Exception as e:
        print(e)
    return
def YouTubeStreamerList(file_path):
    if file_path == '' or None:
        print("Error: No streamer list selected.")
        return
    try:
        textData2=open(file_path,"r")
        list2 = textData2.read().split('\n')
        for i in range(len(list2)):
            streamer = list2[i]
            streamerX = streamer.split(',')
            X = CheckYouTubeStream(streamerX[0], streamerX[1])
            if X == True:
                streamerName = str(yt_name)
                StreamerStatus2.append("Channel Name: " + streamerName + " - " + streamerX[0] + " : ONLINE")
            else:
                streamerName = str(yt_name)
                StreamerStatus2.append("Channel Name: " + streamerName + " - " + streamerX[0] + " : OFFLINE")
        with open("streamers_youtube_status.txt","a") as file2:
            file2.write("[YouTube Streamer Status]\n")
            for row in StreamerStatus2:
                s = "".join(map(str, row))
                file2.write(s+'\n')
            file2.close()
    except Exception as e:
        print(e)
    return
def CheckTwitchStream(streamer):
    cts = None
    try:
        response = requests.get("https://twitch.tv/" + streamer)
        body = response.text
        if "isLiveBroadcast" in body:
            print(streamer + " is live streaming on Twitch.TV")
            cts = True
            return cts
        else:
            print(streamer + " is offline on Twitch.TV")
            cts = False
            return cts
    except Exception as e:
        print(e)
    return
def CheckYouTubeStream(streamer, subtype):
    cys = None
    body = ""
    chan_name = ""
    try: #hqdefault_live.jpg
        if subtype == "0": #0 = channel, 1 = vanity
            response = requests.get("https://www.youtube.com/channel/" + streamer)
            body = response.text
            tree = html.fromstring(response.content) 
            chan_name = tree.xpath('/html/body/title')[0].text
            setYTName(chan_name[0:-10])
        else:
            response = requests.get("https://www.youtube.com/c/" + streamer)
            body = response.text
            tree = html.fromstring(response.content) 
            chan_name = tree.xpath('/html/body/title')[0].text
            setYTName(chan_name[0:-10])
        if "hqdefault_live.jpg" in body:
            print("Channel Name: " + yt_name + " - " + streamer + " is live streaming on YouTube.com")
            cys = True
            return cys
        else:
            print("Channel Name: " + yt_name + " - " + streamer + " is offline on YouTube.com")
            cys = False
            return cys
    except Exception as e:
        print(e)
    return
removeStatusFiles()
TwitchStreamerList('streamers_twitch.txt')
YouTubeStreamerList('streamers_youtube.txt')
