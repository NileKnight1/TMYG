# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = Character("Userkaf", color="#7A5A2E")        
define m = Character("Minas", color="#4A2E14")          
define e = Character("Eya", color="#4B2A4F")            
define t = Character("Tausert", color="#1F4A4A")        
define um = Character("Userkaf's Mother", color="#3F2A6B") 
define ud = Character("Userkaf's Father", color="#1F3D5A") 
define V = Character("Village Chief", color="#5C3A1E")  
define ss = Character("STRANGER", color="#2B2B2B")      
define i = Character("Intaf", color="#7A2E2E")          


image intro:
    "bg/intro.png"  
    xalign 0.0
    yalign 0.5
    linear 50.0 xalign 1.0




transform showFade:
    alpha 0.0 
    linear 0.5 alpha 1.0 

transform hideFade:
    alpha 1.0 
    linear 1.0 alpha 0.0 

transform showBlur:
    blur 0 
    linear 1.0 blur 10

transform hideBlur:
    blur 10 
    linear 1.0 blur 0

transform p1:
    xalign 0.0 yalign 1.0 zoom 0.6
transform p2:
    xalign 0.30 yalign 1.0 zoom 0.6
transform p3:
    xalign 0.70 yalign 1.0 zoom 0.6
transform p4:
    xalign 1.0 yalign 1.0 zoom 0.6



##################
### Characters ###
##################


image userkaf h:
    "ch/userkaf.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/userkaf2.png"
    crop(0, 0, 640, 960)
    pause 0.1
    repeat    
image userkaf s:
    "ch/userkaf.png"
    crop(0, 960, 640, 960)
    pause 5
    "ch/userkaf2.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat
image userkaf a:
    "ch/userkaf.png"
    crop(0, 1920, 640, 960)
    pause 5
    "ch/userkaf2.png"
    crop(0, 1920, 640, 960)
    pause 0.1
    repeat
image userkaf c:
    "ch/userkaf.png"
    crop(0, 2880, 640, 960)
    pause 5
    "ch/userkaf2.png"
    crop(0, 2880, 640, 960)
    pause 0.1
    repeat
image userkaf n:
    "ch/userkaf.png"
    crop(0, 3840, 640, 960)
    pause 5
    "ch/userkaf2.png"
    crop(0, 3840, 640, 960)
    pause 0.1
    repeat
image userkaf z:
    "ch/userkaf.png"
    crop(0, 4800, 640, 960)
    pause 5
    "ch/userkaf2.png"
    crop(0, 4800, 640, 960)
    pause 0.1
    repeat
image userkaf b:
    "ch/userkaf.png"
    crop(0, 5760, 640, 960)
    pause 5
    "ch/userkaf2.png"
    crop(0, 5760, 640, 960)
    pause 0.1
    repeat
image userkaf d:
    "ch/userkaf.png"
    crop(0, 6720, 640, 960)
    pause 5
    "ch/userkaf2.png"
    crop(0, 6720, 640, 960)
    pause 0.1
    repeat

image minas h:
    "ch/minas.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/minas2.png"
    crop(0, 0, 640, 960)
    pause 0.1
    repeat    
image minas s:
    "ch/minas.png"
    crop(0, 960, 640, 960)
    pause 5
    "ch/minas2.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat
image minas d:
    "ch/minas.png"
    crop(0, 1920, 640, 960)
    pause 5
    "ch/minas2.png"
    crop(0, 1920, 640, 960)
    pause 0.1
    repeat
image minas z:
    "ch/minas.png"
    crop(0, 2880, 640, 960)
    pause 5
    "ch/minas2.png"
    crop(0, 2880, 640, 960)
    pause 0.1
    repeat
image minas n:
    "ch/minas.png"
    crop(0, 3840, 640, 960)
    pause 5
    "ch/minas2.png"
    crop(0, 3840, 640, 960)
    pause 0.1
    repeat    
