from urllib.request import urlopen
StreamerStatus = []
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
        with open("streamers_twitch_status.txt","a") as file:
            file.write("[Twitch Streamer Status]\n")
            for row in StreamerStatus:
                s = "".join(map(str, row))
                file.write(s+'\n')
    except Exception as e:
        print(e)
    return
def YouTubeStreamerList(file_path):
    if file_path == '' or None:
        print("Error: No streamer list selected.")
        return
    try:
        textData=open(file_path,"r")
        list1 = textData.read().split('\n')
        for i in range(len(list1)):
            streamer = list1[i]
            streamerX = streamer.split(',')
            X = CheckYouTubeStream(streamerX[0], streamerX[1])
            if X == True:
                StreamerStatus.append(streamerX[0] + " : ONLINE")
            else:
                StreamerStatus.append(streamerX[0] + " : OFFLINE")
        with open("streamers_youtube_status.txt","a") as file:
            file.write("[YouTube Streamer Status]\n")
            for row in StreamerStatus:
                s = "".join(map(str, row))
                file.write(s+'\n')
    except Exception as e:
        print(e)
    return
def CheckTwitchStream(streamer):
    cts = None
    try:
        response = urlopen("https://twitch.tv/" + streamer)
        body = response.read()
        decoded_body = body.decode("utf-8")
        response.close()
        if "isLiveBroadcast" in decoded_body:
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
    try: #hqdefault_live.jpg
        if subtype == "0": #0 = channel, 1 = vanity
            response = urlopen("https://www.youtube.com/channel/" + streamer)
            body = response.read()
            decoded_body = body.decode("utf-8")
            response.close()
        else:
            response = urlopen("https://www.youtube.com/c/" + streamer)
            body = response.read()
            decoded_body = body.decode("utf-8")
            response.close()
        if "hqdefault_live.jpg" in decoded_body:
            print(streamer + " is live streaming on YouTube.com")
            cys = True
            return cys
        else:
            print(streamer + " is offline on YouTube.com")
            cys = False
            return cys
    except Exception as e:
        print(e)
    return
TwitchStreamerList('streamers_twitch.txt')
YouTubeStreamerList('streamers_youtube.txt')
