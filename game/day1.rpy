default n = 0

init python:
    renpy.music.register_channel("music2", mixer="music", loop=True)
    renpy.music.register_channel("music3", mixer="music", loop=True)
    def lock_skipping():
        config.allow_skipping = False

    def unlock_skipping():
        config.allow_skipping = True

    def pau(time):
        renpy.pause(time, hard=True)

        

    def spau(name):
        renpy.music.play(name, channel="sound", _async=False)

label start:

    # jump d9k2


    if n == 0:
        $ n = 1
        show intro
        $ lock_skipping()
        # [edit]
        play music intro_music fadein 1.0

        "{cps=35}Egypt...{/cps}{w=1.5}{nw}"
        
        "{cps=35}Who doesn't know Egypt?{/cps}{w=1.5}{nw}"
        
        "{cps=35}Egyptians were always special.{/cps}{w=1.5}{nw}"
        
        "{cps=35}They had three seasons.{/cps}{w=2.0}{nw}"
        
        "{cps=35}Starting with Shemu...{/cps}{w=1.5}{nw}"
        
        "{cps=35}Yes, it's called Shemu.{/cps}{w=1.5}{nw}"
        
        "{cps=35}They harvested the crops before the flooding of the Nile.{/cps}{w=2.5}{nw}"
        
        "{cps=35}Then Akhet...{/cps}{w=1.5}{nw}"
        
        "{cps=35}The Nile's flooding season.{/cps}{w=2.0}{nw}"
        
        "{cps=35}And finally, Peret.{/cps}{w=1.5}{nw}"
        
        "{cps=35}When they began to plant the crops.{/cps}{w=2.5}{nw}"
        
        "{cps=35}In a small village in Aswan...{/cps}{w=1.5}{nw}"
        
        "{cps=35}Exactly, in Kom Ombo.{/cps}{w=1.5}{nw}"
        
        "{cps=35}People used to celebrate the Peret season in their own way.{/cps}{w=3.0}{nw}"
        
        "{cps=35}And there was a very special contest during these celebrations...{/cps}{w=3.5}{nw}"
        
        "{cps=35}The Guardians of the Nile.{/cps}{w=4.0}{nw}"
        
        "{cps=35}In 2550 BC, in a small house...{/cps}{w=4.5}{nw}"
        
        $ unlock_skipping()

        stop music fadeout 1.0

    scene bg ubd1 with pixellate
    if(s == 0):
        play sound sfx_rooster
        $ pau(1.2)

    pause 1.0
    play music music_morning fadein 1.0

    if s == 0:
        play sound sfx_appear
        show userkaf n at left, showFade 
        pause 1.0
        play sound sfx_appear
        show umom at right, showFade
        $ renpy.music.set_volume(0.6, delay=0, channel='music2')
        play music2 music_happy fadein 1.0
        pause 1.0
        um "{cps=20}Good morning, Userkaf!{/cps}"
        play sound sfx_sparkle3
        show userkaf h at left
        u "{cps=20}Good morning mom!{/cps}"
        um "{cps=20}Today is the day you're waiting for.{/cps}"
        u "{cps=20}Yeah, I'm so excited.{/cps}"
        u "{cps=20}Where's dad?{/cps}"
        um "{cps=20}In the village square, he is gathered with the elders.{/cps}"
        um "{cps=20}I'll leave you now, I'm sewing some clothes for the festival.{/cps}"
        um "{cps=20}Don't forget to eat before you go.{/cps}"
        u "{cps=20}Okay mom thank you!{/cps}"
        pause 1.0

        play sound sfx_disappear
        show umom at right, hideFade with dissolve
        hide umom
        show userkaf n at left
        $ s = 1
        stop music2 fadeout 1.0
        pause 1.0
    else:
        play sound sfx_appear
        show userkaf n at left, showFade 
        pause 1.0


    menu:
        "Look in the mirror":
            play sound sfx_disappear
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            pause 1.0

            scene bg ubd1 at showBlur
            play sound sfx_magic
            
            show mirror1 with dissolve

            if(eat == 0):
                u "{cps=20}I'm hungry.{/cps}"
            else:
                u "{cps=20}I'm so exited for the opening day.{/cps}"

            show mirror1 at hideFade with dissolve
            hide mirror1
            play sound sfx_disappear

            jump start


        "Go to the kitchen":
            play sound sfx_disappear
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            $ pau(1.0)
            play sound sfx_out
            jump kit1
            

        "Go to the festival opening":
            play sound sfx_out
            jump out1
    return