image minas b:
    "ch/minas.png"
    crop(0, 4800, 640, 960)
    pause 5
    "ch/minas2.png"
    crop(0, 4800, 640, 960)
    pause 0.1
    repeat
image minas c:
    "ch/minas.png"
    crop(0, 5760, 640, 960)
    pause 5
    "ch/minas2.png"
    crop(0, 5760, 640, 960)
    pause 0.1
    repeat
image minas a:
    "ch/minas.png"
    crop(0, 6720, 640, 960)
    pause 5
    "ch/minas2.png"
    crop(0, 6720, 640, 960)
    pause 0.1
    repeat

image tausert h:
    "ch/tausert.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/tausert2.png"
    crop(0, 0, 640, 960)
    pause 0.1
    repeat    
image tausert s:
    "ch/tausert.png"
    crop(0, 960, 640, 960)
    pause 5
    "ch/tausert2.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat
image tausert n:
    "ch/tausert.png"
    crop(0, 1920, 640, 960)
    pause 5
    "ch/tausert2.png"
    crop(0, 1920, 640, 960)
    pause 0.1
    repeat
image tausert a:
    "ch/tausert.png"
    crop(0, 2880, 640, 960)
    pause 5
    "ch/tausert2.png"
    crop(0, 2880, 640, 960)
    pause 0.1
    repeat
image tausert z:
    "ch/tausert.png"
    crop(0, 3840, 640, 960)
    pause 5
    "ch/tausert2.png"
    crop(0, 3840, 640, 960)
    pause 0.1
    repeat    
image tausert b:
    "ch/tausert.png"
    crop(0, 4800, 640, 960)
    pause 5
    "ch/tausert2.png"
    crop(0, 4800, 640, 960)
    pause 0.1
    repeat
image tausert c:
    "ch/tausert.png"
    crop(0, 5760, 640, 960)
    pause 5
    "ch/tausert2.png"
    crop(0, 5760, 640, 960)
    pause 0.1
    repeat

image eya h:
    "ch/eya.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/eya2.png"
    crop(0, 0, 640, 960)
    pause 0.1
    repeat    
image eya s:
    "ch/eya.png"
    crop(0, 960, 640, 960)
    pause 5
    "ch/eya2.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat
image eya n:
    "ch/eya.png"
    crop(0, 1920, 640, 960)
    pause 5
    "ch/eya2.png"
    crop(0, 1920, 640, 960)
    pause 0.1
    repeat
image eya a:
    "ch/eya.png"
    crop(0, 2880, 640, 960)
    pause 5
    "ch/eya2.png"
    crop(0, 2880, 640, 960)
    pause 0.1
    repeat
image eya z:
    "ch/eya.png"
    crop(0, 3840, 640, 960)
    pause 5
    "ch/eya2.png"
    crop(0, 3840, 640, 960)
    pause 0.1
    repeat    
image eya b:
    "ch/eya.png"
    crop(0, 4800, 640, 960)
    pause 5
    "ch/eya2.png"
    crop(0, 4800, 640, 960)
    pause 0.1
    repeat
image eya c:
    "ch/eya.png"
    crop(0, 5760, 640, 960)
    pause 5
    "ch/eya2.png"
    crop(0, 5760, 640, 960)
    pause 0.1
    repeat

image udad:
    "ch/dad.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/dad.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat    

image udad h:
    "ch/dad.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/dad.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat    
image udad s:
    "ch/dad.png"
    crop(0, 1920, 640, 960)
    pause 5
    "ch/dad.png"
    crop(0, 2880, 640, 960)
    pause 0.1
    repeat

image umom:
    "ch/mom.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/mom.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat    

image umom h:
    "ch/mom.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/mom.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat    
image umom n:
    "ch/mom.png"
    crop(0, 1920, 640, 960)
    pause 5
    "ch/mom.png"
    crop(0, 2880, 640, 960)
    pause 0.1
    repeat
