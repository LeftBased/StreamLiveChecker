from urllib.request import urlopen

def CheckTwitchStream(streamer):
    response = urlopen("https://m.twitch.tv/" + streamer)
    body = response.read()
    decoded_body = body.decode("utf-8")
    response.close()
    cts = None
    if "isLiveBroadcast" in decoded_body:
        print(streamer + " is live streaming")
        cts = True #set cts as true.
    else:
        print(streamer + " is not live streaming")
        cts = False
    return cts
    
CheckTwitchStream('merlinsgoat')
CheckTwitchStream('amouranth')
CheckTwitchStream('ninja')
