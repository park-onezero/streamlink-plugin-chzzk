# encoding: utf-8
import re
import requests
from streamlink.plugin import Plugin, pluginmatcher
from streamlink.stream import HLSStream 
import json

@pluginmatcher(re.compile(
    r'(http)?(s)?(://)?(www\.)?chzzk.naver.com/live/(?P<channel>[^/]+)'
))
class Chzzk(Plugin): 

    def _get_streams(self):  
        channel = self.match['channel']

        headers = {  
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Whale/3.23.214.17 Safari/537.36",
        }
        
        live_data = requests.get(url='https://api.chzzk.naver.com/service/v1/channels/{}/live-detail'.format(channel), headers=headers).json()
        live_content = live_data["content"]

        self.id = live_content["liveId"];
        self.author = live_content["channel"]["channelName"]
        self.category = live_content["liveCategory"]
        self.title = live_content["liveTitle"].replace("\n", " ").strip()

        print(self.title)

        playback_data = json.loads(live_content["livePlaybackJson"])
 
        variant = HLSStream.parse_variant_playlist(self.session, list(map(lambda x:x['path'],playback_data['media'])) [0]) 
        for q, s in list(variant.items()): 
            yield q, s

__plugin__ = Chzzk