label kit1:
    if eat == 0:
        scene bg kitchen1 with pixellate
        pause 1.0
        play sound sfx_appear
        show userkaf n at left, showFade
        pause 1.0
        u "{cps=20}Oh an apple!{/cps}"
        show userkaf h at left
        menu:
            "Eat the apple":
                $ eat = 1
                play sound sfx_apple
                scene bg kitchen1-2 with pixellate
                show userkaf h at left, showFade
                u "{cps=20}So delicious.{/cps}"

            "Go back to your room":
                play sound sfx_disappear
                show userkaf h at hideFade with dissolve
                hide userkaf h 
                pause 1.0
                play sound sfx_out
                jump start

    menu:
        "Go back to your room":
            play sound sfx_disappear
            show userkaf h at hideFade with dissolve
            hide userkaf h 
            pause 1.0
            play sound sfx_out
            jump start


    return

label out1:
    scene bg street1 m with pixellate
    pause 1.0
    play sound sfx_appear
    show userkaf n at left, showFade
    pause 1.0

    u "{cps=20}Nice air ...{/cps}"
    play sound sfx_confusion
    show userkaf c at left
    "A familiar voice" "{cps=20}Hoho, look who's here!{/cps}"

    show minas h at right, showFade
    play music2 music_happy fadein 1.0
    play sound sfx_appear
    pause 1.0

    show userkaf h at left

    u "{cps=20}HEYYY MINAAS!{/cps}"
    m "{cps=20}HEYYY BROTHER!{/cps}"
    if eat == 0:
        m "{cps=20}Bro you don't seem good, are you okay?{/cps}"
        u "{cps=20}Yeah, I'm all good. Don't worry.{/cps}"
        m "{cps=20}The day is gonna be tiring. You gotta be ready.{/cps}"


    m "{cps=20}Wanna go to the opening together?.{/cps}"
    
    menu:
        "Go with him":
            u "{cps=20}I was gonna say the same.{/cps}"

        "Go back home":
            u "{cps=20}I'll go home very quick ...{/cps}"
            u "{cps=20}Wait for me there.{/cps}"
            m "{cps=20}Okay, see you.{/cps}"
            show userkaf h at left, hideFade with dissolve
            hide userkaf h
            play sound sfx_disappear
            show minas h at right, hideFade with dissolve
            hide minas h
            play sound sfx_disappear
            pause 1.0

            if eat == 0:
                stop music2 fadeout 1.0
                play sound sfx_out
                jump room2
            else:
                stop music2 fadeout 1.0
                play sound sfx_out
                jump room22
    


    m "{cps=20}Great!{/cps}"
    show userkaf h at left, hideFade with dissolve
    hide userkaf h
    play sound sfx_disappear
    show minas h at right, hideFade with dissolve
    hide minas h
    play sound sfx_disappear

    stop music2 fadeout 1.0
    stop music fadeout 1.0
    pause 1.0
    jump square1


    return

label room2:
    scene bg ubd1 with pixellate
    pause 1.0
    play sound sfx_angry
    show userkaf a at left, showFade
    pause 1.0

    menu:
        "Look in the mirror":
            show userkaf a at left, hideFade with dissolve
            hide userkaf a
            play sound sfx_disappear
            pause 1.0

            scene bg ubd1 at showBlur
            play sound sfx_magic
            
            show mirror4 with dissolve

            u "{cps=20}I'm very hungry!{/cps}"

            show mirror4 at hideFade with dissolve
            hide mirror4
            play sound sfx_disappear
            jump room2

        "Go to the kitchen":
            show userkaf a at left, hideFade with dissolve
            hide userkaf a
            play sound sfx_disappear
            jump kit2

        "Go Out":
            play sound sfx_out
            jump out2

    return

