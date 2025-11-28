default d5s3c = 0
default d5sc1 = ""
default d5sc0 = ""
default ds5 = 0

label day5:
    $ renpy.music.set_volume(1, delay=0, channel='music')
    $ renpy.music.set_volume(0.4, delay=0, channel='music2')
    scene black with dissolve
    pause 5.0
    if temtem == 0:
        jump d5r0
    else:
        jump d5r1

    return

label d5r0:
    scene bg ubd1 with pixellate
    if(ds5 == 0):
        $ ds5 = 1
        play sound sfx_rooster
        $ pau(2.0)
    play music music_morning fadein 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0


    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg ubd1 at showBlur
            play sound sfx_magic
            
            show mirror1 with dissolve

            u "{cps=20}I have to meet the team.{/cps}"


            show mirror1 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror1
            jump d5r0

        "Check Eya's paper":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg ubd1 at showBlur
            play sound sfx_paper
            
            show expression papyrusN with dissolve

            " "


            show expression papyrusN at hideFade with dissolve
            play sound sfx_disappear
            hide expression papyrusN
            jump d5r0

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5k0

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5s0


    return

label d5k0:
    scene bg kitchen1 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d5k0

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5r0

    return

label d5s0:
    scene bg street1 m with pixellate
    play music music_morning fadein 1.0
    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Go back home":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5r0
        "Go to the palm tree":
            $ d5sc0 = "palm"
            jump d5p0
        "Go to the square":
            $ d5sc0 = "square"
            jump d5sp1
        # "Go to Eya":
        #     $ d5sc0 = "eya"
        #     jump d5sp1


    return

label d5sp1:
    show userkaf n at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0

    if d5sc0 == "square":
        scene bg square with pixellate
        play music music_wind fadein 1.0
    elif d5sc0 == "eya":
        scene bg eya m with pixellate
        play music music_morning fadein 1.0


    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    if d5sc0 == "square":
        u "{cps=20}They haven't started yet.{/cps}"
    
    else:
        u "{cps=20}Nothing to do here.{/cps}"
    
    menu:
        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5s0

    return

label d5p0:

    scene bg palm1 with pixellate
    play music music_rivermorning fadein 1.0
    pause 1.0
    show userkaf n at p2, showFade
    play sound sfx_appear
    pause 1.0
    show minas n at p1, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Hi.{/cps}"
    e "{cps=20}Hi.{nw}{/cps}"
    t "{cps=20}Hi.{nw}{/cps}"
    m "{cps=20}Hi.{/cps}"
    u "{cps=20}Guys.{/cps}"
    e "{cps=20}Yes?{/cps}"
    u "{cps=20}I want to go to the temple.{/cps}"
    m "{cps=20}Now?{/cps}"
    e "{cps=20}Yess.{/cps}"
    t "{cps=20}Why not.{/cps}"
    e "{cps=20}Okay.{/cps}"

    show userkaf n at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    show minas n at p1, hideFade with dissolve
    play sound sfx_disappear
    hide minas n
    show eya n at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya n
    show tausert n at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert n

    jump d5s00


    return

label d5s00:
    scene bg street3 with pixellate
    play music music_jungle fadein 1.0

    pause 1.0
    show userkaf n at p2, showFade
    play sound sfx_appear
    show minas n at p1, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Let's enter.{/cps}"
    m "{cps=20}Are you sure?{/cps}"
    u "{cps=20}Yes.{/cps}"

    show userkaf n at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    show minas n at p1, hideFade with dissolve
    play sound sfx_disappear
    hide minas n
    show eya n at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya n
    show tausert n at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert n

    jump d5t0

    return

