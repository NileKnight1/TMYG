default d7sc = ""
default ds7 = 0

label day7:
    
    $ renpy.music.set_volume(1, delay=0, channel='music')
    $ renpy.music.set_volume(0.4, delay=0, channel='music2')
    jump d7r1

    return

label d7r1:

    scene bg ubd1 with pixellate
    if(ds7 == 0):
        $ ds7 = 1
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

            u "{cps=20}The contest will start soon.{/cps}"


            show mirror1 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror1
            jump d7r1

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
            jump d7r1

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d7k1

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d7s1

    return

label d7k1:
    scene bg kitchen1 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d7k1

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d7r1

    return

label d7s1:
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
            jump d7r1
        "Go to the palm tree":
            $ d7sc = "palm"
            jump d7sp1
        "Go to the square":
            jump d7q1
        "Go to Eya":
            $ d7sc = "eya"
            jump d7sp1
        "Go to the temple":
            $ d7sc = "temple"
            jump d7sp1


    return

label d7sp1:
    show userkaf n at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0
    
    if d7sc == "palm":
        scene bg palm1 with pixellate
        play music music_rivermorning fadein 1.0
    elif d7sc == "temple":
        scene bg street3 with pixellate
        play music music_jungle fadein 1.0

    elif d7sc == "eya":
        scene bg eya m with pixellate
        play music music_morning fadein 1.0


    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    if d7sc != "temple":
        u "{cps=20}Nothing to do here.{/cps}"
    
    menu:
        "Enter the temple" if (d7sc == "temple"):
            show userkaf n at center, hideFade with dissolve
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
                    jump d7sp1



        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d7s1

    return

