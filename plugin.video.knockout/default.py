# -*- coding: utf-8 -*-


# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Knock Out 0.0.1
# Author: Gracie242

import os           
import xbmc        
import xbmcaddon 
import xbmcplugin   
import re     
import xbmcgui      

from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File



debug        = Addon_Setting(setting='debug')    
addon_id     = xbmcaddon.Addon().getAddonInfo('id') 


BASE  = "plugin://plugin.video.youtube/playlist/"


YOUTUBE_CHANNEL_ID_1 = "PLxcn4s0qfjOpheJmWV1E6RUlRj986k9EA"
YOUTUBE_CHANNEL_ID_2 = "PLxcn4s0qfjOq58UM_CC7GKuTsf3sYYw3e"
YOUTUBE_CHANNEL_ID_3 = "PLxcn4s0qfjOoF5DdFBJwOxbBu4urqAsA2"
YOUTUBE_CHANNEL_ID_4 = "PLxcn4s0qfjOoNCd-eimkVpZUCjV5Tnz2r"
YOUTUBE_CHANNEL_ID_5 = "PLxcn4s0qfjOrFivNVh_TqtOa-wsHOx6BM"
YOUTUBE_CHANNEL_ID_6 = "PLxcn4s0qfjOo4yYjePk--YdFZNggkkNtY"
YOUTUBE_CHANNEL_ID_7 = "PLxcn4s0qfjOpTX8-5Fw_QJoD3899jhu5s"
YOUTUBE_CHANNEL_ID_8 = "PLxcn4s0qfjOpxYr2s7EXLYzPXM0ENKccd"
YOUTUBE_CHANNEL_ID_9 = "PLxcn4s0qfjOqd5AAk28p-u4VfSinqqbat"
YOUTUBE_CHANNEL_ID_10 = "PLxcn4s0qfjOql96tFsDujtV0oBPvDwhGg"
YOUTUBE_CHANNEL_ID_11 = "PLxcn4s0qfjOopUgHQpCyZRL1iS-fsI6U3"
YOUTUBE_CHANNEL_ID_12 = "PLxcn4s0qfjOr47IvMvjzh5uVksxHgyGq6"
YOUTUBE_CHANNEL_ID_13 = "PLxcn4s0qfjOpM3BOwH65yYv3z7LBUQkHd"
YOUTUBE_CHANNEL_ID_14 = "PLxcn4s0qfjOpwFBNuNTyt997RjM9LRigO"
YOUTUBE_CHANNEL_ID_15 = "PLxcn4s0qfjOrNQYuJOB63dwzQ0dy9fcmj"
YOUTUBE_CHANNEL_ID_16 = "PLxcn4s0qfjOokCCKRo09LuOWs_3ReWo7T"
YOUTUBE_CHANNEL_ID_17 = "PLxcn4s0qfjOoJHMibv48FU8tq48Nkg1rg"
YOUTUBE_CHANNEL_ID_18 = "PLxcn4s0qfjOp_mwGjIG_rRiL-6Dkj08wM"
YOUTUBE_CHANNEL_ID_19 = "PLxcn4s0qfjOqwtAjHfzbAQ2oAlF2TUtdJ"
YOUTUBE_CHANNEL_ID_20 = "PLxcn4s0qfjOpFW1QGbpeSbrCj-WL1lDQA "
YOUTUBE_CHANNEL_ID_21 = "PLxcn4s0qfjOrt4qmh9zv35DM_ar504MkG"
YOUTUBE_CHANNEL_ID_22 = "PLxcn4s0qfjOrmsEx5RYo6qptBww_bX-wT"
YOUTUBE_CHANNEL_ID_23 = "PLxcn4s0qfjOqKCYzQT-YYYp2Umo_paWs1"
YOUTUBE_CHANNEL_ID_24 = "PLxcn4s0qfjOqugU0BukAMH-TuEE7GqGLO"
YOUTUBE_CHANNEL_ID_25 = "PLxcn4s0qfjOofdViqIb8HGP3QpYhIrQCa"
YOUTUBE_CHANNEL_ID_26 = "PLxcn4s0qfjOqUUQ_0CjL6K8xTK7O0zfBN"
YOUTUBE_CHANNEL_ID_27 = "PLxcn4s0qfjOrJSuljQWS1s--XEoN46h9R"
YOUTUBE_CHANNEL_ID_28 = "PLxcn4s0qfjOp-f-xMP7kXK9GB23T153hI"
YOUTUBE_CHANNEL_ID_29 = "PLxcn4s0qfjOqQ2PThxCDbdEcThQt0-pps"
YOUTUBE_CHANNEL_ID_30 = "PLxcn4s0qfjOrhF5_-UokkgXYysa8k2KCX"
YOUTUBE_CHANNEL_ID_31 = "PLxcn4s0qfjOr_0uUR7zj2agTlYNOKzuNE"
YOUTUBE_CHANNEL_ID_32 = "PLxcn4s0qfjOoXrzbUT31KacbQUBm-n2af"
YOUTUBE_CHANNEL_ID_33 = "PLxcn4s0qfjOo-8jWOn9DZ9suqyEZpw5CP"
YOUTUBE_CHANNEL_ID_34 = "PLxcn4s0qfjOo0lWcHfd7MN6QNIhfROL0s"
YOUTUBE_CHANNEL_ID_35 = "PLxcn4s0qfjOr8K5nGJ5e5QbFSwrPlgAkv"
YOUTUBE_CHANNEL_ID_36 = "PLxcn4s0qfjOo_ui2P7anIyChduOvN6cke"
YOUTUBE_CHANNEL_ID_37 = "PLxcn4s0qfjOoT4p-7d5i_xozDH-pQYSx8"
YOUTUBE_CHANNEL_ID_38 = "PLxcn4s0qfjOrrI0AJAf5VOwKEbTL5iN9Q"
YOUTUBE_CHANNEL_ID_39 = "PLxcn4s0qfjOoCFgK-odVaGYDy_WHQRXD5"
YOUTUBE_CHANNEL_ID_40 = "PLxcn4s0qfjOqWQRie7ON7ZnqIOvz9KdC4"
YOUTUBE_CHANNEL_ID_41 = "PLxcn4s0qfjOod2uv35In-laU8e1W7-ZlN"
YOUTUBE_CHANNEL_ID_42 = "PLxcn4s0qfjOoCsX5y7o2n0f2Hvau6iswn"
YOUTUBE_CHANNEL_ID_43 = "PLxcn4s0qfjOrwTfwXX8uzJ1H16vZXatt5"
YOUTUBE_CHANNEL_ID_44 = "PLxcn4s0qfjOoNoJIyLc8DLrHVkyf3y9T5"
YOUTUBE_CHANNEL_ID_45 = "PLxcn4s0qfjOr_3mZse_AYCl43cWShlRji"
YOUTUBE_CHANNEL_ID_46 = "PLxcn4s0qfjOqWz5EkSNPJstmCYKMfwb7B"
YOUTUBE_CHANNEL_ID_47 = "PLxcn4s0qfjOrYJYQ-Xkrfh1Xi995wq_mf"
YOUTUBE_CHANNEL_ID_48 = "PLxcn4s0qfjOqkGlG9QWEvBf96xFDI5kNA"
YOUTUBE_CHANNEL_ID_49 = "PLxcn4s0qfjOrxiMqSiKkFo7yjQPy2QKOn"
YOUTUBE_CHANNEL_ID_50 = "PLxcn4s0qfjOryMK_iRCy3ZRxmDvCfpLb3"