label d5t0:
    scene bg temple1 with pixellate
    play music music_temple fadein 1.0
    pause 1.0

    

    show minas z at p1, showFade
    play sound sfx_appear
    show eya z at p2, showFade
    play sound sfx_appear
    show userkaf z at p3, showFade
    play sound sfx_appear
    show tausert z at p4, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Finally we're here.{/cps}"

    play sound sfx_temple1
    scene bg temple2 with pixellate
    play music music_temple fadein 1.0

    show userkaf z at p3 
    show tausert z at p4
    show minas z at p1
    show eya z at p2

    e "{cps=20}Oh my God!{/cps}"
    show minas a at p1
    m "{cps=20}Are you happy now?{/cps}"
    show eya a at p2
    e "{cps=20}YOU MADE US LOSE USERKAF ...{/cps}"
    e "{cps=20}I HATE YOU.{/cps}"
    show userkaf s at p3

    u "{cps=20}I'm sor—{nw}{/cps}" 
    u "—" nointeract
    play sound sfx_push
    show userkaf a at p3 with vpunch
    show minas d at p3
    show eya z at p1 
    
    m "{cps=20}Don't you speak.{/cps}"

    menu:
        "Kick him":
            show minas z at p2 with vpunch
            show userkaf d at p3
            play sound sfx_push
            pause 1.0
            play sound sfx_colapse
            scene black
            $ pau(2) 
            
            scene bg temple3 with vpunch

            show userkaf z at p3 
            show tausert z at p4
            show minas z at p2
            t "{cps=20}IT FELL ON EYA.{/cps}"
            m "{cps=20}YOU MADE US LOSE.{/cps}"
            m "{cps=20}YOU KILLED EYA.{/cps}"
            m "{cps=20}YOU KILLED HER USERKAF.{/cps}"
            play sound sfx_rewind
            scene black
            $ pau(2)

            jump d5r1


    return

label d5r1:
    scene bg ubd1 with pixellate
    play music music_morning fadein 1.0

    if temtem == 0:
        $ temtem = 1
        m "{cps=20}YOU KILLED HER USERKAF.{/cps}"
        um "{cps=20}USERKAF ...{/cps}"
        show umom at left, showFade
        play sound sfx_appear
        um "{cps=20}Are you okay ?{/cps}"
        show userkaf s at right, showFade
        play sound sfx_appear
        

        menu:
            "I'm okay.":
                u "{cps=20}I'm okay ...{/cps}"
                u "{cps=20}Just a bad dream.{/cps}"
                
        um "{cps=20}Okay Userkaf ...{/cps}"
        um "{cps=20}I'm here if you need something.{/cps}"
        show umom at left, hideFade with dissolve
        play sound sfx_disappear
        hide umom
        pause 1.0
        u "{cps=20}It's just a dream.{/cps}"
        show userkaf n at right, hideFade with dissolve
        play sound sfx_disappear
        hide userkaf n

        
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0


    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg ubd1 at showBlur
            play sound sfx_magic
            
            show mirror1 with dissolve

            u "{cps=20}I hope she reads it.{/cps}"


            show mirror1 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror1
            jump d5r1

        "Check Eya's paper":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg ubd1 at showBlur
            play sound sfx_paper
            
            show expression papyrusN with dissolve

            " "


            show expression papyrusN at hideFade with dissolve
            play sound sfx_disappear
            hide expression papyrusN
            jump d5r1

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5k1

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5s1

    return

label d5k1:
    scene bg kitchen1 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d5k1

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5r1

    return

label d5s1:
    scene bg street1 m with pixellate
    play music music_morning fadein 1.0
    pause 1.0

    show userkaf n at left, showFade
    play sound sfx_appear


    menu:
        "Go back home":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5r1
        "Go to the palm tree":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5p1
        "Go to the square":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5q1
        #"Go to the temple":
        #    show userkaf n at left, hideFade with dissolve
        #    hide userkaf n
        #    jump d5s2

    return

label d5p1:
    scene bg palm1 with pixellate
    play music music_rivermorning fadein 1.0
    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Nothing to do here.{/cps}"
    menu:
        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5s1
        
    return

label d5s2:
    scene bg street3 with pixellate
    play music music_jungle fadein 1.0

    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Nothing to do here.{/cps}"
    menu:
        "Enter the temple":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5t1
        
        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5s1
        
    return

label d5t1:
    scene bg temple1 with pixellate
    play music music_temple fadein 1.0

    pause 1.0
    show userkaf z at center, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Mhm.{/cps}"
    menu:
        "Go back":
            show userkaf z at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf z
            pause 1.0
            jump d5s2
        
    return