label kit2:
    scene bg kitchen1-2 with pixellate
    play sound sfx_out
    pause 1.0
    show userkaf a at left, showFade
    play sound sfx_angry
    
    u "{cps=30}THERE'S NO FOOD, I'M HUNGRY!{/cps}"
    menu:
        "Search the home for food":
            show userkaf a at left, hideFade with dissolve
            hide userkaf a
            play sound sfx_disappear
            $ pau(0.5)
            play sound sfx_search 
            pause 5.0
            show userkaf a at left, showFade
            u "{cps=30}Nothing here{/cps}"

    
        "Call you mother":
            u "{cps=30}MOM ARE YOU HERE?{/cps}"
            "..."

        "Go out":
            show userkaf a at left, hideFade with dissolve
            hide userkaf a
            play sound sfx_disappear
            pause 1.0
            play sound sfx_out
            jump out2

    u "{cps=30}I'm going out!{/cps}"

    show userkaf a at left, hideFade with dissolve
    hide userkaf a
    play sound sfx_disappear
    pause 1.0    
    play sound sfx_out
    jump out2

    return    

label room22:
    scene bg ubd1 with pixellate
    pause 1.0
    play sound sfx_appear
    show userkaf n at left, showFade
    pause 1.0

    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            play sound sfx_disappear
            pause 1.0

            scene bg ubd1 at showBlur
            play sound sfx_magic
            
            show mirror1 with dissolve

            u "{cps=20}I don't know why I came here.{/cps}"

            show mirror1 at hideFade with dissolve
            hide mirror1
            play sound sfx_disappear
            jump room22

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            play sound sfx_disappear
            jump kit22
        
        "Go to the festival opening":
            stop music fadeout 1.0
            play sound sfx_out
            jump square2

    return

label kit22:
    scene bg kitchen1-2 with pixellate
    play sound sfx_out
    pause 1.0
    play sound sfx_appear
    show userkaf n at left, showFade
    
    menu:
        "Go back to your room":
            show userkaf n at left, hideFade
            hide userkaf n
            play sound sfx_disappear
            pause 1.0
            play sound sfx_out
            jump room22


    return    

label out2:


    scene bg street1 m with pixellate
    pause 1.0
    show userkaf a at left, showFade
    play sound sfx_appear
    pause 1.0
    play sound sfx_sudden
    show stranger at right, showFade
    play music2 music_weird fadein 1.0
    pause 1.0
    ss "{cps=20}Hey kid! Why do you look angry?{/cps}"
    show userkaf s at left
    $ smeet = 1

    u "{cps=20}I didn't eat anything and I'm late for the opening!{/cps}"
    ss "{cps=20}Don't worry, take this loaf!{/cps}"

    menu:
        "Take it":
            play sound sfx_sparkle2
            show userkaf h at left
            u "{cps=20}Oh sir thank you.{/cps}"
            ss "{cps=20}You're welcome kid ...{/cps}"
            ss "{cps=20}Now go fast they have started.{/cps}"
            show userkaf h at left, hideFade with dissolve
            hide userkaf h
            play sound sfx_disappear
            pause 1.0
            stop music fadeout 1.0
            stop music2 fadeout 1.0
            jump square2
            
        "Don't take it":
            u "{cps=20}No thanks.{/cps}"
            ss "{cps=20}As you like.{/cps}"

            play music3 music_faint fadein 1.0

            with Fade(0.1, 0.1, 1.0)
            with Fade(0.2, 0.1, 1.0)
            with Fade(0.4, 0.1, 1.0)
            with Fade(0.8, 0.2, 1.0)
            stop music fadeout 1.0
            stop music2 fadeout 1.0
            stop music3 fadeout 1.0
            pause 1.0
            play sound sfx_faintdrop
            scene black
            $ pau(1.0)
            play sound sfx_slowheartbeats
            $ pau(5.0)

            scene bg street1 m
            play sound sfx_confusion
            show userkaf c at left
            show stranger at right
            


            play music music_morning fadein 1.0
            play music2 music_weird fadein 1.0

            pause 1.0
            play sound sfx_confusion
            show userkaf c at left
            u "{cps=20}What happened?{/cps}"
            ss "{cps=20}You fainted.{/cps}"
            ss "{cps=20}I told you!{/cps}"

            u "{cps=20}I'm sorry sir ...{/cps}"
            show userkaf s at left

            u "{cps=20}I don't know how to thank you.{/cps}"
            ss "{cps=20}No worries ...{/cps}"
            show userkaf h at left
            ss "{cps=20}Now go to the ceremony fast.{/cps}"
            show userkaf h at left, hideFade with dissolve
            hide userkaf h
            play sound sfx_disappear

            pause 1.0
            stop music fadeout 1.0
            stop music2 fadeout 1.0
            jump square2


    return


