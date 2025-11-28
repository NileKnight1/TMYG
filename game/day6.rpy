default d6sc = ""
default d6rc2 = 0
default d6s5chat = 0
default ds6 = 0


label day6:
    $ renpy.music.set_volume(1, delay=0, channel='music')
    $ renpy.music.set_volume(0.4, delay=0, channel='music2')
    jump d6r1

    return

label d6r1:

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

            u "{cps=20}I want to sleep.{/cps}"


            show mirror3 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror3
            jump d6r1

        "Check Eya's paper":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg ubd3 at showBlur
            play sound sfx_paper
            
            show expression papyrusN with dissolve

            " "


            show expression papyrusN at hideFade with dissolve
            play sound sfx_disappear
            hide expression papyrusN
            jump d6r1

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d6k1

        "Sleep":
            scene black with dissolve
            pause 2.0
            u "{cps=20}I can't sleep.{/cps}"
            jump d6r1

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d6s1

    return

label d6k1:
    scene bg kitchen3 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d6k1

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d6r1

    return

label d6s1:
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
            jump d6r1
        "Go to the palm tree":
            $ d6sc = "palm"
            jump d6sp1
        "Go to the square":
            $ d6sc = "square"
            jump d6sp1
        "Go to Eya":
            $ d6sc = "eya"
            jump d6sp1
        "Go to the temple":
            pause 1.0
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg street3 n with pixellate
            play music music_jungle fadein 1.0
            play music3 music_night fadein 1.0
            pause 1.0

            ""
            show userkaf n at left, showFade
            play sound sfx_appear
            $ pau(3)
            show monster at right, showFade
            play sound sfx_appear
            $ pau(1)
            play sound sfx_monster
            show userkaf s at left
            $ pau(2)


            play sound sfx_rewind
            stop music3
            scene black
            $ pau(2)

            u "{cps=15}Ahhhhhhhhh{nw}{/cps}"
            jump d6r2


    return

label d6sp1:
    show userkaf n at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0
    
    if d6sc == "palm":
        scene bg palm3 with pixellate
        play music music_rivernight fadein 1.0
    elif d6sc == "square":
        scene bg square3 with pixellate
        play music music_night fadein 1.0
    elif d6sc == "eya":
        scene bg eya n with pixellate
        play music music_night fadein 1.0


    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    if d6sc == "square":
        u "{cps=20}They haven't started yet.{/cps}"
    else:
        u "{cps=20}Nothing to do here.{/cps}"
    
    menu:
        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d6s1

    return



label d6r2:
    scene bg ubd3 with pixellate
    play music music_night fadein 1.0
    pause 1.0
    show userkaf s at left, showFade
    play sound sfx_appear
    pause 1.0

    if d6rc2 == 0:
        $ d6rc2 = 1

        show userkaf s at left, hideFade with dissolve
        play sound sfx_disappear
        hide userkaf s
        show userkaf s at right, showFade
        play sound sfx_appear
        pause 1.0

        show umom s at left, showFade
        play sound sfx_appear
        pause 1.0

        um "{cps=20}What's the problem Userkaf?{/cps}"
        u "{cps=20}Bad dream again.{/cps}"
        um "{cps=20}I'm sorry.{/cps}"
        um "{cps=20}Userkaf.{/cps}"
        u "{cps=20}Yes mom?{/cps}"
        um "{cps=20}Your dad ..{nw}{/cps}"
        u "{cps=20}Is missing?{/cps}"
        um "{cps=20}Yes.{/cps}"
        u "{cps=20}I knew that.{/cps}"
        u "{cps=20}Why didn't you say?{/cps}"
        um "{cps=20}I didn't want to make you worry.{/cps}"
        um "{cps=20}I thought he would come.{/cps}"
        show userkaf h at right
        u "{cps=20}Don't worry mom.{/cps}"
        u "{cps=20}I'll find him.{/cps}"
        um "{cps=20}Be careful.{/cps}"
        u "{cps=20}Sure.{/cps}"
        show umom s at left, hideFade with dissolve
        play sound sfx_disappear
        hide umom s
        pause 1.0

        show userkaf h at right, hideFade with dissolve
        play sound sfx_disappear
        hide userkaf h
        show userkaf s at left, showFade
        play sound sfx_appear


    menu:
        "Look in the mirror":
            show userkaf s at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            pause 1.0

            scene bg ubd3 at showBlur
            play sound sfx_magic
            
            show mirror6 with dissolve

            u "{cps=20}Where are you dad?{/cps}"


            show mirror6 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror6
            jump d6r2

        "Check Eya's paper":
            show userkaf s at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            pause 1.0

            scene bg ubd3 at showBlur
            play sound sfx_paper
            
            show expression papyrusN with dissolve

            " "


            show expression papyrusN at hideFade with dissolve
            play sound sfx_disappear
            hide expression papyrusN
            jump d6r2

        "Go to the kitchen":
            show userkaf s at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            jump d6k2

        "Sleep":
            scene black with dissolve
            pause 3.0
            jump d6r3

        "Go out":
            show userkaf s at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            jump d6s2




    return