label d5q1:
    scene bg square with pixellate
    play music music_wind fadein 1.0

    pause 1.0

    show minas h at p1, showFade
    play sound sfx_appear

    show userkaf h at p2, showFade
    play sound sfx_appear
    show eya h at p3, showFade
    play sound sfx_appear
    show tausert h at p4, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Hello friends.{/cps}"
    e "{cps=20}Hi.{/cps}{nw}"
    m "{cps=20}Hey.{/cps}{nw}"
    t "{cps=20}Hello.{/cps}"

    e "{cps=20}He's gonna talk shush.{/cps}"
    pause 1.0

    show minas h at p1, hideFade with dissolve
    play sound sfx_disappear
    hide minas h
    show userkaf h at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf h

    show eya h at p3, hideFade with dissolve
    hide eya h
    play sound sfx_disappear

    show tausert h at p4, hideFade with dissolve
    hide tausert h
    play sound sfx_disappear

    pause 1.0
    show cheif at center, showFade
    play sound sfx_appear
    
    V "{cps=10}Welcome again ...{/cps}"
    V "{cps=10}The true games start today ...{/cps}"
    V "{cps=10}We're having senet and archery today ...{/cps}"
    V "{cps=10}2 of each team will play one game of these ...{/cps}"
    V "{cps=10}Good luck kids.{/cps}"

    pause 1.0
    show cheif at center, hideFade with dissolve
    play sound sfx_disappear
    hide cheif
    pause 1.0

    show minas h at p1, showFade
    play sound sfx_appear

    show userkaf h at p2, showFade
    play sound sfx_appear
    show eya h at p3, showFade
    play sound sfx_appear
    show tausert h at p4, showFade
    play sound sfx_appear
    pause 1.0


    e "{cps=20}Me and Userkaf will go for senet.{/cps}"
    e "{cps=20}Minas and Tausert go for archery.{/cps}"
    "{cps=20}Okay leader.{/cps}"

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

    pause 1.0
    jump d5q2

    return

label d5q2:
    scene bg sq2 with pixellate
    play music music_wind fadein 1.0

    pause 1.0

    show userkaf n at left, showFade
    play sound sfx_appear
    show eya n at right, showFade
    play sound sfx_appear
    pause 1.0


    show userkaf h at left
    u "{cps=20}Good luck Eya.{/cps}"
    show eya h at right
    u "{cps=20}You too!{/cps}"
    if efd == 0:
        show userkaf n at left
        u "{cps=20}Have you seen the temple?{/cps}"
        e "{cps=20}The one you wanted to explore?{/cps}"
        show eya n at right
        u "{cps=20}Yes .. I had a bad dream about it.{/cps}"
        e "{cps=20}And then you go to explore it?!!{/cps}"
        u "{cps=20}There'e something inside it!{/cps}"
        e "{cps=20}Something like what?{/cps}"
        u "{cps=20}I don't know .. but we'll discover.{/cps}"

    e "{cps=20}It's our turn let's play.{/cps}"
    pause 1.0

    scene black with dissolve
    pause 2.0
    "{cps=20}A few minutes later ...{/cps}"
    scene bg sq2 with pixellate
    pause 1.0


    show userkaf n at left, showFade
    play sound sfx_appear
    show eya s at right, showFade
    play sound sfx_appear
    pause 1.0

    
    u "{cps=20}What's wrong Eya?.{/cps}"
    show userkaf s at left
    e "{cps=20}I lost.{/cps}"
    u "{cps=20}It's okay .. it happens to all.{/cps}"
    e "{cps=20}I hope the others won.{/cps}"

    pause 1.0
    show userkaf n at p1
    show eya n at p2
    pause 1.0

    show tausert n at p3, showFade
    play sound sfx_appear
    show minas n at p4, showFade
    play sound sfx_appear


    u "{cps=20}What did you do guys?{/cps}"
    m "{cps=20}2 points !{/cps}"
    m "{cps=20}And you?{/cps}"
    e "{cps=20}1 point.{/cps}"

    menu:
        "Refer that Eya lost":
            e "{cps=20}I lost.{/cps}"
            show tausert h at p3
            t "{cps=20}Ohh .. that's okay Eya.{/cps}"
            show eya h at p2
            e "{cps=20}I love you.{/cps}"

        "Lie about Eya's lose":
            u "{cps=20}I lost.{/cps}"
            e "{cps=20}Hu—{nw}{/cps}"
            e "—" nointeract
            show eya b at p2
            u "{cps=20}Shush.{/cps}"
            m "{cps=20}No problem bro .. don't worry.{/cps}"

    pause 1.0
    show userkaf n at p1, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    show eya n at p2, hideFade with dissolve
    play sound sfx_disappear
    hide eya n
    show tausert n at p3, hideFade with dissolve
    play sound sfx_disappear
    hide tausert n
    show minas at p4, hideFade with dissolve
    play sound sfx_disappear
    hide minas n

    pause 1.0
    jump d5q3

    return


