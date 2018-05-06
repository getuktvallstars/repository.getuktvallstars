# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by: SkymashiTV
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.learnlanguageallstars'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCydVvh3Wg4VPvllLHFoe5_A" 	#Learn Spanish
YOUTUBE_CHANNEL_ID_2 = "UCHk14TRSD33vAyx5xKzpcnw" 	#Learn French
YOUTUBE_CHANNEL_ID_3 = "UCb5faEH1hEiLaT_aGMBWeBg" 	#Learn Italian
YOUTUBE_CHANNEL_ID_4 = "UCgF23VqDjioQVQqHUzzSe9g"	#Learn Portuguese
YOUTUBE_CHANNEL_ID_5 = "UCCNoD0ZtJ_uJgTtQeoVZhgw"	#Learn Swedish
YOUTUBE_CHANNEL_ID_6 = "UCY0BCa9cKhn-V1W52ALrR5Q"	#Learn Dutch
YOUTUBE_CHANNEL_ID_7 = "UCEul3aIysbBBqaRaVDFKUrg"	#Learn Filipino
YOUTUBE_CHANNEL_ID_8 = "UCTobWZV_HWGSoaRrhHyrJ-A"	#Learn German
YOUTUBE_CHANNEL_ID_9 = "UC0ox9NuTHYeRys63yZpBFuA"	#Learn Japanese
YOUTUBE_CHANNEL_ID_10 = "UCJhnlRY-oKpanPGSvL8Ml8Q"	#Learn Chinese


# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Learn Spanish",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/spain-flag-heart-3d-medium.png?raw=true",
		fanart="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/spain-flag-xl.png?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Learn French",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/france-flag-heart-3d-medium.png?raw=true",
		fanart="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/france-flag-xl.png?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Learn Italian",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/italy-flag-heart-3d-medium.png?raw=true",
		fanart="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/italy-flag-xl.png?raw=true",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Learn Portuguese",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/portugal-flag-heart-3d-medium.png?raw=true",
		fanart="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/portugal-flag-xl.png?raw=true",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Learn Swedish",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/sweden-flag-heart-3d-medium.png?raw=true",
		fanart="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/sweden-flag-xl.png?raw=true",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Learn Dutch",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/netherlands-flag-heart-3d-medium.png?raw=true",
		fanart="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/netherlands-flag-xl.png?raw=true",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Learn Filipino",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/philippines-flag-heart-3d-medium.png?raw=true",
		fanart="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/philippines-flag-xl.png?raw=true",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Learn German",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/germany-flag-heart-3d-medium.png?raw=true",
		fanart="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/germany-flag-xl.png?raw=true",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Learn Japanese",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/japan-flag-heart-3d-medium.png?raw=true",
		fanart="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/japan-flag-xl.png?raw=true",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Learn Chinese",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/china-flag-heart-3d-medium.png?raw=true",
		fanart="https://github.com/getuktvallstars/repository.getuktvallstars/blob/master/language%20addon%20images/china-flag-xl.png?raw=true",
        folder=True )

		
run()
