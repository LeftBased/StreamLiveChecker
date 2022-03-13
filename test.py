from urllib.request import urlopen
StreamerStatus = []
def streamerList(file_path, stream_platform):
    if stream_platform == '' or None:
        print("Error: No stream platform defined.")
        return
    if file_path == '' or None:
        print("Error: No streamer list selected.")
        return
    try:
        textData=open(file_path,"r")
        list1 = textData.read().split('\n')
        for i in range(len(list1)):
            streamer = list1[i]
            if stream_platform == 0:
                X = CheckTwitchStream(streamer)
                if X == True:
                    StreamerStatus.append(streamer + " : ONLINE")
                else:
                    StreamerStatus.append(streamer + " : OFFLINE")
        with open("Streamer_Status.txt","a") as file:
            file.write("[Twitch Streamer Status]\n")
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
            print(streamer + " is not live streaming on Twitch.TV")
            cts = False
            return cts
    except Exception as e:
        print(e)
    return
streamerList('streamers.txt', 0)