label d7q1:
    scene bg square with pixellate
    play music music_wind fadein 1.0
    pause 1.0
    show cheif at center, showFade
    play sound sfx_appear
    pause 1.0

    V "{cps=10}Hi kids ...{/cps}"
    V "{cps=10}Today is the day before last ...{/cps}"

    V "{cps=10}6 teams left ...{/cps}"
    V "{cps=10}2 of them will go ...{/cps}"
    V "{cps=10}We are playing 'Hounds and Jackals' and 'Stick Fighting' ...{/cps}"
    V "{cps=10}Same rules as always .. See you.{/cps}"

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

    u "{cps=20}Hi.{/cps}"
    e "{cps=20}Hi.{nw}{/cps}"
    t "{cps=20}Hi.{nw}{/cps}"
    m "{cps=20}Hi.{/cps}"

    e "{cps=20}Same teams?{/cps}"
    t "{cps=20}No problems.{/cps}"
    m "{cps=20}Mhm.{/cps}"
    u "{cps=20}Great.{/cps}"
    
    show minas h at p1
    show tausert h at p4

    t "{cps=20}Later guys.{/cps}"
    show userkaf h at p2
    show eya h at p3

    e "{cps=20}Later.{/cps}"

    pause 1.0
    show tausert h at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert h
    show minas h at p1, hideFade with dissolve
    play sound sfx_disappear
    hide minas h
    pause 1.0

    e "{cps=20}Let's go.{/cps}"


    pause 1.0

    show userkaf h at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf h
    show eya h at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya h


    scene bg sq2 with pixellate
    pause 1.0

    show userkaf s at left, showFade
    play sound sfx_appear
    show eya h at right, showFade
    play sound sfx_appear


    pause 1.0
    e "{cps=20}Userkaf ...{/cps}"
    u "{cps=20}Yes Eya?{/cps}"
    show eya h at right
    e "{cps=20}We'll find him.{/cps}"
    show userkaf h at left
    u "{cps=20}I believe.{/cps}"
    e "{cps=20}We'll search after the contest.{/cps}"
    u "{cps=20}Let's play now.{/cps}"

    pause 1.0

    scene black with pixellate
    pause 1.0

    "{cps=20}They start playing ...{/cps}"

    pause 2.0

    scene bg sq2 with pixellate
    pause 1.0
    show userkaf s at left, showFade
    play sound sfx_appear
    show eya s at right, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Don't kid with me.{/cps}"
    u "{cps=20}You lost too?{/cps}"
    e "{cps=20}Oh my God you too.{/cps}"
    e "{cps=20}Let's see others.{/cps}"

    pause 1.0
    scene square with pixellate
    pause 1.0

    show userkaf s at p1, showFade
    play sound sfx_appear
    show eya s at p2, showFade
    play sound sfx_appear

    pause 1.0
    show tausert h at p3, showFade
    play sound sfx_appear
    pause 1.0

    show tausert c at p3

    t "{cps=20}What's the matter{/cps}"
    e "{cps=20}We both lost.{/cps}"
    u "{cps=20}Where's Minas?{/cps}"
    t "{cps=20}He told me I lost then he left.{/cps}"
    e "{cps=20}What did you do Tau?{/cps}"
    t "{cps=20}I won.{/cps}"

    play sound sfx_amazed
    V "{cps=10}SILENCE.{/cps}"
    pause 1.0

    show userkaf s at p1, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf s
    show eya s at p2, hideFade with dissolve
    play sound sfx_disappear
    hide eya s
    show tausert s at p3, hideFade with dissolve
    play sound sfx_disappear
    hide tausert s

    pause 1.0

    show cheif at center, showFade
    play sound sfx_appear
    pause 1.0

    V "{cps=10}6 teams played this morning ...{/cps}"
    V "{cps=10}And 2 of them will leave us ...{/cps}"
    V "{cps=10}The other 4 will compete on the last day ...{/cps}"
    V "{cps=10}See you tomorrow.{/cps}"

    pause 1.0
    show cheif at center, hideFade with dissolve
    play sound sfx_disappear
    hide cheif
    pause 1.0

    show userkaf n at p2, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    show userkaf c at p2
    u "{cps=20}We didn't disqualify?{/cps}"
    show eya z at p3
    show tausert c at p4
    e "{cps=20}Huh how!{/cps}"
    t "{cps=20}This is weird.{/cps}"
    u "{cps=20}Mhm.{/cps}"
    show userkaf n at p2 
    show eya n at p3
    show tausert n at p4
    pause 1.0

    e "{cps=20}Userkaf .. {nw}{/cps}"
    e "{cps=20}Let's talk with the cheif before he leaves.{/cps}"
    u "{cps=20}Oh yeah you reminded me.{/cps}"
    u "{cps=20}Cheif!{/cps}"
    pause 1.0
    show cheif at p1
    pause 1.0

    V "{cps=10}Hello kids.{/cps}"
    t "{cps=20}Hello Cheif.{nw}{/cps}"
    u "{cps=20}Hello Cheif.{nw}{/cps}"
    e "{cps=20}Hello Cheif.{/cps}"
    u "{cps=20}We wanted to ask you if you ever seen a monster.{/cps}"
    V "{cps=10}A monster? Haha.{/cps}"
    e "{cps=20}So these are rumors?{/cps}"
    V "{cps=10}Of course kids ...{/cps}"
    V "{cps=10}There are no monsters in Aswan.{/cps}"
    t "{cps=20}So are there monsters not in Aswan?{/cps}"
    V "{cps=10}Haha who knows.{/cps}"
    pause 1.0
    show userkaf c at p2
    show eya c at p3
    show tausert c at p4
    pause 1.0

    "A Guard" "{cps=20}Cheif ...{/cps}"
    V "{cps=10}Yes?{/cps}"
    "A Guard" "{cps=20}Someone made a change to today results.{/cps}"
    show userkaf z at p2
    show eya z at p3
    show tausert z at p4
    V "{cps=10}And you left him?{/cps}"
    "A Guard" "{cps=20}We tried to catch him but he ran away.{/cps}"
    V "{cps=10}So there's cheat in the contest.{/cps}"
    V "{cps=10}I will see.{/cps}"
    show userkaf n at p2
    show eya n at p3
    show tausert n at p4
    V "{cps=10}I have to go kids.{/cps}"
    u "{cps=20}One last thing please Cheif.{nw}{/cps}"
    u "{cps=20}Have you seen my father lately?{/cps}"
    V "{cps=10}Your father?{/cps}"
    V "{cps=10}I can't remembe{nw}{/cps}"

    V "{cps=10}I remember that he was responsible for the draw on the opening day{/cps}"
    u "{cps=20}Mhm thank you Cheif.{/cps}"
    V "{cps=10}I will ask about him don't worry Userkaf.{/cps}"
    V "{cps=10}Now I got to deal with that cheater.{/cps}"
    V "{cps=10}See you tomorrow.{/cps}"

    pause 1.0
    show cheif at p1, hideFade with dissolve
    play sound sfx_disappear
    hide cheif
    pause 1.0

    u "{cps=20}Now it makes sense why we didn't disqualify.{/cps}"
    t "{cps=20}Oh my God Minas did that.{/cps}"
    t "{cps=20}But why!{/cps}"
    e "{cps=20}We are getting more problems by time.{/cps}"
    u "{cps=20}I'm going to search for my father.{/cps}"
    show userkaf h at p2
    show eya h at p3
    show tausert h at p4
    e "{cps=20}We're with you don't worry.{/cps}"
    t "{cps=20}Let's go.{/cps}"

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

    jump d7ss1


    return