label d6k2:
    scene bg kitchen3 with pixellate

    pause 1.0
    show userkaf s at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d6k2

        "Go back to your room":
            show userkaf s at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            pause 1.0
            jump d6r2

    return

label d6s2:
    scene bg street1 n with pixellate
    play music music_night fadein 1.0

    pause 1.0
    show userkaf s at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Go back home":
            show userkaf s at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            jump d6r2
        "Go to the palm tree":
            $ d6sc = "palm"
            jump d6sp2
        "Go to the square":
            $ d6sc = "square"
            jump d6sp2
        "Go to Eya":
            $ d6sc = "eya"
            jump d6sp2
        # "Go to the temple":
        #     $ d6sc = "temple"
        #     jump d6sp2


    return

label d6sp2:
    show userkaf s at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf s
    pause 1.0
    
    if d6sc == "palm":
        scene bg palm3 with pixellate
        play music music_rivernight fadein 1.0
    elif d6sc == "temple":
        scene bg street3 with pixellate
        play music music_night fadein 1.0
    elif d6sc == "square":
        scene bg square3 with pixellate
        play music music_night fadein 1.0
    elif d6sc == "eya":
        scene bg eya n with pixellate
        play music music_night fadein 1.0


    pause 1.0
    show userkaf s at center, showFade
    play sound sfx_appear
    pause 1.0



    if d6sc != "temple":
        u "{cps=20}Nothing to do here.{/cps}"
    else:
        menu:
            "Enter the temple":
                show userkaf s at left, hideFade with dissolve
                play sound sfx_disappear
                hide userkaf s


                u "{cps=20}Nothing to do here.{/cps}"
                

    menu:
        "Go back":
            show userkaf s at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            pause 1.0
            jump d6s2


    return



label d6r3:
    scene bg ubd1 with pixellate
    if(ds6 == 0):
        $ ds6 = 1
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

            u "{cps=20}I'll find you dad.{/cps}"


            show mirror1 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror1
            jump d6r3

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
            jump d6r3

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d6k3

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d6s3

    return

label d6k3:
    scene bg kitchen1 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d6k3

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d6r3

    return

label d6s3:
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
            jump d6r3
        "Go to the palm tree":
            $ d6sc = "palm"
            jump d6sp3
        "Go to the square":
            jump d6q1
        "Go to Eya":
            $ d6sc = "eya"
            jump d6sp3
        "Go to the temple":
            $ d6sc = "temple"
            jump d6sp3


    return

label d6sp3:
    show userkaf n at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0
    
    if d6sc == "palm":
        scene bg palm1 with pixellate
        play music music_morning fadein 1.0
    elif d6sc == "temple":
        scene bg street3 with pixellate
        play music music_jungle fadein 1.0
    elif d6sc == "eya":
        scene bg eya m with pixellate
        play music music_morning fadein 1.0


    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    if d6sc != "temple":
        u "{cps=20}Nothing to do here.{/cps}"
    
    menu:
        "Enter the temple" if (d6sc == "temple"):
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            scene bg temple1 with pixellate
            play music music_temple fadein 1.0
            pause 1.0
            show userkaf n at center, showFade
            play sound sfx_appear
            pause 1.0
            u "{cps=20}I'll know your secret.{/cps}"
            menu:
                "Go back":
                    show userkaf n at center, hideFade with dissolve
                    play sound sfx_disappear
                    hide userkaf n
                    pause 1.0
                    jump d6sp3



        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d6s3

    return

