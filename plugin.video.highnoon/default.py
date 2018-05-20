# -*- coding: utf-8 -*-




# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: High Noon
# Author: Gracie


import os           
import xbmc      
import xbmcaddon    
import xbmcplugin   





from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File




debug        = Addon_Setting(setting='debug')      
addon_id     = xbmcaddon.Addon().getAddonInfo('id') 

BASE  = "plugin://plugin.video.youtube/playlist/"


YOUTUBE_CHANNEL_ID_1 = "PL991qh8jWvScbUNtSVUtjDFbqpxe7zxqc"
YOUTUBE_CHANNEL_ID_2 = "PL991qh8jWvSer-8aaWr0gkcwjCzF5uEfP"
YOUTUBE_CHANNEL_ID_3 = "PL991qh8jWvSesy0xYChBRH8W3Lcirpm4_"
YOUTUBE_CHANNEL_ID_4 = "PL991qh8jWvScZqTN9hk0PiSiKw7HEgbV0"
YOUTUBE_CHANNEL_ID_5 = "PL991qh8jWvSccaah15PiLHszclIzHmG-W"
YOUTUBE_CHANNEL_ID_7 = "PL991qh8jWvScy5AhavvdEEh_XM-cAT5V3"


@route(mode='main_menu')
def Main_Menu():

	Add_Dir( 
        name="Western Movies", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1uMq6alaJOfXQQaGQtmMqcuaze3NqHn0k5UGCXQRq5jFFVggvtw")

	Add_Dir( 
        name="Cowboys and Indians", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiXE5gw6ZeFH1jW12DW-WwLJSHwwp0FH7C5r1wY9VbdxR0NXgEDg")
		
	Add_Dir( 
		name="Wild West Documentaries", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_jqG5K_SfDympmneCfX7sFmutlf7nxfYCZYO4CRCJlMAlcCGx")
		
	Add_Dir( 
		name="Country Classic Music", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRy85p8CCcXPS945C_eUZBa2t7-0jqgKLJH4aqrbm50lcbLx7dZAw")
		
	Add_Dir( 
		name="Western Audio Books", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTju0-8cmPQLwW64T2gZKeylLdwqdXSjaoXjdcKy4uXeKhDTGfWTA")	
	
	Add_Dir( 
        name="Bonanza Episodes", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRP76cDyF_FCLzOWLWXiKuETSONFO1E-jJOQQi9RMefI22yUIuGYQ")
	

@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()

	
@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)




if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))