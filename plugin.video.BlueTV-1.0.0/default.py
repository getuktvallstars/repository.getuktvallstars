# -*- coding: utf-8 -*-
#------------------------------------------------------------
# kodi tutorials from the group
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: lesismore
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.BlueTV'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCU2PacFf99vhb3hNiYDmxww"
YOUTUBE_CHANNEL_ID_2 = "UCeXlURDsE_zyn3fYNy3Uwyg"
YOUTUBE_CHANNEL_ID_3 = "UCb51e53V1Cq3jx8_EFYflWA"
YOUTUBE_CHANNEL_ID_4 = "UCmRtuRpYo_PnIt0BAQqPsxg"
YOUTUBE_CHANNEL_ID_5 = "UCRI59AxvnZSCYPhtuFfGLOQ"
YOUTUBE_CHANNEL_ID_6 = "UC4i_9WvfPRTuRWEaWyfKuFw"
YOUTUBE_CHANNEL_ID_7 = "UCNAf1k0yIjyGu3k9BwAg3lg"



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
        title="Chelsea FC Channel Videos",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-_-grPaix4ZQ/AAAAAAAAAAI/AAAAAAAAAAA/kCxr3PPmMu8/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chelsea Fans Channel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-kSD29QrBaVA/AAAAAAAAAAI/AAAAAAAAAAA/BtAwJy4qodE/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="100 Percent Chelsea",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-we76oDTWMFw/AAAAAAAAAAI/AAAAAAAAAAA/ZjRBMscw5Ik/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chelsea Retro TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-UxhomE72XW4/AAAAAAAAAAI/AAAAAAAAAAA/Sy94_CTSBps/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Football Replay",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-Q-Is3H69dyA/AAAAAAAAAAI/AAAAAAAAAAA/E1B4aNW0v4I/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="BT Sport",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-zLLqi4rqrBw/AAAAAAAAAAI/AAAAAAAAAAA/_73BhShNrT4/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sky Sports Football",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-s4KkHI3fkVA/AAAAAAAAAAI/AAAAAAAAAAA/OSRu4_xgevM/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    
run()