label d6q1:
    scene bg square with pixellate
    play music music_wind fadein 1.0
    pause 1.0
    show cheif at center, showFade
    play sound sfx_appear
    pause 1.0

    V "{cps=10}Hello kids ...{/cps}"
    V "{cps=10}We're on the third day of the Guradians Of The Nile ...{/cps}"
    V "{cps=10}Now 8 teams are participating ...{/cps}"
    V "{cps=10}We will say goodbye to two of them today.{/cps}"
    V "{cps=10}Today ..{w=0.2} we'll play mehen and wrestling ...{/cps}"
    V "{cps=10}Same rules as yesterday .. Good luck.{/cps}"

    pause 1.0
    show cheif at center, hideFade with dissolve
    play sound sfx_disappear
    hide cheif
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

    u "{cps=20}Hello.{/cps}"
    e "{cps=20}Hello.{nw}{/cps}"
    t "{cps=20}Hello.{nw}{/cps}"
    m "{cps=20}Hello.{/cps}"

    e "{cps=20}Userkaf you will go for Mehen yes?{/cps}"
    u "{cps=20}You know me.{/cps}"
    t "{cps=20}So like yesterday teams yes?{/cps}"
    m "{cps=20}I guess.{nw}{/cps}"
    e "{cps=20}Yeah I'll play Mehen too and you both go for wrestling.{/cps}"
    show eya h at p3
    e "{cps=20}Good luck all.{/cps}"
    show userkaf h at p2
    show tausert h at p4
    show minas n at p1
    m "{cps=20}See you.{nw}{/cps}"
    t "{cps=20}See you.{/cps}"

    pause 1.0

    show tausert h at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert h
    show minas h at p1, hideFade with dissolve
    play sound sfx_disappear
    hide minas h
    pause 1.0

    u "{cps=20}Let's move Eya.{/cps}"

    pause 1.0

    show userkaf h at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf h
    show eya h at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya h

    pause 1.0

    scene bg sq2 with pixellate
    
    pause 1.0

    show userkaf s at left, showFade
    play sound sfx_appear
    show eya h at right, showFade
    play sound sfx_appear

    pause 1.0


    show eya s at right
    e "{cps=20}You seem worried.{/cps}"
    u "{cps=20}I'm good.{/cps}"
    e "{cps=20}You're not.{nw}{/cps}"
    e "{cps=20}Are you worried about the game?{/cps}"
    u "{cps=20}Actually not.{/cps}"
    e "{cps=20}So what's the matter!{/cps}"
    u "{cps=20}My father is missing.{/cps}"
    show eya c at right
    e "{cps=20}Huh how?{/cps}"
    u "{cps=20}I don't know .. We haven't seen him since the opening of the festival.{/cps}"
    e "{cps=20}Have you tried to search for him?{/cps}"
    u "{cps=20}Not yet.{/cps}"
    show eya h at right
    e "{cps=20}We all will help you. {nw}{/cps}"
    e "{cps=20}Don't worry Userkaf{/cps}"
    show userkaf h at left
    u "{cps=20}Thank you Eya.{/cps}"
    u "{cps=20}Let me teach you some tricks before we start.{/cps}"
    e "{cps=20}Okayyy let's go.{/cps}"

    pause 1.0
    scene black with dissolve
    pause 2.0
    "{cps=20}Userakaf teaching Eya tricks ...{/cps}"
    pause 2.0

    "{cps=20}They start playing ...{/cps}"
    pause 2.0

    scene bg sq2 with pixellate
    pause 1.0
    show userkaf h at left, showFade
    play sound sfx_appear
    show eya h at right, showFade
    play sound sfx_appear
    pause 1.0


    u "{cps=20}What did you do Eya?{/cps}"
    e "{cps=20}I wonnn.{/cps}"
    u "{cps=20}Great I won too.{/cps}"
    u "{cps=20}Let's see the others.{/cps}"

    pause 1.0
    scene square with pixellate
    pause 1.0

    show userkaf h at p1, showFade
    play sound sfx_appear
    show eya h at p2, showFade
    play sound sfx_appear

    pause 1.0

    show tausert n at p3, showFade
    play sound sfx_appear
    show minas s at p4, showFade
    play sound sfx_appear

    pause 1.0

    e "{cps=20}What did you do guys?{/cps}"
    show userkaf z at p1
    show eya z at p2
    m "{cps=20}I lost ...{/cps}"
    u "{cps=20}Oh my God Minas you're kidding of course.{/cps}"
    show userkaf n at p1
    show eya n at p2

    e "{cps=20}And you Tau?{/cps}"
    t "{cps=20}I won.{/cps}"
    e "{cps=20}We won too.{/cps}"
    t "{cps=20}Good.{/cps}"
    u "{cps=20}It's okay Minas we're good.{/cps}"
    m "{cps=20}I don't want to talk.{/cps}"
    t "{cps=20}The cheif is going to speak now.{/cps}"

    play sound sfx_amazed
    V "{cps=10}SILENCE.{/cps}"
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
    show minas n at p4, hideFade with dissolve
    play sound sfx_disappear
    hide minas n

    pause 1.0

    show cheif at center, showFade
    play sound sfx_appear
    pause 1.0

    V "{cps=10}You were 8 teams this morning ...{/cps}"
    V "{cps=10}We're eliminating the least 2 teams now ...{/cps}"
    V "{cps=10}6 teams left ...{/cps}"
    V "{cps=10}Good luck tomorrow.{/cps}"

    pause 1.0
    show cheif at center, hideFade with dissolve
    play sound sfx_disappear
    hide cheif
    pause 1.0


    show minas n at p1, showFade
    play sound sfx_appear
    show userkaf n at p2, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    e "{cps=20}We qualified Minas no need to worry.{/cps}"
    show minas h at p1
    m "{cps=20}Sure.{/cps}"
    

    e "{cps=20}Guys.{w=0.2}{nw}{/cps}"
    show tausert c at p4
    show minas c at p1
    e "{cps=20}I have something to tell you.{/cps}"
    show userkaf s at p2
    show tausert z at p4
    show minas z at p1
    e "{cps=20}Userkaf's father is missing.{/cps}"
    t "{cps=20}Oh my God. {nw}{/cps}"
    e "{cps=20}And we're gonna find him.{/cps}"
    show tausert c at p4
    t "{cps=20}What if he is kidnapped by the monster?{/cps}"
    show userkaf h at p2
    show minas h at p1
    m "{cps=20}If this is real, I'm ready to get kidnapped too.{/cps}"
    show eya h at p3
    e "{cps=20}Same for me.{/cps}"
    show tausert h at p4
    t "{cps=20}I guess I can't say no.{/cps}"
    u "{cps=20}I love you guys.{/cps}"
    pause 2.0

    show eya n at p3
    show userkaf n at p2
    show tausert n at p4
    show minas n at p1

    t "{cps=20}So what leader?{/cps}"
    e "{cps=20}Should we split up?{/cps}"
    t "{cps=20}No are you kidding!{w=0.1}{nw}{/cps}"
    t "{cps=20}We'll find him together.{/cps}"
    e "{cps=20}Mhm okay.{/cps}"
    m "{cps=20}Let's go then.{/cps}"
    u "{cps=20}Where will we go first?{/cps}"
    e "{cps=20}Let's start with Intaf's area.{/cps}"
    u "{cps=20}Whatever.{/cps}"

    pause 1.0
    show minas n at p1, hideFade with dissolve
    play sound sfx_disappear
    hide minas n
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

    jump d6i1

    return