label square1:
    scene bg square with pixellate
    play music music_crowd fadein 1.0
    pause 1.0

    stop music fadeout 1.0
    play sound sfx_amazed
    V "{cps=10}SILENCE.{/cps}"
    pause 1.0
    
    show cheif at center, showFade
    play sound sfx_appear
    pause 1.0
    play music2 music_official fadein 1.0
    if eat == 0:
        jump square1n
        
    V "{cps=10}All of us know why we are gathering here ...{/cps}"

    V "{cps=10}Peret Festival is after 3 days ...{/cps}"
    V "{cps=10}And of course the most thing you're waiting for is ...{/cps}"
    V "{cps=10}Guardians Of The Nile ...{/cps}"
    V "{cps=10}So ..{/cps}"
    V "{cps=10}Whoever wants to participate please gather here !{/cps}"
    V "{cps=10}We having here 44 boy and girl ...{/cps}"
    V "{cps=10}PREPARE THE PAPYRUS !{/cps}"

    stop music2 fadeout 1.0
    play music music_crowd fadein 1.0

    pause 1.0
    show cheif at center, hideFade with dissolve
    hide cheif
    play sound sfx_disappear


    pause 1.0

    play sound sfx_appear
    show userkaf s at left, showFade
    pause 1.0
    play sound sfx_appear
    show minas n at right, showFade
    pause 1.0
    
    m "{cps=20}Userkaf what's wrong??{/cps}"
    show minas s at right

    u "{cps=20}Bro, i'm nerovus{/cps}"
    m "{cps=20}Why, the atomsphere is fun and exciting!{/cps}"
    u "{cps=20}It's my first time, and I've never attended a previous version of it{/cps}"
    m "{cps=20}Bruh, you know that's my first time too ...{/cps}"
    m "{cps=20}Everything has a first time.{/cps}"
    show minas h at right
    u "{cps=20}What IF I LOSE ?!{/cps}"
    u "{cps=20}I hate lose you know.{/cps}"
    m "{cps=20}It's okay bro, I trust in you ...{/cps}"
    m "{cps=20}I hope we're on the same team.{/cps}"
    show userkaf h at left
    play sound sfx_amazed
    V "{cps=10}Silence!{/cps}"
    stop music fadeout 1.0
    show userkaf h at left, hideFade with dissolve
    hide userkaf h
    play sound sfx_disappear

    show minas h at right, hideFade with dissolve
    hide minas h
    play sound sfx_disappear

    pause 1.0

    $ dwp = 0
    jump drawp

    return

label square2:
    scene bg square with pixellate
    play music music_crowd fadein 1.0
    pause 1.0

    play sound sfx_appear
    show userkaf n at left, showFade
    pause 1.0

    "Crowd " "{cps=20}HERE HERE, a fourth is here!{/cps}"
    
    play sound sfx_confusion
    show userkaf c at left
    u "{cps=20}What's happening?!{/cps}"

    play sound sfx_appear
    show minas c at right, showFade

    m "{cps=20}Userkaf !!!{/cps}"
    m "{cps=20}Why are you that late??{/cps}"
    u "{cps=20}Tell me what's the matter?{/cps}"
    m "{cps=20}We were 43 and 3 of us wouldn't share because we should be 4s {/cps}"
    show userkaf n at left

    u "{cps=20}Aha, I see{nw}{/cps}"

    stop music fadeout 1.0
    play sound sfx_amazed
    V "{cps=10}SILENCE !{/cps}"

    show userkaf n at left, hideFade with dissolve
    hide userkaf n
    play sound sfx_disappear

    show minas n at right, hideFade with dissolve
    hide minas n
    play sound sfx_disappear

    pause 1.0

    $ dwp = 1
    jump drawp

    return

