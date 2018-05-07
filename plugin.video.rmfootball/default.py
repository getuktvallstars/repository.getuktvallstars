# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Retromania on YouTube by s2law
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: s2law
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.rmfootball'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLpODz2ZE55fAefFqsTCi45xhkkkDAWT7_"
YOUTUBE_CHANNEL_ID_2 = "PLpODz2ZE55fA_x6J_uFi1aM003crbo62F"
YOUTUBE_CHANNEL_ID_3 = "PLpODz2ZE55fA0UupUml8mhHgiXUiemN9Q"
YOUTUBE_CHANNEL_ID_4 = "PLpODz2ZE55fBhvdS5OnaEw58D94culmV7"
YOUTUBE_CHANNEL_ID_5 = "PLpODz2ZE55fBLUS9IfuZMpaZlV-svyV5c"
YOUTUBE_CHANNEL_ID_6 = "PLpODz2ZE55fCw51AnBINaTJ6q1TSO9-eq"
YOUTUBE_CHANNEL_ID_7 = "PLpODz2ZE55fB1DIkqRvN1ceLRCDcCm37q"
YOUTUBE_CHANNEL_ID_8 = "PLpODz2ZE55fAln6SWpWrQN656p_NPmpxD"
YOUTUBE_CHANNEL_ID_9 = "PLpODz2ZE55fAkqaIBpbLGhY68ACiqZ9xA"
YOUTUBE_CHANNEL_ID_10 = "PLpODz2ZE55fAm-e-A0mwqp9CKvkEnKyL8"
YOUTUBE_CHANNEL_ID_11 = "PLpODz2ZE55fARPbP1gRvw00d9Ou8cZySt"
YOUTUBE_CHANNEL_ID_12 = "PLpODz2ZE55fCZfffeEyfdLbu5ri6KHl7G"
YOUTUBE_CHANNEL_ID_13 = "PLpODz2ZE55fD0ax0NJFXeky3nrcJZcYgO"
YOUTUBE_CHANNEL_ID_14 = "PLpODz2ZE55fCYARZqi7uPGVC1chK6Q82E"
YOUTUBE_CHANNEL_ID_15 = "PLpODz2ZE55fD-zQRZum-ePHFiIorAv1tm"
YOUTUBE_CHANNEL_ID_16 = "PLpODz2ZE55fBa8G7V8b_rRWnHONR79CZ2"
YOUTUBE_CHANNEL_ID_17 = "PLpODz2ZE55fCWByOjqULwJPT5QaIs-Zbr"
YOUTUBE_CHANNEL_ID_18 = "PLpODz2ZE55fCehpABAxw19q0SIArNhyjo"
YOUTUBE_CHANNEL_ID_19 = "PLpODz2ZE55fBfx-YDyPBWQxce_QB_yc5Y"
YOUTUBE_CHANNEL_ID_20 = "PLpODz2ZE55fAeh_gqX1cVxX9E9NSgQk3c"
YOUTUBE_CHANNEL_ID_21 = "PLpODz2ZE55fDB-KYqoAEPuoU_TEtuwBMz"
YOUTUBE_CHANNEL_ID_22 = "PLpODz2ZE55fDZwD18RWJXrXpqFFTjaRTX"
YOUTUBE_CHANNEL_ID_23 = "PLpODz2ZE55fCYtS1oQVebKcWwTrq1K8WH"
YOUTUBE_CHANNEL_ID_24 = "PLpODz2ZE55fD9cZ4hVANCPZgHxGaRfkWL"
YOUTUBE_CHANNEL_ID_25 = "PLpODz2ZE55fBq6yeOFQqR3w--YWcXnoxU"
YOUTUBE_CHANNEL_ID_26 = "PLpODz2ZE55fArpp0nLrv39UQAuSS_8VSG"
YOUTUBE_CHANNEL_ID_27 = "PLpODz2ZE55fCS8sVLrAdrYdUj7hX4geRF"

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
        title="Home of RetroMania",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item(
        #action="",
        title="Greatest Moments",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\greatest.png",
        folder=True )
        
    plugintools.add_item(
        #action="",
        title="Documentaries",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\docs.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Goals - Volleys",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\olleys.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Goals - Bicycle Kicks",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\overhead.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Goals - Team Effort",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\eam.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Goals - Lobs & Chips",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\lob.png",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Goals - Free Kicks",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\kick.png",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Goals - Long Shots",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\longshot.png",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Skills - Tricks",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\skills.png",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Skills - Passes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\pass.png",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Skills - Special Players",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\legends.png",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Greatest Saves & Tackles",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\keeper.png",
        folder=True )
        
    plugintools.add_item(
        #action="",
        title="Funny Moments",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\unny.png",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Goal Keeper Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\kfails.png",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Referee Fails",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\effails.png",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Worst Misses",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\miss.png",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Respect & Emotion",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\espect.png",
        folder=True )
        
    plugintools.add_item(
        #action="",
        title="Fouls & Fights",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\ouls.png",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Anthems",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\hems.png",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Funny Chants",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\chants.png",
        folder=True )
        
    plugintools.add_item(
        #action="",
        title="Football Songs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\songs.png",
        folder=True )
        
    plugintools.add_item(
        #action="",
        title="Soccer AM - Showboat",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\showboat.png",
        folder=True )
        
    plugintools.add_item(
        #action="",
        title="Soccer AM - You Know The Drill",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\drill.png",
        folder=True )
        
    plugintools.add_item(
        #action="",
        title="Soccer AM - Crossbar Challenge",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\cross.png",
        folder=True )
        
    plugintools.add_item(
        #action="",
        title="Soccer AM - Tubes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\ubes.png",
        folder=True )
        
    plugintools.add_item(
        #action="",
        title="Soccer AM - 3rd Eye",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="special://home/addons\plugin.video.rmfootball\media\eye.png",
        folder=True )
run()