label d6i1:
    pause 1.0
    scene bg intaf m with pixellate
    play music music_morning fadein 1.0
    pause 1.0

    show minas n at p1, showFade
    play sound sfx_appear
    show userkaf n at p2, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    i "{cps=20}Hello again boys and girls.{/cps}"
    e "{cps=20}Hii Intaf. {nw}{/cps}"
    m "{cps=20}Hey bro.{nw}{/cps}"
    t "{cps=20}Hello.{w=0.2}{nw}{/cps}"
    u "{cps=20}Hello.{/cps}"

    i "{cps=20}How are you doing in the contest?{/cps}"
    e "{cps=20}We're still in.{/cps}"
    t "{cps=20}They are using a different system from you had told us.{/cps}"
    i "{cps=20}Oh really.{/cps}"
    m "{cps=20}Yes but we came for another reason.{/cps}"
    e "{cps=20}Userkaf's father is missing.{/cps}"
    i "{cps=20}Oh my God.{/cps}"
    i "{cps=20}How does he look like?{/cps}"
    e "{cps=20}He is an Userkaf with a black beard.{/cps}"
    show userkaf z at p2
    i "{cps=20}Oh I remembered him.{/cps}"
    u "{cps=20}YOU SAW HIM?{/cps}"
    show userkaf n at p2
    i "{cps=20}No, I remembered him from the last year festival.{/cps}"
    i "{cps=20}But sorry I haven't seen him lately.{/cps}"
    t "{cps=20}Where can we search?{/cps}"
    u "{cps=20}or who can we ask?{/cps}"
    i "{cps=20}You can ask the village Cheif.{/cps}"
    i "{cps=20}And if I knew something I will tell you.{/cps}"
    scene bg intaf e
    play music music_wind fadein 1.0

    show minas n at p1
    show userkaf h at p2
    show eya h at p3
    show tausert h at p4
    i "{cps=20}Thank you Intaf.{/cps}"
    i "{cps=20}Good luck in the contest guys.{/cps}"


    pause 1.0
    show minas n at p1, hideFade with dissolve
    play sound sfx_disappear
    hide minas n
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

    jump d6ss1

    return