label d5q3:
    scene bg square with pixellate
    play music music_wind fadein 1.0

    pause 1.0

    show cheif at center, showFade
    play sound sfx_appear
    pause 1.0

    V "{cps=10}Well done kids ...{/cps}"
    V "{cps=10}We've gathered your points ...{/cps}"
    V "{cps=10}And we're eliminating the least two teams ...{/cps}"
    V "{cps=10}Good luck tomorrow.{/cps}"

    pause 1.0
    show cheif at center, hideFade with dissolve
    play sound sfx_disappear
    hide cheif
    pause 1.0

    if mfd == 0:
        show userkaf h at p2, showFade
        play sound sfx_appear
        show minas h at p1, showFade
        play sound sfx_appear
        pause 1.0

        m "{cps=20}Good job bro.{/cps}"
        show minas n at p1
        show userkaf n at p2, showFade
        play sound sfx_appear
        u "{cps=20}Minas ...{/cps}"
        u "{cps=20}I dreamt that we fought in that temple.{/cps}"
        m "{cps=20}What's your problem with it?{/cps}"
        u "{cps=20}There's something in it believe me Minas.{/cps}"
        m "{cps=20}Of course there are ...{/cps}"
        m "{cps=20}Pillars and sculptures.{/cps}"
        u "{cps=20}Shut up.{/cps}"
        show minas h at p1
        m "{cps=20}Haha.{/cps}"
        pause 1.0

    else:
        show userkaf n at p2, showFade
        play sound sfx_appear
        show minas n at p1, showFade
        play sound sfx_appear

    show eya n at p3, showFade
    play sound sfx_appear

    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    e "{cps=20}Are you going to the Palm guys?{/cps}"

    menu:
        "Yes":
            u "{cps=20}Yes.{/cps}"
            e "{cps=20}Let's go.{/cps}"
            m "{cps=20}I'm not coming.{/cps}"
            u "{cps=20}Okay see you later.{/cps}"
            show minas n at p1, hideFade with dissolve
            play sound sfx_disappear
            hide minas n
            pause 1.0

            show userkaf n at p2, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            show eya n at p3, hideFade with dissolve
            play sound sfx_disappear
            hide eya n
            show tausert n at p4, hideFade with dissolve
            play sound sfx_disappear
            hide tausert n
            pause 1.0
            jump d5p2

    return

label d5p2:
    scene bg palm1 with pixellate
    play music music_rivermorning fadein 1.0
    pause 1.0
    show userkaf n at p2, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear

    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    t "{cps=20}What are we going to do?{/cps}"
    u "{cps=20}I don't know.{/cps}"
    e "{cps=20}Wanna have some action?{/cps}"
    t "{cps=20}Of course.{/cps}"
    e "{cps=20}Let's  go to that temple.{/cps}"
    u "{cps=20}I support.{/cps}"
    pause 1.0
    show userkaf n at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    show eya n at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya n
    show tausert n at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert n
    pause 1.0
    jump d5st2
    return

label d5st2:
    scene bg street3 with pixellate
    play music music_jungle fadein 1.0
    pause 1.0
    show userkaf n at p2, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    show tausert c at p4
    t "{cps=20}Are you sure you're gonna enter?{/cps}"
    show userkaf h at p2
    u "{cps=20}Yessss.{nw}{/cps}"
    show eya h at p3
    e "{cps=20}Yes Tausert!{/cps}"
    show tausert n at p4
    t "{cps=20}I'm kinda scared .. I'll stay here.{/cps}"
    e "{cps=20}As you like.{/cps}"
    e "{cps=20}Let's go Userkaf.{/cps}"
    u "{cps=20}Okay.{/cps}"
    pause 1.0 
    show userkaf n at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    show eya n at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya n
    pause 1.0 
    jump d5t2

    return