image umom s:
    "ch/mom.png"
    crop(0, 3840, 640, 960)
    pause 5
    "ch/mom.png"
    crop(0, 4800, 640, 960)
    pause 0.1
    repeat


image kid h:
    "ch/kid.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/kid.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat    
image kid n:
    "ch/kid.png"
    crop(0, 1920, 640, 960)
    pause 5
    "ch/kid.png"
    crop(0, 2880, 640, 960)
    pause 0.1
    repeat

image kidmom h:
    "ch/kidmom.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/kidmom.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat    
image kidmom n:
    "ch/kidmom.png"
    crop(0, 1920, 640, 960)
    pause 5
    "ch/kidmom.png"
    crop(0, 2880, 640, 960)
    pause 0.1
    repeat


image cheif:
    "ch/cheif.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/cheif.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat    

image stranger:
    "ch/stranger.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/stranger.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat    

image stranger c1:
    "ch/stranger2.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/stranger2.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat    
image stranger c2:
    "ch/stranger2.png"
    crop(0, 1920, 640, 960)
    pause 5
    "ch/stranger2.png"
    crop(0, 2880, 640, 960)
    pause 0.1
    repeat
image stranger c3:
    "ch/stranger2.png"
    crop(0, 3840, 640, 960)
    pause 5
    "ch/stranger2.png"
    crop(0, 4800, 640, 960)
    pause 0.1
    repeat
image stranger c4:
    "ch/stranger2.png"
    crop(0, 5760, 640, 960)
    pause 5
    "ch/stranger2.png"
    crop(0, 6720, 640, 960)
    pause 0.1
    repeat

image monster:
    "ch/monster.png"
    crop(0, 0, 640, 960)
    pause 5
    "ch/monster.png"
    crop(0, 960, 640, 960)
    pause 0.1
    repeat    


##################
##### Places #####
##################


image bg ubd1:
    "bg/ubd1.png" 
    crop (0,0,1280,720)
    pause 0.2
    "bg/ubd1.png" 
    crop (0,720,1280,720)
    pause 0.2
    "bg/ubd1.png" 
    crop (0,1440,1280,720)
    pause 0.2
    "bg/ubd1.png" 
    crop (0,2160,1280,720)
    pause 0.2
    "bg/ubd1.png" 
    crop (0,2880,1280,720)
    pause 0.2
    
    "bg/ubd1.png" 
    crop (0,3600,1280,720)
    pause 0.2
    "bg/ubd1.png" 
    crop (0,4320,1280,720)
    pause 0.2
    "bg/ubd1.png" 
    crop (0,5040,1280,720)
    pause 0.2
    "bg/ubd1.png" 
    crop (0,5760,1280,720)
    pause 0.2
    "bg/ubd1.png" 
    crop (0,6480,1280,720)
    pause 0.2

    repeat

image bg ubd1-2:
    "bg/ubd1-2.png" 
    crop (0,0,1280,720)
    pause 0.2
    "bg/ubd1-2.png" 
    crop (0,720,1280,720)
    pause 0.2
    "bg/ubd1-2.png" 
    crop (0,1440,1280,720)
    pause 0.2
    "bg/ubd1-2.png" 
    crop (0,2160,1280,720)
    pause 0.2
    "bg/ubd1-2.png" 
    crop (0,2880,1280,720)
    pause 0.2
    
    "bg/ubd1-2.png" 
    crop (0,3600,1280,720)
    pause 0.2
    "bg/ubd1-2.png" 
    crop (0,4320,1280,720)
    pause 0.2
    "bg/ubd1-2.png" 
    crop (0,5040,1280,720)
    pause 0.2
    "bg/ubd1-2.png" 
    crop (0,5760,1280,720)
    pause 0.2
    "bg/ubd1-2.png" 
    crop (0,6480,1280,720)
    pause 0.2

    repeat