label d7ss1:
    scene bg street1 m with pixellate
    play music music_morning fadein 1.0
    pause 1.0

    show userkaf n at p2, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear

    pause 1.0
    e "{cps=20}Let's go to the palm area first.{/cps}"

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

    jump d7ss2

    return

label d7ss2:
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

    t "{cps=20}Since the Cheif said there's no monsters we can split up.{/cps}"
    u "{cps=20}Haha yes.{/cps}"
    e "{cps=20}Search the area guys.{/cps}"

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
    pause 3.0

    show userkaf n at p2, showFade
    play sound sfx_appear
    pause 2.0

    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0
    show userkaf c at p2
    u "{cps=20}Anything?{/cps}"
    show userkaf n at p2 
    show tausert c at p4
    t "{cps=20}No, you?{/cps}"
    show tausert n at p4
    u "{cps=20}Nothing.{/cps}"
    pause 1.0

    show eya n at p3, showFade
    play sound sfx_appear
    pause 1.0
    show userkaf c at p2
    show tausert c at p4
    u "{cps=20}Found something?{/cps}"
    show userkaf n at p2
    show tausert n at p4
    show eya c at p3
    e "{cps=20}No, you?{/cps}"
    show eya n at p3
    t "{cps=20}Same.{/cps}"
    e "{cps=20}Let's move then.{/cps}"

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

    jump d7ss3

    return