label d6ss1:
    scene bg street1 e with pixellate
    play music music_wind fadein 1.0

    pause 1.0

    show minas n at p1, showFade
    play sound sfx_appear
    show userkaf n at p2, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    e "{cps=20}We will continue searching tommorow.{/cps}"
    t "{cps=20}Yes we have to go home now.{/cps}"
    e "{cps=20}See you later guys.{/cps}"

    e "{cps=20}See you later guys.{/cps}"

    pause 1.0

    show tausert n at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert n
    show eya n at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya n
    pause 1.0


    m "{cps=20}Sorry for that Userkaf.{/cps}"
    show userkaf h at p2
    u "{cps=20}No worries.{/cps}"
    pause 1.0

    show minas n at p1, hideFade with dissolve
    play sound sfx_disappear
    hide minas n
    pause 1.0

    show userkaf n at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n

    show userkaf n at left
    pause 1.0

    menu:
        "Go back home":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d6r4
        "Go to the palm tree":
            $ d6sc = "palm"
            jump d6sp4
        "Go to the square":
            $ d6sc = "square"
            jump d6sp4
        "Go to Eya":
            $ d6sc = "eya"
            jump d6sp4
        "Go to the temple":
            $ d6sc = "temple"
            jump d6sp4





    return



label d6r4:

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

            u "{cps=20}I want to have a nap.{/cps}"


            show mirror2 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror2
            jump d6r4

        "Check Eya's paper":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg ubd2 at showBlur
            play sound sfx_paper
            
            show expression papyrusN with dissolve

            " "


            show expression papyrusN at hideFade with dissolve
            play sound sfx_disappear
            hide expression papyrusN
            jump d6r4

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d6k4

        "Sleep":

            scene black with dissolve
            pause 2.0
            play sound sfx_sleep
            jump d6r5
            

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d6s4

        

    return

label d6k4:
    scene bg kitchen2 with pixellate
    

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d6k4

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d6r4

    return

label d6s4:
    scene bg street1 e with pixellate
    play music music_wind fadein 1.0

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Go back home":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d6r4
        "Go to the palm tree":
            $ d6sc = "palm"
            jump d6sp4
        "Go to the square":
            $ d6sc = "square"
            jump d6sp4
        "Go to Eya":
            $ d6sc = "eya"
            jump d6sp4
        "Go to the temple":
            $ d6sc = "temple"
            jump d6sp4


    return

label d6sp4:
    show userkaf n at left, hideFade with dissolve
    hide userkaf n
    pause 1.0
    
    if d6sc == "palm":
        scene bg palm2 with pixellate
        play music music_wind fadein 1.0
    elif d6sc == "temple":
        scene bg street3 e with pixellate
        play music music_jungle fadein 1.0
    elif d6sc == "eya":
        scene bg eya e with pixellate
        play music music_wind fadein 1.0
    elif d6sc == "square":
        scene bg square2 with pixellate
        play music music_wind fadein 1.0


    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    if d6sc != "temple":
        u "{cps=20}Nothing to do here.{/cps}"
    
    menu:
        "Enter the temple" if (d6sc == "temple"):
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            scene bg temple1 with pixellate
            play music music_temple fadein 1.0
            pause 1.0
            show userkaf n at center, showFade
            play sound sfx_appear

            pause 1.0
            u "{cps=20}I'll know your secret.{/cps}"
            menu:
                "Go back":
                    show userkaf n at center, hideFade with dissolve
                    play sound sfx_disappear
                    hide userkaf n
                    pause 1.0
                    jump d6sp4



        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d6s4

    return