label square1n:

    play music3 music_faint fadein 1.0

    with Fade(0.1, 0.1, 1.0)
    V "{cps=10}All of us know why we are gathering here ...{/cps}"
    with Fade(0.4, 0.1, 1.0)
    V "{cps=10}Peret Festival is after 3 days ...{/cps}"

    stop music fadeout 1.0
    stop music2 fadeout 1.0
    stop music3 fadeout 1.0
    pause 1.0
    play sound sfx_faintdrop
    scene black
    $ pau(1.0)
    play sound sfx_slowheartbeats
    $ pau(5.0)

    play music crowd
    scene bg square

    play sound sfx_appear
    show udad s at p3
    show userkaf c at p2
    show umom s at p1
    show minas s at p4
    play sound sfx_confusion
    ud "{cps=20}Userkaf !{/cps}"
    ud "{cps=20}Are you okay?{/cps}"
    u "{cps=20}What happened?{/cps}"
    ud "{cps=20}You fainted.{/cps}"
    um "{cps=20}Have you eaten?{/cps}"
    show umom n at p1
    u "{cps=20}Actually not.{/cps}"
    um "{cps=20}I told you to eat.{/cps}"
    show udad h at p3
    ud "{cps=20}You won't just find someone with food in the street.{/cps}"
    show minas n at p4
    m "{cps=20}Who knows.{/cps}"

    pause 1.0
    show umom n at p1, hideFade with dissolve
    hide umom n
    play sound sfx_disappear

    show userkaf n at p2, hideFade with dissolve
    hide userkaf n
    play sound sfx_disappear

    show udad h at p3, hideFade with dissolve
    hide udad h
    play sound sfx_disappear

    show minas n at p4, hideFade with dissolve
    hide minas n
    play sound sfx_disappear

    pause 1.0


    jump drawp

    return