label d7ss3:
    scene bg eya m with pixellate
    play music music_morning fadein 1.0
    pause 1.0
    show userkaf n at p2, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    e "{cps=20}Ask the neighbours and look in alleys.{/cps}"
    t "{cps=20}Okay leader.{/cps}"
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
    pause 3.0

    show eya n at p3, showFade
    play sound sfx_appear
    pause 2.0

    show userkaf n at p2, showFade
    play sound sfx_appear
    pause 1.0

    e "{cps=20}Goodness me.{/cps}"
    u "{cps=20}Nothing.{/cps}"
    pause 1.0

    show eya c at p3
    e "{cps=20}Why do you thing Minas did that?{/cps}"
    u "{cps=20}I'm his friend and I'm shocked like you.{/cps}"
    show eya n at p3
    e "{cps=20}It seems he wanted that title.{/cps}"
    u "{cps=20}I don't think he did all that for just the title.{/cps}"
    u "{cps=20}I think there's something bigger.{/cps}"
    e "{cps=20}Days will reveal.{/cps}"
    pause 1.0

    e "{cps=20}Tau is late, I'm worried about her.{/cps}"
    u "{cps=20}No please we got enough.{/cps}"

    show userkaf c at p2
    show eya c at p3
    t "{cps=20}Guys guys ...{nw}{/cps}"
    show tausert s at p4, showFade
    play sound sfx_appear
    t "{cps=20}Guys!{/cps}"
    t "{cps=20}You won't believe what I've just heard.{/cps}"
    t "{cps=20}I went to a neighbour and asked her if she has seen your father.{/cps}"
    show userkaf z at p2
    show eya z at p3
    t "{cps=20}She told me her little son saw someone dragging someone but she didn't belive him.{/cps}"
    e "{cps=20}We have to go to her now.{/cps}"

    pause 1.0
    show userkaf z at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf z
    show eya z at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya z
    show tausert s at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert s
    pause 1.0

    scene bg eyan with pixellate
    play music music_morning fadein 1.0
    pause 1.0

    show kidmom n at p1, showFade
    play sound sfx_appear
    pause 1.0

    show userkaf n at p2, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0



    t "{cps=20}Hello again Miss.{/cps}"
    "The Mom" "{cps=20}Hi little girl.{/cps}"

    t "{cps=20}I brought my friends .. we need to know more details.{/cps}"
    "The Mom" "{cps=20}I will tell you everything I know.{/cps}"
    "The Mom" "{cps=20}6 days ago, my son was playing with friends ...{/cps}"
    "The Mom" "{cps=20}When he returned he told me they saw somebody dragging someone ...{/cps}"
    "The Mom" "{cps=20}But I thought he was kidding and didn't give a care...{/cps}"
    e "{cps=20}Can we speak with him?{/cps}"
    show kidmom h at p1
    "The Mom" "{cps=20}Okay I'll call him.{/cps}"

    pause 1.0
    show kidmom h at p1, hideFade with dissolve
    play sound sfx_disappear
    hide kidmom h
    pause 1.0

    show kid h at p1, showFade
    play sound sfx_appear
    pause 1.0

    "The Son" "{cps=20}Hi guys.{/cps}"
    u "{cps=20}Hey.{/cps}"
    u "{cps=20}Can you tell us everything you saw?{/cps}"
    "The Son" "{cps=20}Oh you believe me?{/cps}"
    show eya h at p3
    e "{cps=20}Yes! Speak don't worry.{/cps}"
    show eya n at p3
    # [Edit] remember scene
    show kid n at p1
    "The Son" "{cps=20}Okayy .. sooo .. we were playing and I saw a masked guy ...{/cps}"
    "The Son" "{cps=20}He was carrying a body .. then he saw me ...{/cps}"
    show userkaf z at p2
    show eya z at p3
    show tausert z at p4
    "The Son" "{cps=20}He tried to approach me carrying a stick ...{/cps}"
    "The Son" "{cps=20}He saw my friends .. we were too many .. so he could do nothing to us{/cps}"
    "The Son" "{cps=20}He held the body and ran with it into the trees.{/cps}"
    show userkaf n at p2
    show eya n at p3
    show tausert n at p4
    e "{cps=20}Can you show us where you were playing?{/cps}"
    "The Son" "{cps=20}Yes of course.{/cps}"
    u "{cps=20}Great thank you.{/cps}"

    pause 1.0
    show kid n at p1, hideFade with dissolve
    play sound sfx_disappear
    hide kid n
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

    scene bg street2 e with pixellate
    play music music_wind fadein 1.0

    pause 1.0
    show kid n at p1, showFade
    play sound sfx_appear
    show userkaf n at p2, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0


    "The Son" "{cps=20}We were playing exactly here ...{/cps}"
    "The Son" "{cps=20}And he ran directly there.{/cps}"
    show eya h at p3
    e "{cps=20}Thank you very much.{/cps}"
    show userkaf h at p2
    show tausert h at p4
    u "{cps=20}We really appreciate that.{/cps}"
    "The Son" "{cps=20}You're welcome .. now I have to go before night comes.{/cps}"
    "The Son" "{cps=20}Bye bye.{/cps}"

    pause 1.0
    show kid n at p1, hideFade with dissolve
    play sound sfx_disappear
    hide kid n
    pause 1.0

    show userkaf n at p2
    show eya n at p3
    show tausert n at p4
    pause 1.0

    u "{cps=20}Do you think what I think?{/cps}"
    e "{cps=20}He ran into the temple?{/cps}"
    t "{cps=20}But we went there and didn't find anything.{/cps}"
    u "{cps=20}Maybe there's a secret room or something.{/cps}"
    t "{cps=20}What if the kidnapper saw us?{/cps}"
    e "{cps=20}So that will be his end.{/cps}"
    u "{cps=20}Let's go to the temple.{/cps}"

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

    scene bg street3 e with pixellate
    play music music_jungle fadein 1.0
    
    pause 1.0
    show userkaf n at p2, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Let's enter.{/cps}"
    t "{cps=20}Are you sure?{/cps}"
    e "{cps=20}Don't worry Tausert.{/cps}"

    show monster at p1, showFade
    play sound sfx_appear
    pause 1.0
    play sound sfx_monster
    pause 1.0

    show userkaf z at p2
    show eya z at p3
    show tausert z at p4

    t "{cps=20}Ahhhhh.{nw}{/cps}"
    e "{cps=20}Ahhhhh.{nw}{/cps}"
    u "{cps=20}Ahhhhh.{nw}{/cps}"

    show userkaf z at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf z
    show eya z at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya z
    show tausert z at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert z

    pause 1.0
    scene bg street1 e with pixellate
    play music music_wind fadein 1.0
    pause 1.0
    show userkaf s at p2, showFade
    play sound sfx_appear
    show eya s at p3, showFade
    play sound sfx_appear
    show tausert s at p4, showFade
    play sound sfx_appear
    pause 1.0


    e "{cps=20}I can't believe it's real.{/cps}"
    t "{cps=20}I told you.{/cps}"
    u "{cps=20}The monster is always in the temple area.{/cps}"
    e "{cps=20}So it's protecting the temple.{/cps}"
    e "{cps=20}We'll continue tomorrow.{/cps}"
    t "{cps=20}I'll never go there again.{/cps}"
    e "{cps=20}We're going home now.{/cps}"
    e "{cps=20}See you Userkaf.{/cps}"
    u "{cps=20}See you girls.{/cps}"

    pause 1.0
    show eya s at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya s
    show tausert s at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert s
    pause 1.0

    show userkaf s at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf s
    scene bg street1 n with pixellate
    play music music_night fadein 1.0

    show userkaf n at left, showFade
    play sound sfx_appear

    pause 1.0

    menu:
        "Go back home":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d7r2
        "Go to the palm tree":
            $ d7sc = "palm"
            jump d7sp2
        "Go to the square":
            $ d7sc = "square"
            jump d7sp2
        "Go to Eya":
            $ d7sc = "eya"
            jump d7sp2
        #"Go to the temple":
        #    $ d7sc = "temple"
        #    jump d7sp2


    return



