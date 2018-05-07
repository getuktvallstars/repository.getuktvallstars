# -*- coding: utf-8 -*-


import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.feedyourmind'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCzTfKoeKcQirS7wjMPZc8Lw" 				#Biography
YOUTUBE_CHANNEL_ID_2 = "UC88lvyJe7aHZmcvzvubDFRg" 				#History
YOUTUBE_CHANNEL_ID_3 = "UCaUQ3WmCPBenH6we_sXu22Q" 				#Wildlife
YOUTUBE_CHANNEL_ID_4 = "UCjqDr-twV-kqnbDJ1k6Bqnw" 				#Art
YOUTUBE_CHANNEL_ID_5 = "UCppyk_vc2LR3HEB5l1GvE9g" 	            #Battlefield
YOUTUBE_CHANNEL_ID_6 = "PLtUeiZkcnkGybHUkD47XK7cta2rAOoNeI" 	#Crime PL
YOUTUBE_CHANNEL_ID_7 = "UCU1mhOq8nSpcOw98qObBfhw" 				#Disaster
YOUTUBE_CHANNEL_ID_8 = "PLImletmkNNsln-P3wkJFx9bnv2HothoFV" 	#Drugs PL
YOUTUBE_CHANNEL_ID_9 = "PLqduaEP5i4pcH1S33OVxp0aBu4Wofd5GH" 	#Mafia
YOUTUBE_CHANNEL_ID_10 = "UCfj9TK1mhbIWpcmP5rcIfYQ" 				#Paranormal
YOUTUBE_CHANNEL_ID_11 = "UCqjiWBNiTpk03Qf1LEivMhg" 				#Prison
YOUTUBE_CHANNEL_ID_12 = "PL5z9aEiERjy7yawNMpsLb75Yp53iUw0O9" 	#Science PL
YOUTUBE_CHANNEL_ID_13 = "PLmkjUS2UqPAOQn25fI5g9dCaQ0N-Vz758" 	#UFO

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
        title="Art",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Battlefield",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Biography",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Crime",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Disaster",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )
		
			
		
    plugintools.add_item( 
        #action="", 
        title="Drugs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )	
		
		
    plugintools.add_item( 
        #action="", 
        title="History",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )
		

    plugintools.add_item( 
        #action="", 
        title="Mafia",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Paranormal",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )		
		

    plugintools.add_item( 
        #action="", 
        title="Prison",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )		


    plugintools.add_item( 
        #action="", 
        title="Science",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )		

		
    plugintools.add_item( 
        #action="", 
        title="Wildlife",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )
		
		
    plugintools.add_item( 
        #action="", 
        title="UFO",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://dmitsoftware.in/wp-content/uploads/2017/04/know-your-brain-fimg-256x256.jpg",
		fanart="https://images6.alphacoders.com/681/681840.jpg",
        folder=True )				


		
run()
