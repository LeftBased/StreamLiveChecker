from urllib.request import urlopen
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
                CheckTwitchStream(streamer)
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