label drawp:
    stop music fadeout 1.0
    play sound sfx_appear
    
    show cheif at center, showFade

    play music2 music_official fadein 1.0
    

    if dwp == 0:
        V "{cps=10}There are 44 piece of papyrus in here ...{/cps}"
        V "{cps=10}Each one has a number ...{/cps}"
        V "{cps=10}Same numbers come in same team ...{/cps}"
        V "{cps=10}And the bolded number is the team leader ...{/cps}"
        V "{cps=10}Leader can give the lead to another one if he wants ...{/cps}"
    
    if dwp == 1:
        V "{cps=10}Add more 4 pieces ...{/cps}"
    
    V "{cps=10}AND LET THE DRAW BEGIN !{/cps}"
    
    "{cps=20}Draw a paper ...{/cps}"

    menu:
        "Draw a paper ..."

        "DRAW":
            $ dN = 7
        "DRAW":
            $ dN = 1

        "DRAW":
            $ dN = 11

        "DRAW":
            $ dN = 4

    play sound sfx_paper
    pause 1.0

    play sound sfx_magic
    "{cps=20}You got number [dN] !{/cps}"
    pause 1.0

    V "{cps=10}Gather togther teams ...{/cps}"
    V "{cps=10}Be ready ...{/cps}"
    V "{cps=10}No one knows tommorow ...{/cps}"
    V "{cps=10}See you on festival day.{/cps}"

    show cheif at center, hideFade with dissolve
    hide cheif
    play sound sfx_disappear

    stop music2 fadeout 1.0
    play music music_crowd fadein 1.0
    pause 1.0

    play sound sfx_sun
    show sun onlayer master zorder 100 at truecenter, showFade
    pause 1.0

    "A soft voice" "{cps=20}Team [dN]? Team [dN]?{/cps}"
    "Another voice" "{cps=20}Hey I have a [dN] here.{/cps}"

    play sound sfx_appear
    show userkaf h at p2, showFade
    pause 1.0

    play sound sfx_appear
    show eya h at p3, showFade
    play sound sfx_appear
    show tausert h at p4, showFade

    u "{cps=20}I'm in team [dN] too{/cps}"
    e "{cps=20}Oh hello !{/cps}"
    u "{cps=20}Hello !{/cps}"
    e "{cps=20}I'm Eya and you?{/cps}"
    t "{cps=20}I'm Tausert.{/cps}"
    u "{cps=20}Userkaf.{/cps}"

    play sound sfx_appear
    show minas c at p1, showFade

    pause 1.0

    m "{cps=20}Bro, what have you got?{/cps}"
    u "{cps=20}A [dN], you?{/cps}"
    
    show minas c at p1, hideFade with dissolve
    hide minas c
    play sound sfx_disappear


    u "{cps=20}Minas where are you going !{/cps}"
    e "{cps=20}Who's that?{/cps}"
    u "{cps=20}My friend, we knew eachothers since childhood.{/cps}"
    t "{cps=20}One is missing now.{/cps}"
    e "{cps=20}Guys who's team 3?{/cps}"
    play sound sfx_appear
    show minas h at p1, showFade
    pause 1.0


    u "{cps=20}Minas what's going on ?!{/cps}"
    m "{cps=20}Nothing, I was checking something ...{/cps}"
    m "{cps=20}I'm the fourth.{/cps}"
    e "{cps=20}Great, we're complete now.{/cps}"
    u "{cps=20}Who's the leader?{/cps}"
    e "{cps=20}The one who has the bolded number.{/cps}"
    m "{cps=20}Who has it?{/cps}"
    e "{cps=20}Oh, it's Userkaf!{/cps}"
    u "{cps=20}Oh that's a responsibilty.{/cps}"
    t "{cps=20}The sun is so hot, let's find another place.{/cps}"
    u "{cps=20}I know a quiet place.{/cps}"
    m "{cps=20}Aha, I got you.{/cps}"
    u "{cps=20}You know it of course.{/cps}"
    e "{cps=20}Okay let's go.{/cps}"

    pause 1.0

    show minas h at p1, hideFade with dissolve
    hide minas h
    play sound sfx_disappear

    show userkaf h at p2, hideFade with dissolve
    hide userkaf h
    play sound sfx_disappear

    show eya h at p3, hideFade with dissolve
    hide eya h
    play sound sfx_disappear

    show tausert h at p4, hideFade with dissolve
    hide tausert h
    play sound sfx_disappear

    stop music fadeout 1.0
    jump palm1

    return

label palm1:
    scene bg palm1 with pixellate
    play music music_rivermorning fadein 1.0
    pause 1.0

    play sound sfx_appear
    show userkaf n at p2, showFade
    pause 0.5
    play sound sfx_appear
    show minas n at p1, showFade
    show tausert h at p4, showFade
    pause 1.0

    play sound sfx_appear

    show eya h at p3, showFade
    $ pau(1.0)
    play sound sfx_love
    show userkaf b at p2

    play sound sfx_fastheartbeats
    # u2 "She's so beautiful!"
    $ pau(5.0)

    play sound sfx_confusion
    show eya c at p3
    e "{cps=20}Why are you silent?{/cps}"
    show userkaf n at p2
    u "{cps=20}Oh are we.{/cps}"
    show eya n at p3
    m "{cps=20}Soooo ...{/cps}"
    t "{cps=20}What will we be doing?{/cps}"
    m "{cps=20}No idea ...{/cps}"
    u "{cps=20}Eya ...{/cps}"
    show eya c at p3 
    e "{cps=20}Yes?{/cps}"
    show userkaf h at p2
    menu:
        
        "Say 'You're so beautiful ...'":
            u "{cps=20}You're s—{nw}{/cps}" 
            play sound sfx_fall
            show userkaf s at p2 with vpunch
            "A DATE FALLS ON HIS HEAD"
            show minas h at p1
            show eya h at p3
            show tausert h at p4
            "All laughs"
        
        "Say 'No nevermind.'":
            u "{cps=20}No nevermind.{/cps}"

    show minas n at p1
    show userkaf n at p2
    show eya n at p3
    show tausert n at p4

    pause 1.0
    t "{cps=20}I think we're all tired, let's meet tommorow better.{/cps}"
    m "{cps=20}Agree.{/cps}"
    u "{cps=20}Same place?{/cps}"
    e "{cps=20}Yes LEADER!{/cps}"
    show userkaf h at p2
    u "{cps=20}Okay, good luck all.{/cps}"

    show minas h at p1, hideFade with dissolve
    hide minas h
    play sound sfx_disappear

    show userkaf h at p2, hideFade with dissolve
    hide userkaf h
    play sound sfx_disappear

    show eya h at p3, hideFade with dissolve
    hide eya h
    play sound sfx_disappear

    show tausert h at p4, hideFade with dissolve
    hide tausert h
    play sound sfx_disappear

    pause 1.0
    stop music fadeout 1.0

    if smeet == 0:
        jump out3
    jump room3

    return

