# -*- coding: utf-8 -*-


# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Serendipity
# Author: Gracie


import os
import xbmc        
import xbmcaddon    
import xbmcplugin   
import re 
import xbmcgui
from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File


addon_id     = xbmcaddon.Addon().getAddonInfo('id') 

BASE  = "plugin://plugin.video.youtube/playlist/"
		  


YOUTUBE_CHANNEL_ID_1 = "PL991qh8jWvSffZfV4lwUypJPYf5mahFUq"
YOUTUBE_CHANNEL_ID_2 = "PL991qh8jWvSevvIHrhs3MGAiuCBiN2NFf"
YOUTUBE_CHANNEL_ID_3 = "PL991qh8jWvSeNLu12H9jyBiUEVpANsUw8"
YOUTUBE_CHANNEL_ID_4 = "PL991qh8jWvSfb1wD7vICOog2lhqO2_TJR"
YOUTUBE_CHANNEL_ID_5 = "PL991qh8jWvSdM-kydtQh5X9-nUXUgu8b_"
YOUTUBE_CHANNEL_ID_6 = "PL9lDxmOVB4z4g2aeA9Em8lSK3TS-QBn0X"
YOUTUBE_CHANNEL_ID_7 = "PL991qh8jWvSfI5BHnlj8wizl_76tPvpth"
YOUTUBE_CHANNEL_ID_8 = "PL991qh8jWvSd3LdC9aE80mUYzL6zqYE6B"
YOUTUBE_CHANNEL_ID_9 = "PL991qh8jWvSdH5wMZBboRoJNZFK7KSaQ7"
YOUTUBE_CHANNEL_ID_10 ="PL991qh8jWvSenrISwIS7Y8Yp0sNQVH5iV"
YOUTUBE_CHANNEL_ID_11 ="PL991qh8jWvSd2_guNbJmF2DSKhq1rvlDm"

@route(mode='main_menu')
def Main_Menu():

	Add_Dir( 
        name="Kung Fu", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://fthmb.tqn.com/kpIAgag59hxXJBLjlT5c2w4kSCU=/400x0/about/GettyImages-asi03152-591992385f9b586470fa035b.jpg")

	Add_Dir( 
        name="Horror", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdh4bFkDA27w1EtdTO37YcfeEeHhOEaGe8i5ZBXJJnarzFmUko")
		
	Add_Dir( 
		name="Fitness", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpzgSGnTcjUZ9ljQwjHrr60ayaksluX_B0VpgXn8OHSDPrnla4")
		
	Add_Dir( 
		name="Mental Health", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoqto69CSMYynPKYmSe5iHilHaTC0d3qkPSocCB5991R9VIHLT")
		
	Add_Dir( 
		name="Documentary", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRj1GH5V4-s5F8ywDosuBhEC_zz_PvnlRnZXHxeNyU8LLp3y3d2yw")	
	
	Add_Dir( 
        name="True Crime", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3-iwpcvykirtgGvb3vJ_T4MW-yBF0nHNTo_LFgFfdGB-PGehusw")
	
	Add_Dir( 
        name="History", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="https://news.artnet.com/app/news-upload/2015/05/palmyra-256x256.jpg")
	
	Add_Dir( 
        name="Geography", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="https://www.shareicon.net/data/256x256/2016/12/30/866938_globe_512x512.png")
	
	Add_Dir( 
        name="Science", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="https://upload.wikimedia.org/wikipedia/commons/f/fb/Icon_Atomic_256x256.png")
		
	Add_Dir( 
        name="Anime", url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1IoUnbtsJnnu41VXvbcHxEUPHtNDnSB9F74AAzKcejmwOnwgM")
		
	Add_Dir( 
        name="Transportation", url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,
        icon="https://news.artnet.com/app/news-upload/2014/08/vintage-cars-speed-read-256x256.jpg")
		
		

@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()

	
@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)



if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))