label d5t2:
    scene bg temple1 with pixellate
    play music music_temple fadein 1.0
    pause 1.0
    show userkaf z at p2, showFade
    play sound sfx_appear
    show eya h at p3, showFade
    play sound sfx_appear
    pause 1.0

    e "{cps=20}It's just an empty room.{nw}{/cps}"
    u "{cps=20}Exactly as in the dream.{/cps}"
    show userkaf h at p2
    e "{cps=20}Who do you think built it?{/cps}"
    u "{cps=20}It looks old so maybe 2 families ago?{/cps}"
    e "{cps=20}We can ask the Cheif later.{/cps}"
    show eya n at p3
    u "{cps=20}Mhm.{nw}{/cps}"
    show userkaf n at p2
    show eya c at p3
    u "{cps=35}Anyways stay away from that pillar.{/cps}"
    show eya n at p3
    e "{cps=20}Of course it's going to break.{/cps}"

    show eya c at p3
    show userkaf c at p2
    play sound sfx_run
    t "{cps=30}Guys ...{nw}{/cps}"
    t "{cps=30}Guys!{nw}{/cps}"
    show tausert s at p4
    e "{cps=30}What's wrong?{nw}{/cps}"
    t "{cps=30}Something ..{nw}{/cps}"
    t "{cps=30}Someone ..{nw}{/cps}"
    t "{cps=30}I don't know ..{nw}{/cps}"
    show userkaf a at p2
    play sound sfx_amazed
    u "{cps=40}CALM DOWN TAUSERT!{/cps}"
    show userkaf n at p2
    show eya n at p3
    e "{cps=20}It's okay we're here{/cps}"
    t "{cps=20}I think I saw a monster.{/cps}"
    e "{cps=20}Huh?{/cps}"
    u "{cps=20}In the morning!{/cps}"
    e "{cps=20}What did it look like?{/cps}"
    t "{cps=20}It came out of trees then I ran .. I couldn't see it well.{/cps}"
    u "{cps=20}Maybe it was a homeless?{/cps}"
    t "{cps=20}I don't think so, it seemed agressive.{/cps}"
    e "{cps=20}I think we should move now.{nw}{/cps}"
    t "{cps=20}I wanna go home.{/cps}"
    e "{cps=20}Userkaf can you come with us?{/cps}"

    menu:
        "Yes":
            u "{cps=20}Sure Eya.{/cps}"
            pause 1.0 
            show userkaf n at p2, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            show eya n at p3, hideFade with dissolve
            play sound sfx_disappear
            hide eya n
            show tausert n at p4, hideFade with dissolve
            play sound sfx_disappear
            hide tausert n
            pause 1.0 
            jump d5eh1

    return

label d5eh1:
    scene bg eya m with pixellate
    play music music_morning fadein 1.0
    pause 1.0
    show userkaf n at p4, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert s at p2, showFade
    play sound sfx_appear
    pause 1.0

    show eya h at p3
    e "{cps=20}Thanks Userkaf.{/cps}"
    show userkaf h at p4
    u "{cps=20}Welcome!{/cps}"
    show eya n at p3
    show userkaf n at p4
    u "{cps=20}Are you better Tasuert?{/cps}"
    t "{cps=20}I think so.{/cps}"
    t "{cps=20}I'm going home .. see you later.{/cps}"
    u "{cps=20}Bye. {nw}{/cps}"
    e "{cps=20}Bye.{/cps}"
    pause 1.0

    show tausert n at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert n
    pause 1.0

    e "{cps=20}What do you see?{/cps}"
    u "{cps=20}It might be an animal or something.{/cps}"
    e "{cps=20}I don't think so .. {nw}{/cps}"
    e "{cps=20}She was terrified!{/cps}"
    show userkaf c at p4
    u "{cps=20}What if it's something distancing us from the temple?{/cps}"
    show eya c at p3
    e "{cps=20}Why so?{/cps}"
    show userkaf n at p4
    u "{cps=20}Protecting its secret!{/cps}"
    show eya n at p3
    e "{cps=20}You're convincing me now Userkaf.{/cps}"
    show userkaf h at p4
    u "{cps=20}Haha.{/cps}"
    show userkaf n at p4
    e "{cps=20}Will you go again?{/cps}"
    u "{cps=20}Of course I will.{/cps}"
    e "{cps=20}Bruh.{/cps}"
    e "{cps=20}Don't go alone.{/cps}"
    u "{cps=20}Sure.{/cps}"
    show eya c at p3

    e "{cps=20}What's that letter!{/cps}"
    show userkaf c at p4
    u "{cps=20}What letter?{/cps}"
    e "{cps=20}Here beside the house.{/cps}"
    show userkaf n at p4
    u "{cps=20}Ohh I saw it.{/cps}"
    show eya n at p3
    show userkaf c at p4
    u "{cps=20}What's written?{/cps}"
    e "{cps=20}I don't know .. I'll read it later.{/cps}"
    show userkaf n at p4
    u "{cps=20}Mhm.{/cps}"
    u "{cps=20}Anyways .. I'm going home.{/cps}"
    u "{cps=20}Take care.{/cps}"
    e "{cps=20}You too.{/cps}"

    pause 1.0
    show userkaf n at p4, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0

    jump d5s30

    return

