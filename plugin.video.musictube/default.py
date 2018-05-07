# -*- coding: utf-8 -*-


import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.musictube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI" 	#Trending Now
YOUTUBE_CHANNEL_ID_2 = "PLFgquLnL59akA2PflFpeQG9L01VFg90wS" 	#Latest Music Videos
YOUTUBE_CHANNEL_ID_3 = "PLDcnymzs18LWrKzHmzrGH1JzLBqrHi3xQ" 	#Pop Music
YOUTUBE_CHANNEL_ID_4 = "PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG" 	#Top 50 Songs This Week & Top 100 Hits of 2017-2018
YOUTUBE_CHANNEL_ID_5 = "PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj" 	#POP Music Playlist 2017 (POP Songs of All Time)
YOUTUBE_CHANNEL_ID_6 = "PL3oW2tjiIxvQ1BZS58qtot3-p-lD32oWT" 	#Music 2017-2018: Playlist of Popular Songs (New Hits)
YOUTUBE_CHANNEL_ID_7 = "PL55713C70BA91BD6E"                  	#Billboard Top Songs 2017
YOUTUBE_CHANNEL_ID_8 = "PLvFYFNbi-IBFeP5ALr50hoOmKiYRMvzUq" 	#Best New Songs
YOUTUBE_CHANNEL_ID_9 = "PLFgquLnL59amTdtEvjQOSlQozduow4qet" 	#Alternative Music
YOUTUBE_CHANNEL_ID_10 = "PLH6pfBXQXHEC2uDmDy5oi3tHW6X8kZ2Jo" 	#Hip-Hop Music
YOUTUBE_CHANNEL_ID_11 = "PLr8RdoI29cXIlkmTAQDgOuwBhDh3yJDBQ" 	#Pop Rock Music
YOUTUBE_CHANNEL_ID_12 = "PLhInz4M-OzRUsuBj8wF6383E7zm2dJfqZ" 	#House Music
YOUTUBE_CHANNEL_ID_13 = "PLYAYp5OI4lRLf_oZapf5T5RUZeUcF9eRO" 	#Reggae Music
YOUTUBE_CHANNEL_ID_14 = "PL9NMEBQcQqlzwlwLWRz5DMowimCk88FJk" 	#Hard Rock Music
YOUTUBE_CHANNEL_ID_15 = "PLFgquLnL59amVPzpNpN5bNLcZCld7JfI8" 	#Indie Music
YOUTUBE_CHANNEL_ID_16 = "PLFgquLnL59akYpPgfxzsw5jlPZ9R6HewT" 	#Dance/EDM Music
YOUTUBE_CHANNEL_ID_17 = "PLFgquLnL59amI45Go39kM7ha2evwjOxzs" 	#Coutry Music
YOUTUBE_CHANNEL_ID_18 = "PLFgquLnL59annf9DmPBRYyrq7NE9I4vhX" 	#Christian Music
YOUTUBE_CHANNEL_ID_19 = "PLFgquLnL59akXPIHrEZci0oouw4dArE0D" 	#Electronic Music
YOUTUBE_CHANNEL_ID_20 = "PLFgquLnL59anIJu29gI8F5j5jZwp9Fo7t" 	#Metal Music

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
        title="Trending Now",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Latest Additions",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )


    plugintools.add_item( 
        #action="", 
        title="Billboard Top Songs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Alternative Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Hip-Hop Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pop Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pop Rock Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="House Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )
				
    plugintools.add_item( 
        #action="", 
        title="Reggae Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )
				
    plugintools.add_item( 
        #action="", 
        title="Hard Rock Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Indie Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Dance/EDM Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Coutry Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Christian Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Electronic Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Metal Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="http://findicons.com/files/icons/1580/devine_icons_part_2/256/cd_music.png",
		fanart="http://www.freeportnewsnetwork.com/wp-content/uploads/2016/12/music-07.jpg",
        folder=True )
		

		
run()