label d7r2:
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

            u "{cps=20}It was a tiring day.{/cps}"


            show mirror3 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror3
            jump d7r2

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
            jump d7r2

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d7k2

        "Sleep":
            scene black with dissolve
            pause 2.0
            play sound sfx_sleep
            jump day8

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d7s2

    return

label d7k2:
    scene bg kitchen3 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d7k2

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d7r2

    return

label d7s2:
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
            jump d7r2
        "Go to the palm tree":
            $ d7sc = "palm"
            jump d7sp2
        "Go to the square":
            $ d7sc = "square"
            jump d7sp2
        "Go to Eya":
            $ d7sc = "eya"
            jump d7sp2



    return

label d7sp2:
    show userkaf n at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0
    
    if d7sc == "palm":
        scene bg palm3 with pixellate
        play music music_rivernight fadein 1.0
    elif d7sc == "temple":
        scene bg street3 with pixellate
        play music music_jungle fadein 1.0
    elif d7sc == "eya":
        scene bg eya n with pixellate
        play music music_night fadein 1.0
    elif d7sc == "square":
        scene bg square3 with pixellate
        play music music_night fadein 1.0


    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    if d7sc != "temple":
        u "{cps=20}Nothing to do here.{/cps}"
    
    menu:
        "Enter the temple" if (d7sc == "temple"):
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
                    jump d7sp1



        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d7s2

    return