label d5s3chat:

    u "{cps=20}Hi Stranger.{/cps}"
    ss "{cps=20}Hello kid.{/cps}"
    show userkaf c at left
    u "{cps=20}Have you ever heard about a MONSTER?{/cps}"
    ss "{cps=20}A monster? {nw}{/cps}"
    show userkaf s at left
    ss "{cps=20}Yeah yeah.{/cps}"
    u "{cps=20}Oh my God, really?{/cps}"
    ss "{cps=20}Yess.{/cps}"
    show userkaf n at left
    u "{cps=20}How does it look like?{/cps}"
    ss "{cps=20}Umm..{nw}{/cps}"
    show userkaf c at left
    ss "{cps=20}I don't know.{/cps}"
    show userkaf n at left
    u "{cps=20}You seen it before?{/cps}"
    ss "{cps=20}Yeah many times .. but I couldn't see him well.{nw}{/cps}"
    show userkaf c at left
    ss "{cps=20}How is Eya?{/cps}"
    u "{cps=20}She is good?{/cps}"
    show userkaf n at left
    ss "{cps=20}I mean how's your love.{/cps}"
    u "{cps=20}We're good.{/cps}"
    u "{cps=20}Yesterday .. I wrote a letter for her.{/cps}"
    ss "{cps=20}What did you write?{/cps}"
    u "{cps=20}A confess letter.{/cps}"
    ss "{cps=20}Oh that's brave.{/cps}"
    show userkaf c at left
    ss "{cps=20}But why didn't you write your name on it?{/cps}"
    u "{cps=20}Huh?{nw}{/cps}"
    u "{cps=20}How you know?{/cps}"
    show userkaf n at left
    ss "{cps=20}Just guessing kid CHILL.{/cps}"
    u "{cps=20}Okay.{/cps}"
    u "{cps=20}Evening is entering .. I'm going.{/cps}"
    ss "{cps=20}Sure see you later.{/cps}"
    pause 1.0
    show stranger at right, hideFade with dissolve
    play sound sfx_disappear
    hide stranger
    pause 1.0
    jump d5s3

label d5s30:
    scene bg street1 m with pixellate
    play music music_morning fadein 1.0
    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    if d5s3c == 0:
        show stranger at right, showFade
        play sound sfx_appear
        pause 1.0
        $ d5s3c = 1
        call d5s3chat

    return


label d5s3:
    if d5s3c == 0:
        scene bg street1 e with pixellate
        play music music_wind fadein 1.0
    else:
        scene bg street1 e with pixellate
        play music music_wind fadein 1.0
    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    if d5s3c == 0:
        show stranger at right, showFade
        play sound sfx_appear
        pause 1.0
        $ d5s3c = 1
        call d5s3chat

    
    menu:
        "Go back home":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5r2
        "Go to the palm tree":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5p3
        "Go to the square":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5q4
        "Go to Eya":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5eh2
        "Go to the temple":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5s4

    return

label d5p3:
    scene bg palm2 with pixellate
    play music music_riverevening fadein 1.0
    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Nothing to do here.{/cps}"
    menu:
        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5s3
        
    return

label d5q4:
    scene bg square2 with pixellate
    play music music_wind fadein 1.0
    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Nothing to do here.{/cps}"
    menu:
        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5s3
        
    return

label d5s4:
    scene bg street3 e with pixellate
    play music music_jungle fadein 1.0
    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Nothing to do here.{/cps}"
    menu:
        "Enter the temple":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5t3
        
        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5s3
        
    return

label d5t3:
    scene bg temple1 with pixellate
    play music music_temple fadein 1.0

    pause 1.0
    show userkaf z at center, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}What is you secret?{/cps}"
    menu:
        "Go back":
            show userkaf z at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf z
            pause 1.0
            jump d5s4
        
    return