image bg ubd2:
    "bg/ubd2.png" 
    crop (0,0,1280,720)
    pause 1.0
    "bg/ubd2.png" 
    crop (0,720,1280,720)
    pause 1.0
    "bg/ubd2.png" 
    crop (0,1440,1280,720)
    pause 1.0
    "bg/ubd2.png" 
    crop (0,2160,1280,720)
    pause 1.0
    
    repeat

image bg ubd3:
    "bg/ubd3.png"

image bg kitchen1:
    "bg/kit1.png" 
    crop (0,0,1280,720)
    pause 0.2
    "bg/kit1.png" 
    crop (0,720,1280,720)
    pause 0.2
    "bg/kit1.png" 
    crop (0,1440,1280,720)
    pause 0.2
    "bg/kit1.png" 
    crop (0,2160,1280,720)
    pause 0.2
    "bg/kit1.png" 
    crop (0,2880,1280,720)
    pause 0.2   
    repeat 

image bg kitchen1-2:
    "bg/kit1-2.png" 
    crop (0,0,1280,720)
    pause 0.2
    "bg/kit1-2.png" 
    crop (0,720,1280,720)
    pause 0.2
    "bg/kit1-2.png" 
    crop (0,1440,1280,720)
    pause 0.2
    "bg/kit1-2.png" 
    crop (0,2160,1280,720)
    pause 0.2
    "bg/kit1-2.png" 
    crop (0,2880,1280,720)
    pause 0.2   
    repeat 

image bg kitchen1-3:
    "bg/kit1-3.png" 
    crop (0,0,1280,720)
    pause 0.2
    "bg/kit1-3.png" 
    crop (0,720,1280,720)
    pause 0.2
    "bg/kit1-3.png" 
    crop (0,1440,1280,720)
    pause 0.2
    "bg/kit1-3.png" 
    crop (0,2160,1280,720)
    pause 0.2
    "bg/kit1-3.png" 
    crop (0,2880,1280,720)
    pause 0.2   
    repeat 

image bg kitchen1-4:
    "bg/kit1-4.png" 
    crop (0,0,1280,720)
    pause 0.2
    "bg/kit1-4.png" 
    crop (0,720,1280,720)
    pause 0.2
    "bg/kit1-4.png" 
    crop (0,1440,1280,720)
    pause 0.2
    "bg/kit1-4.png" 
    crop (0,2160,1280,720)
    pause 0.2
    "bg/kit1-4.png" 
    crop (0,2880,1280,720)
    pause 0.2   
    repeat 

image bg kitchen2:
    "bg/kit2.png"

image bg kitchen2-2:
    "bg/kit2-2.png" 
    crop (0,0,1280,720)
    pause 0.2
    "bg/kit2-2.png" 
    crop (0,720,1280,720)
    pause 0.2
    "bg/kit2-2.png" 
    crop (0,1440,1280,720)
    pause 0.2
    "bg/kit2-2.png" 
    crop (0,2160,1280,720)
    pause 0.2
    "bg/kit2-2.png" 
    crop (0,2880,1280,720)
    pause 0.2   
    repeat 

image bg kitchen3:
    "bg/kit3.png"

image bg kitchen3-2:
    "bg/kit3-2.png" 
    crop (0,0,1280,720)
    pause 0.2
    "bg/kit3-2.png" 
    crop (0,720,1280,720)
    pause 0.2
    "bg/kit3-2.png" 
    crop (0,1440,1280,720)
    pause 0.2
    "bg/kit3-2.png" 
    crop (0,2160,1280,720)
    pause 0.2
    "bg/kit3-2.png" 
    crop (0,2880,1280,720)
    pause 0.2   
    repeat 

image bg street1 m:
    "bg/street1.png"
image bg street1 e:
    "bg/street1-2.png"
image bg street1 n:
    "bg/street1-3.png"

image bg street2 m:
    "bg/street2.png"
image bg street2 e:
    "bg/street2-2.png"