@route(mode='main_menu')
def Main_Menu():
	Add_Dir( 
        name="Sugar Ray Robinson 175-196-2", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT96Su-N0VVxRy0519XVis0HjuNMujzhMZ1uUazRSglGQMQAZLyiA")

	Add_Dir( 
		name="Muhammad Ali/Cassius Clay 56-5",url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
		icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSake2NtLgwytGpSqfleBBpoiXrWXnclR-vcZDTvgs-4tvKr1cIw")
	
	Add_Dir( 
        name="Joe Louis 68-3", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTP8pBXO9NpY8noZ5MxqRoruI7XKk6way2aL5p-sO-w1Ry8Ms_2")
	
	Add_Dir( 
        name="Rocky Marciano 49-0", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsKTDvH5o5g6MBJPXSqy6R5Baz7hXsfAVnFbyOcGDCDGRx-Sww")
	
	Add_Dir( 
        name="Henry Armstrong 151-21-9", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdf-ufrG8U7k8B79sR54MVY7yna-_L2BNzNhPvaSCDwvpFNCUQ")
	
	Add_Dir( 
        name="Sugar Ray Leonard 36-3-1", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbonsa3e3BayPpL6asBFdD11tXYSVuH17kbHUPcjlhc-9kC3Tx")
	
	Add_Dir( 
        name="Roberto Duran 103-16", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9CY0XYeP-bw2fCcAaw4m2lTVof1XBPtQ26-zLTF6jBRgkzN46")
	
	Add_Dir( 
        name="Mike Tyson 50-6-0-2 ", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZM2J0F3Qwe98ZOgvf79PTCqhwwAcsglxQ2AjG41gmMyAh-EO2")
	
	Add_Dir( 
        name="Jack Dempsey 61-6-8", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8ZISmdeuAIOz4pp6Hqs4fND6cSyxtr_AFBLUAmiEGY3AE-MKIkg")
	
	Add_Dir( 
        name="Jack Johnson 77-13-14", url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoFyrln6fGhd2G8cT39NShU7VjXdBAP1-ut2L6SjsRVWUXUv0IMA")
	
	Add_Dir( 
        name="Sam Langford 167-38-37-3", url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPlwmoUMIz-yVKLANMBK95vj_4R6ih6Fc9bjd9jrsFa9nLL-yZ")
	
	Add_Dir( 
        name="Gene Tunney 61-1-1-1", url=BASE+YOUTUBE_CHANNEL_ID_12+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrljdTvugvcY0ypL8dDELP5WX8jZQVuH0bUKsSXadXS36IRc6yOw")
	
	Add_Dir( 
        name="Archie Moore 183-24-10-1", url=BASE+YOUTUBE_CHANNEL_ID_13+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0tn88vFWHLoYoj_dcc8q1bl1wXpmVSRE7TPfzeUDojLVQdxUIaQ")
	
	Add_Dir( 
        name="Joe Frazier 32-4-1", url=BASE+YOUTUBE_CHANNEL_ID_14+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVXui8aJOay3aKJIdfnnVzNfp0pVBZ676HInt4qLUJFkDB33zD")
	
	Add_Dir( 
        name="George Foreman 76-5", url=BASE+YOUTUBE_CHANNEL_ID_15+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfnXjn2ZNaJJ3aLT__8uMUY_MXG51fZ0GsvcxXpz4S137wYTlHWg")
	
	Add_Dir( 
        name="Willie Pep 229-11-1", url=BASE+YOUTUBE_CHANNEL_ID_16+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZ2cLInrOeuU5luECA_mBqpIqxCIdxu9hByJn3YKbMDU_pAm42")
	
	Add_Dir( 
        name="Joe Gans 158-12-20-6", url=BASE+YOUTUBE_CHANNEL_ID_17+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRP5BIGU_e5_baoYNflCU3fWtod5uO_xY7voxxiGsigJh_1_g-bjg")
	
	Add_Dir( 
        name="Floyd Mayweather Jr. 50-0", url=BASE+YOUTUBE_CHANNEL_ID_18+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWVKEG_rLNAyCx2Ni1xtx-KueX86CAsA6tN0IunVxDBdEh37-e")
	
	Add_Dir( 
        name="Lennox Lewis 41-2-1", url=BASE+YOUTUBE_CHANNEL_ID_19+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReBxU3LMi0yz5_tKb3fUfVDtLEPLosK_RmZ1lYsGP4qyPHeBcz")
	
	Add_Dir( 
        name="Joe Calzaghe 46-0", url=BASE+YOUTUBE_CHANNEL_ID_20+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRP2ZYGldUeIXr4Z9EsQ6X7hupSWKL7979BTghcSQIaJcNLZtIy")
	
	Add_Dir( 
        name="Stanley Ketchel 51-4-4-1", url=BASE+YOUTUBE_CHANNEL_ID_21+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuc3MabpcThEabAAedTzP28PwE5M3WMgt1fAVjP5ASNm9Bhek6")
	
	Add_Dir( 
        name="Harry Greb 261-17-19-1", url=BASE+YOUTUBE_CHANNEL_ID_22+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_Lhu_WN25xnojRMT2Xkd2LrFas-GYqQ2aPbSJIf5ILhpbx-s2oQ")
	
	Add_Dir( 
        name="Jimmy Wilde 132-3-1-5", url=BASE+YOUTUBE_CHANNEL_ID_23+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ91aDDIGyA7JYQcwcHMfWjMTSmcr-v4-kNlrJhFA0oQgEeU-psIw")
	
	Add_Dir( 
        name="Benny Leonard 90-6-1", url=BASE+YOUTUBE_CHANNEL_ID_24+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-KQVjC2KD3KMTEVobWg8aBpgmd9zl-4oOml-8MVRygH7mcJW8KQ")
	
	Add_Dir( 
        name="Julio Cesar Chavez 108-6-2", url=BASE+YOUTUBE_CHANNEL_ID_25+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0_swvYY7tnO_3Z8OkAj_o7ZZUeDDoFOAOehjJXs1GKH8dDpSfRg")
	
	Add_Dir( 
        name="Barney Ross 72-4-3", url=BASE+YOUTUBE_CHANNEL_ID_26+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRV8v3rh3sPOsTTkRYgWjtPIQaDkcFCmXACS-gPMsb9ac82xW7A")
	
	Add_Dir( 
        name="Mickey Walker 131-25-5-2", url=BASE+YOUTUBE_CHANNEL_ID_27+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaE2JQUhY15KMz33Tlv1jkw-ct5qiCcw5FVYhGnJLDMUWCrGyPgQ")
	
	Add_Dir( 
        name="Tony Canzoneri 137-24-10", url=BASE+YOUTUBE_CHANNEL_ID_28+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSH6OaR-nc3rGVOx7RaH5utZXVEWwLDse__sx07lme4FiNGzrsDUg")
	
	Add_Dir( 
        name="Marcel Cerdan 106-4", url=BASE+YOUTUBE_CHANNEL_ID_29+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9FvFrH4Kbzn9_HQ8U6KPDoBKYPM93vmOt9gI6w3kbyHilMYDc9w")
	
	Add_Dir( 
        name="Ezzard Charles 96-25-1", url=BASE+YOUTUBE_CHANNEL_ID_30+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1uu92q0jFX9Bkrn4JaKvyqelqALK-fNaJxiU-JehP5djOZiP6ug")
	
	Add_Dir( 
        name="Sandy Saddler 144-16-2", url=BASE+YOUTUBE_CHANNEL_ID_31+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSncPU2SX7jhSjDQFQAODsevAYqUwZIUjNRCQgrKhbw-nK965F1")
	
	Add_Dir( 
        name="Jimmy McLarnin 62-11-3", url=BASE+YOUTUBE_CHANNEL_ID_32+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThmOQyeLwLxX2P4GBO8vlFJa0j1i1XFHKGQ9F-FEbzD-TWIm41yg")
	
	Add_Dir( 
        name="Terry McGovern 60-4-4", url=BASE+YOUTUBE_CHANNEL_ID_33+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoxzQn9r0a1efzeSTE4kBJw04saP1vGf_82zvOY3XBStY-KX6R")
	
	Add_Dir( 
        name="Emile Griffin 85-24-2-1", url=BASE+YOUTUBE_CHANNEL_ID_34+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXfv3TlI8JVnnRvLmKBwVToVNGOL2P3Otq-IHcQ0pxKsWwwgVL")
	
	Add_Dir( 
        name="Oscar De La Hoya 38-5", url=BASE+YOUTUBE_CHANNEL_ID_35+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbI1dqNdBd3gFC8un12xy26IyoYpQCRt2wMwYVbQm6y4c5j_IL")
	
	Add_Dir( 
        name="Evander Holyfield 4-8-2", url=BASE+YOUTUBE_CHANNEL_ID_36+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrCXkG2IWlCVUxTWuto6ASpeCJ15n-HDsRUvH_YgEsMAYFoT2f")
	
	Add_Dir( 
        name="Marvin Hagler 62-3-2", url=BASE+YOUTUBE_CHANNEL_ID_37+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkm9-_ADaOKTLNbeU4EtNsjaOeySWyjggv-PGdmUQNoki3UCkT1g")
	
	Add_Dir( 
        name="Eder Jofre 72-2-4", url=BASE+YOUTUBE_CHANNEL_ID_38+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSICuW7UCwV-Ha8lMyYM8yrHqdJ5SJ8BgLgZpnXheV4RKEm_q5ATg")
	
	Add_Dir( 
        name="Thomas Hearns 61-5-1", url=BASE+YOUTUBE_CHANNEL_ID_39+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8c5mvki3pFgA9k7lGeKaFVupDNm6ZTh2kt-RQNSW6bIK6rd0h")
	
	Add_Dir( 
        name="Larry Holmes 69-6", url=BASE+YOUTUBE_CHANNEL_ID_40+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6yE0dv1y1WC668EnXV5qceASUUethie1Gj1r0m6aFhTFLEF703g")
	
	Add_Dir( 
        name="Roy Jones Jr 50-4", url=BASE+YOUTUBE_CHANNEL_ID_41+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4FwN929EClmVYi2CJE1bMFK-xdIM47rReHa9nKGlFBI8faxuXFg")
	
	Add_Dir( 
        name="Ted 'kid' Lewis 173-30-14", url=BASE+YOUTUBE_CHANNEL_ID_42+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3tDceWf7VeukB6IeuTq_8k5O196rqTcyMuejKlkzq2LPlA78c")
	
	Add_Dir( 
        name="Carlos Monzon 87-3-9-1", url=BASE+YOUTUBE_CHANNEL_ID_43+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoX9_mpQC6EuXLK15aWihNz_Ql2rp343jDo9MLyKCzSFIphALC")
	
	Add_Dir( 
        name="Pernell Whitaker 40-4-1-1", url=BASE+YOUTUBE_CHANNEL_ID_44+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ78w7rj58dIKCF4GKAPlLlSP3myZ9Bph4YfYkQu_MRwMCSFEWyLg")
	
	Add_Dir( 
        name="Bernard Hopkins 47-4-1", url=BASE+YOUTUBE_CHANNEL_ID_45+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2e6Y9FUCMyOOnYUQ7M6j07BJ5476VGHAwsAJMai_SoLdOSWcUUA")
	
	Add_Dir( 
        name="Alexis Arguello 80-8", url=BASE+YOUTUBE_CHANNEL_ID_46+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQErP5A_ozidm0w82xzEDoJiz8yrJK-5JUIula31Z5HGx2DUl8ibw")
	
	Add_Dir( 
        name="Jose Napoles 77-7", url=BASE+YOUTUBE_CHANNEL_ID_47+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKufkuRdIVhUIyAdN-D_cbhdwifN9v2kvbZ5BBjwP8jZkNhRmnzg")
		
	Add_Dir( 
		name="Marco Antonio Barrera 63-5", url=BASE+YOUTUBE_CHANNEL_ID_48+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSk1Vct5WS8DbLxYL2oQ5iR9FJyqMV0IvcKsEu0iodCXackqUv3RQ")
	
	Add_Dir( 
        name="Riddick Bowe 43-1-1", url=BASE+YOUTUBE_CHANNEL_ID_49+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStfYUsjbGhX_qxfBc0txCa0LwLZfBpQBsCrmH1x1C1Q8tVd0FZ")

	Add_Dir( 
        name="Wladimir Klitschko 64-5", url=BASE+YOUTUBE_CHANNEL_ID_50+"/", folder=True,
        icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBjw9PTMmjs_8sIeh6Jrb-zsEQIqjt8tir1bREFWlJ28aywahc")
		
		
		
		
		
		
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()

@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)

if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))