label d5r2:
    scene bg ubd2 with pixellate
    play music music_wind fadein 1.0

    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg ubd2 at showBlur
            play sound sfx_magic
            
            show mirror2 with dissolve

            u "{cps=20}I have to go to Eya.{/cps}"


            show mirror2 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror2
            jump d5r2

        "Check Eya's paper":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg ubd2 at showBlur
            play sound sfx_paper
            
            show expression papyrusN with dissolve

            u "{cps=20}I'm coming to you.{/cps}"


            show expression papyrusN at hideFade with dissolve
            play sound sfx_disappear
            hide expression papyrusN
            jump d5r2

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5k2

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5s3

    return

label d5k2:
    scene bg kitchen2 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d5k2

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5r2

    return

label d5eh2:

    scene bg eya e with pixellate
    play music music_wind fadein 1.0
    pause 1.0
    show userkaf n at right, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Eyaaa!{/cps}"
    u "{cps=20}Eyaaa!{/cps}"
    u "{cps=20}Eyaa {nw}{/cps}"
    e "{cps=20}I'M COMING!{/cps}"
    pause 1.0
    show eya a at left, showFade
    play sound sfx_appear
    e "{cps=20}YES?{/cps}"

    show eya c at left
    u "{cps=20}The monster is real.{/cps}"
    e "{cps=20}You saw it?{/cps}"
    show eya s at left
    u "{cps=20}No I asked someone.{/cps}"
    e "{cps=20}I'm getting scared for real.{/cps}"
    show eya n at left
    u "{cps=20}I wanna find it.{/cps}"
    show userkaf h at right
    e "{cps=20}Sure why not.{/cps}"
    show eya c at left
    u "{cps=20}Let's go then.{/cps}"
    show userkaf n at right
    e "{cps=20}I'm kidding boy.{/cps}"
    u "{cps=20}Bruh.{/cps}"
    show eya n at left
    e "{cps=20}Userkaf don't go alone.{/cps}"
    e "{cps=20}Specially in night.{/cps}"
    u "{cps=20}Don't worry Eya.{/cps}"
    show userkaf c at right
    show eya b at left
    u "{cps=20}Have you read the letter?{/cps}"
    e "{cps=10}Yes ...{/cps}"
    u "{cps=20}What was it?{nw}{/cps}"
    u "{cps=20}Why are you acting like that?{/cps}"
    u "{cps=10}It was a{w=0.1}{/cps}{cps=25} romantic letter.{/cps}"
    show userkaf h at right
    show eya n at left

    u "{cps=20}Interesting.{/cps}"
    show userkaf n at right
    u "{cps=20}Anyways I'm going home.{/cps}"
    show eya h at left
    u "{cps=20}Do you need something?{/cps}"
    show userkaf h at right
    e "{cps=20}Thank you, see you{/cps}"
    
    pause 1.0
    show userkaf h at right, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf h
    pause 1.0

    jump d5s5

    return

label d5s5:
    scene bg street1 n with pixellate
    play music music_night fadein 1.0
    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Go back home":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5r3
        "Go to the palm tree":
            $ d5sc1 = "palm"
            jump d5s5p
        "Go to the square":
            $ d5sc1 = "square"
            jump d5s5p
        "Go to Eya":
            $ d5sc1 = "eya"
            jump d5s5p
        #"Go to the temple":
        #    jump d5s4

    return

label d5s5p:
    show userkaf n at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0
    
    if d5sc1 == "palm":
        scene bg palm3 with pixellate
        play music music_rivernight fadein 1.0
    elif d5sc1 == "square":
        scene bg square3 with pixellate
        play music music_night fadein 1.0
    elif d5sc1 == "eya":
        scene bg eya n with pixellate
        play music music_night fadein 1.0


    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Nothing to do here.{/cps}"
    menu:
        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5s5

    return

label d5r3:
    scene bg ubd3 with pixellate
    play music music_night fadein 1.0

    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg ubd3 at showBlur
            play sound sfx_magic

            show mirror3 with dissolve

            u "{cps=20}I need to sleep.{/cps}"


            show mirror3 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror3
            jump d5r3

        "Check Eya's paper":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg ubd3 at showBlur
            play sound sfx_paper
            
            show expression papyrusN with dissolve

            u "{cps=20}I'll never throw it.{/cps}"


            show expression papyrusN at hideFade with dissolve
            play sound sfx_disappear
            hide expression papyrusN
            jump d5r3

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5k3

        "Sleep":
            scene black with dissolve
            pause 2.0
            play sound sfx_sleep
            jump day6

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d5s5

    return

label d5k3:
    scene bg kitchen3 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d5k3

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d5r3

    return