image bg street2 n:
    "bg/street2-3.png"

image bg street3 m:
    "bg/street3.png"
image bg street3 e:
    "bg/street3-2.png"
image bg street3 n:
    "bg/street3-3.png"

image bg street3:
    "bg/street3.png"
image bg street2:
    "bg/street2.png"

image bg square:
    "bg/square.png" 
    crop (0,0,1280,720)
    pause 0.1
    "bg/square.png" 
    crop (0,720,1280,720)
    pause 0.1
    "bg/square.png" 
    crop (0,1440,1280,720)
    pause 0.1
    "bg/square.png" 
    crop (0,2160,1280,720)
    pause 0.1
    "bg/square.png" 
    crop (0,2880,1280,720)
    pause 0.1
    "bg/square.png" 
    crop (0,3600,1280,720)
    pause 0.1
    

    repeat
image bg square1-2:
    "bg/square1-2.png" 
    crop (0,0,1280,720)
    pause 0.1
    "bg/square1-2.png" 
    crop (0,720,1280,720)
    pause 0.1
    "bg/square1-2.png" 
    crop (0,1440,1280,720)
    pause 0.1
    "bg/square1-2.png" 
    crop (0,2160,1280,720)
    pause 0.1
    "bg/square1-2.png" 
    crop (0,2880,1280,720)
    pause 0.1
    "bg/square1-2.png" 
    crop (0,3600,1280,720)
    pause 0.1
    

    repeat
image bg square2:
    "bg/square2.png"
image bg square3:
    "bg/square3.png"

image bg sq2:
    "bg/square mag.png" 

image bg palm1:
    "bg/palm.png" 
image bg palm2:
    "bg/palm2.png" 
image bg palm3:
    "bg/palm3.png"

image bg temple1:
    "bg/temple1.png" 
image bg temple2:
    "bg/temple2.png" 
image bg temple3:
    "bg/temple3.png" 
image bg temple4:
    "bg/temple4.png" 

image bg temple5:
    "bg/temple5.png" 
    crop (0,0,1280,720)
    pause 0.2
    "bg/temple5.png" 
    crop (0,720,1280,720)
    pause 0.2
    "bg/temple5.png" 
    crop (0,1440,1280,720)
    pause 0.2
    "bg/temple5.png" 
    crop (0,2160,1280,720)
    pause 0.2
    "bg/temple5.png" 
    crop (0,2880,1280,720)
    pause 0.2   
    repeat 

image bg eya m:
    "bg/eyah1.png"
image bg eya e:
    "bg/eyah2.png"
image bg eya n:
    "bg/eyah3.png"

image bg eyan:
    "bg/eyanh.png"

image bg intaf m:
    "bg/intafh.png"
image bg intaf e:
    "bg/intafh2.png"

image bg raceday1:
    "bg/raceday.png"
image bg raceday2:
    "bg/raceday end.png"



##################
##### Assets #####
##################


image mirror1:
    "assets/mirror1.png" 
    crop (0,0,1280,720)
    pause 5
    "assets/mirror1.png" 
    crop (0,720,1280,720)
    pause 0.1
    repeat
image mirror2:
    "assets/mirror2.png" 
    crop (0,0,1280,720)
    pause 5
    "assets/mirror2.png" 
    crop (0,720,1280,720)
    pause 0.1
    repeat
image mirror3:
    "assets/mirror3.png" 
    crop (0,0,1280,720)
    pause 5
    "assets/mirror3.png" 
    crop (0,720,1280,720)
    pause 0.1
    repeat
image mirror4:
    "assets/mirror4.png" 
    crop (0,0,1280,720)
    pause 5
    "assets/mirror4.png" 
    crop (0,720,1280,720)
    pause 0.5
    repeat
image mirror5:
    "assets/mirror5.png" 
    crop (0,0,1280,720)
    pause 5
    "assets/mirror5.png" 
    crop (0,720,1280,720)
    pause 0.5
    repeat