label out3:
    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    scene bg street1 e with pixellate
    play music music_wind fadein 1.0
    pause 1.0
    play sound sfx_appear
    show userkaf n at left, showFade
    pause 1.0

    show stranger at right, showFade
    play sound sfx_sudden
    play music2 music_weird fadein 1.0
    pause 1.0

    ss "{cps=20}Hey kid! How are you?{/cps}"
    pause 1.0

    menu:
        "I'm fine.":
            show userkaf h at left
            u "{cps=20}I'm fine and you?{/cps}"

        "Who are you?":
            show userkaf c at left
            u "{cps=20}Who are you?{/cps}"
            ss "{cps=20}I don't know...{/cps}"
            ss "{cps=20}I just wanted to ask.{/cps}"
            show userkaf h at left
            u "{cps=20}Mhm, I'm find and you?{/cps}"

    ss "{cps=20}I'm doing good I guess.{/cps}"
    u "{cps=20}Nice to meet you sir.{/cps}"
    ss "{cps=20}Where are you going?{/cps}"

    menu:
        "Not your business.":
            show userkaf a at left
            u "{cps=20}Not your business.{/cps}"
            ss "{cps=20}Chill kid chill.{/cps}"
            show userkaf n at left

        "I'm going home":
            show userkaf n at left
            u "{cps=20}I'm going home.{/cps}"

    ss "{cps=20}Okay, good luck.{/cps}"
    show userkaf n at left, hideFade with dissolve
    hide userkaf n
    play sound sfx_disappear

    pause 1.0
    stop music fadeout 1.0
    stop music2 fadeout 1.0

    play sound sfx_out
    jump room3


    return


label room3:
    scene bg ubd2 with pixellate

    play sound sfx_appear
    show userkaf n at left, showFade
    pause 1.0

    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            play sound sfx_disappear

            pause 1.0

            scene bg ubd2 at showBlur
            
            show mirror2 with dissolve
            play sound sfx_magic

            u "{cps=20}What that weird feeling??!{/cps}"


            show mirror2 at hideFade with dissolve
            hide mirror2
            play sound sfx_disappear
            jump room3


        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            play sound sfx_disappear
            pause 1.0
            play sound sfx_out
            jump kit3

        "Sleep":
            play sound sfx_sleep
            jump day2




    return

label kit3:
    scene bg kitchen2 with pixellate
    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear

    pause 1.0
    
    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump kit3

    
        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            play sound sfx_disappear
            pause 1.0
            play sound sfx_out
            jump room4
        
    

    return    

label room4:
    scene bg ubd3 with pixellate
    show userkaf n at left, showFade
    play sound sfx_appear

    pause 1.0

    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            play sound sfx_disappear
            pause 1.0

            scene bg ubd3 at showBlur
            
            show mirror3 with dissolve
            play sound sfx_magic

            u "{cps=20}I'm very sleepy.{/cps}"


            show mirror3 at hideFade with dissolve
            hide mirror3
            play sound sfx_disappear

            jump room4


        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            play sound sfx_disappear
            pause 1.0

            play sound sfx_out
            jump kit4

        "Sleep":
            play sound sfx_sleep
            jump day2
            




    return

label kit4:
    scene bg kitchen3 with pixellate
    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0
    
    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump kit4

    
        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            hide userkaf n
            play sound sfx_disappear
            pause 1.0
            play sound sfx_out
            jump room4
        
    

    return    