label d6r5:

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

            if(d6s5chat == 0):
                u "{cps=20}I want to talk.{/cps}"
            else:
                u "{cps=20}I need to sleep.{/cps}"



            show mirror3 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror3
            jump d6r5

        "Check Eya's paper":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg ubd3 at showBlur
            play sound sfx_paper
            
            show expression papyrusN with dissolve

            " "


            show expression papyrusN at hideFade with dissolve
            play sound sfx_disappear
            hide expression papyrusN
            jump d6r5

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d6k5

        "Sleep":

            scene black with dissolve
            pause 2.0
            if(d6s5chat == 0):
                u "{cps=20}I can't sleep.{/cps}"
                jump d6r5
            else:
                play sound sfx_sleep
                jump day7




        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d6s5

        

    return

label d6k5:
    scene bg kitchen3 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d6k5

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d6r5

    return

label d6s5:
    scene bg street1 n with pixellate
    play music music_night fadein 1.0

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    if(d6s5chat == 0):
        $ d6s5chat = 1
        show stranger at right, showFade
        play sound sfx_appear

        pause 1.0
        
        
        ss "{cps=20}Hello kid.{/cps}"
        show userkaf h at left
        u "{cps=20}Hi.{/cps}"
        ss "{cps=20}What are doing in the street that late?{/cps}"
        u "{cps=20}I couldn't sleep so I'm taking a walk.{/cps}"
        show userkaf s at left
        ss "{cps=20}You don't look okay.{/cps}"
        u "{cps=20}I haven't found my dad yet.{/cps}"
        ss "{cps=20}You have to live.{/cps}"
        show userkaf c at left
        u "{cps=20}What do you mean?{/cps}"
        ss "{cps=20}Nothing .. {w=0.1} I mean .. {w=0.2} What if he died?{/cps}"
        show userkaf a at left
        u "{cps=20}Don't say that!{/cps}"
        u "{cps=20}I will find him.{/cps}"
        ss "{cps=20}I heard that someone has been killed by the monster this week.{/cps}"
        u "{cps=20}Then I will find his body.{/cps}"
        u "{cps=20}I have to go bye.{/cps}"
        ss "{cps=20}Bye kid.{/cps}"
        pause 1.0


        hide stranger at right, hideFade with dissolve
        play sound sfx_disappear
        hide stranger
        pause 1.0
        show userkaf n at left
        pause 1.0



    menu:
        "Go back home":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d6r5
        "Go to the palm tree":
            $ d6sc = "palm"
            jump d6sp5
        "Go to the square":
            $ d6sc = "square"
            jump d6sp5
        "Go to Eya":
            $ d6sc = "eya"
            jump d6sp5
        #"Go to the temple":
        #    $ d6sc = "temple"
        #    jump d6sp5


    return

label d6sp5:
    show userkaf n at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0
    
    if d6sc == "palm":
        scene bg palm3 with pixellate
        play music music_rivernight fadein 1.0
    elif d6sc == "temple":
        scene bg street3 with pixellate
        play music music_jungle fadein 1.0
    elif d6sc == "eya":
        scene bg eya n with pixellate
        play music music_night fadein 1.0
    elif d6sc == "square":
        scene bg square3 with pixellate
        play music music_night fadein 1.0


    pause 1.0
    show userkaf n at center, showFade
    pause 1.0

    if d6sc != "temple":
        u "{cps=20}Nothing to do here.{/cps}"
    
    menu:
        "Enter the temple" if (d6sc == "temple"):
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            scene bg temple1 with pixellate
            play music music_temple fadein 1.0
            pause 1.0
            show userkaf n at center, showFade
            play sound sfx_appear
            
            pause 1.0
            u "{cps=20}I'll know your secret.{/cps}"
            menu:
                "Go back":
                    show userkaf n at center, hideFade with dissolve
                    play sound sfx_disappear
                    hide userkaf n
                    pause 1.0
                    jump d6sp5



        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d6s5

    return