image mirror6:
    "assets/mirror6.png" 
    crop (0,0,1280,720)
    pause 5
    "assets/mirror6.png" 
    crop (0,720,1280,720)
    pause 0.5
    repeat
image mirror7:
    "assets/mirror7.png" 
    crop (0,0,1280,720)
    pause 5
    "assets/mirror7.png" 
    crop (0,720,1280,720)
    pause 0.5
    repeat
image mirror8:
    "assets/mirror8.png" 
    crop (0,0,1280,720)
    pause 5
    "assets/mirror8.png" 
    crop (0,720,1280,720)
    pause 0.5
    repeat

image sun:
    "assets/sun.png"
    # Vecteezy.com

image papyrus 1:
    "assets/papyrus.png"
    crop (0,0,1280,720)
image papyrus 2:
    "assets/papyrus.png"
    crop (0,720,1280,720)
image papyrus 3:
    "assets/papyrus.png"
    crop (0,1440,1280,720)
image papyrus 4:
    "assets/papyrus.png"
    crop (0,2160,1280,720)

default s = 0
default eat = 0
default dwp = 0
default dN = 7
default smeet = 0

##################
##### Audio ######
##################

define intro_music = "audio/egypt.ogg"
define music_morning = "audio/morning.ogg"
define music_night = "audio/night normal.ogg"
define music_rivermorning = "audio/river morning.ogg"
define music_riverevening = "audio/river.ogg"
define music_rivernight = "audio/river night.ogg"
define music_crowd = "audio/crowd.ogg"
define music_happy = "audio/happy.ogg"
define music_weird = "audio/wednes.ogg"
define music_official = "audio/official.ogg"
define music_faint = "audio/faint.ogg"
define music_night = "audio/night normal.ogg"
define music_jungle = "audio/jungle.ogg"
define music_wind = "audio/wind.ogg"
define music_laca = "audio/laca.ogg"
define music_mine = "audio/mine.ogg"
define music_calm = "audio/calm.ogg"
define music_mis = "audio/mis.ogg"
define music_temple = "audio/s.ogg"



# SFX

define sfx_apple = "audio/eating apple.ogg"
define sfx_rooster = "audio/rooster.ogg"
define sfx_fall = "audio/date fall.ogg"
define sfx_sun = "audio/sun rays.ogg"
define sfx_sleep = "audio/sleep.ogg"
define sfx_out = "audio/door open 2.ogg"
define sfx_appear = "audio/appear.ogg"
define sfx_disappear = "audio/disappear.ogg"
define sfx_sudden = "audio/transform.ogg"
define sfx_magic = "audio/magic.ogg"
define sfx_paper = "audio/paper.ogg"
define sfx_search = "audio/search.ogg"
define sfx_confusion = "audio/confusion.ogg"

define sfx_fastheartbeats = "audio/fast heartbeats.ogg"
define sfx_slowheartbeats = "audio/slow heartbeats.ogg"
define sfx_love = "audio/love.ogg"
define sfx_faintdrop = "audio/faint drop.ogg"
define sfx_angry = "audio/angry2.ogg"
define sfx_amazed = "audio/amazed.ogg"

define sfx_sparkle1 = "audio/sparkle.ogg"
define sfx_sparkle2 = "audio/sparkle2.ogg"
define sfx_sparkle3 = "audio/sparkle3.ogg"

define sfx_water = "audio/water drop.ogg"
define sfx_run = "audio/run.ogg"
define sfx_push = "audio/faint drop.ogg"
define sfx_colapse = "audio/pillar colapse.ogg"
define sfx_rewind = "audio/rewind.ogg"
define sfx_stab = "audio/stab.ogg"
define sfx_monster = "audio/monster.ogg"

define sfx_temple1 = "audio/temple1.ogg"
define sfx_temple2 = "audio/temple2.ogg"