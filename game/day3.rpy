default leader = 1
default papy = 3
default housee= 0
default mincome= 0
default papyrusN = "papyrus %d" % 3 
default ds3 = 0

label day3:
    $ renpy.music.set_volume(1, delay=0, channel='music')
    $ renpy.music.set_volume(0.4, delay=0, channel='music2')
    scene black with dissolve
    pause 5.0

    jump d3r1

    return

label d3r1:
    scene bg ubd1 with pixellate
    if(ds3 == 0):
        $ ds3 = 1
        play sound sfx_rooster
        $ pau(2.0)
    play music music_morning
    pause 1.0

    show userkaf n at left, showFade
    play sound sfx_appear

    pause 1.0

    u "{cps=20}Uhh.{/cps}"


    menu:
        "Look in the mirror":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear

            hide userkaf n
            pause 1.0

            scene bg ubd1 at showBlur
            play sound sfx_magic
            
            show mirror1 with dissolve

            u "{cps=20}I want her.{/cps}"


            show mirror1 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror1
            jump d3r1


        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d3k1

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d3s00

    return


label d3k1:
    scene bg kitchen1
    with pixellate
    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear

    pause 1.0
    
    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d3k1

    
        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d3r1

    return    

label d3s00:
    scene bg street1 m with pixellate
    play music music_morning
    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear

    menu:
        "Go back home":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d3r1

        "Go to the palm tree":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d3p1

        "Go to the square":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d3q1


    return


label d3q1:
    scene bg square with pixellate
    play music music_wind
    pause 1.0
    show userkaf c at center, showFade
    play sound sfx_appear


    u "{cps=20}No one is here.{/cps}"
    menu:
        "Go back":
            show userkaf c at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf c
            pause 1.0
            jump d3s00
        
    return


label d3p1:
    scene bg palm1 with pixellate
    play music music_rivermorning
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


    u "{cps=20}Hello everyone.{/cps}"
    u "{cps=20}I've decided something ...{/cps}"

    menu:
        "Give Minas the lead":
            show minas c at p1
            u "{cps=20}Minas.{/cps}"
            m "{cps=20}Yes Userkaf?{/cps}"
            show userkaf h at p2
            show minas b at p1
            u "{cps=20}You are the leader.{/cps}"
            m "{cps=20}Oh bro why!{/cps}"
            u "{cps=20}You deserve it.{/cps}"
            m "{cps=20}Thanks bro.{/cps}"
            $ leader = 0


        "Give Eya the lead":
            show eya c at p3
            u "{cps=20}Eya.{/cps}"
            e "{cps=20}Yes Userkaf?{/cps}"
            show userkaf h at p2
            show eya b at p3
            u "{cps=20}You are the leader.{/cps}"
            m "{cps=20}Wow.{/cps}"
            e "{cps=20}Oh my God.{/cps}"
            e "{cps=20}You really mean it?{/cps}"
            u "{cps=20}Yes.{/cps}"
            e "{cps=20}Thank youuu.{/cps}"
            $ leader = 1
        
        
        "Give Tausert the lead":
            show tausert c at p4
            u "{cps=20}Tausert.{/cps}"
            t "{cps=20}Yes Userkaf?{/cps}"
            show userkaf h at p2
            show tausert h at p4
            u "{cps=20}You are the leader.{/cps}"
            t "{cps=20}Thank you ...{/cps}"
            t "{cps=20}But you know that I don't care being the leader ...{/cps}"
            t "{cps=20}So give it to one of them.{/cps}"
            u "{cps=20}Mhm okay.{/cps}"
            show tausert n at p4
            show userkaf n at p2
            menu:
                "Give Minas the lead":
                    show minas c at p1
                    u "{cps=20}Minas.{/cps}"
                    m "{cps=20}Yes Userkaf?{/cps}"
                    show userkaf h at p2
                    show minas b at p1
                    u "{cps=20}You are the leader.{/cps}"
                    m "{cps=20}Oh bro why!{/cps}"
                    u "{cps=20}You deserve it.{/cps}"
                    m "{cps=20}Thanks bro.{/cps}"
                    $ leader = 0


                "Give Eya the lead":
                    show eya c at p3
                    u "{cps=20}Eya.{/cps}"
                    e "{cps=20}Yes Userkaf?{/cps}"
                    show userkaf h at p2
                    show eya b at p3
                    u "{cps=20}You are the leader.{/cps}"
                    m "{cps=20}Wow.{/cps}"
                    e "{cps=20}Oh my God.{/cps}"
                    e "{cps=20}You really mean it?{/cps}"
                    u "{cps=20}Yes.{/cps}"
                    e "{cps=20}Thank youuu.{/cps}"
                    $ leader = 1
                


    u "{cps=20}We all know that the leader won't play the first 6 games.{/cps}"
    u "{cps=20}But we all will train.{/cps}"
    t "{cps=20}I agree.{/cps}"
    pause 1.0

    
    u "{cps=20}So who knows what?{/cps}"
    t "{cps=20}I never played senet nor mehen.{/cps}"
    u "{cps=20}And jackals?{/cps}"
    t "{cps=20}Mhm nah.{/cps}"
    u "{cps=20}I always played them with Minas.{/cps}"
    m "{cps=20}MEMORIES.{/cps}"
    u "{cps=20}And you Eya?{/cps}"
    m "{cps=20}I only played it once and I don't remember it.{/cps}"
    u "{cps=20}Well.{/cps}"
    t "{cps=20}Who can play archery?{/cps}"
    m "{cps=20}I do.{/cps}"
    m "{cps=20}What about wrestling hehehe.{/cps}"
    u "{cps=20}You know me.{/cps}"
    e "{cps=20}Let's practice then.{/cps}"
    scene black with dissolve

    "PRACTICING ..."

    scene bg palm2 with pixellate
    play music music_riverevening fadein 1.0
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

    u "{cps=20}Now we choose who plays what.{/cps}"
    e "{cps=20}What do you want to play Userkaf?{/cps}"
    menu:
        "Senet and sticks":
            u "{cps=20}Me senet and sticks.{/cps}"
            t "{cps=20}I will go for archery and mehen.{/cps}"
            e "{cps=20}And Minas wrestling and jackals.{/cps}"
            m "{cps=20}Well.{/cps}"
        "Mehen and archery":
            e "{cps=20}I will go for mehen and archery.{/cps}"
            t "{cps=20}Me senet and sticks.{/cps}"
            e "{cps=20}And Minas wrestling and jackals.{/cps}"
            m "{cps=20}Well.{/cps}"
        "Jackals and wrestling":
            u "{cps=20}Me jackals and wrestling.{/cps}"
            t "{cps=20}I'll go for senet and sticks.{/cps}"
            e "{cps=20}And Minas archery and mehen.{/cps}"
            m "{cps=20}Well.{/cps}"

    e "{cps=20}GUYS I'M SO NERVOUS.{/cps}"
    u "{cps=20}Same for real.{/cps}"
    t "{cps=20}No please ...{/cps}"
    t "{cps=20}We should be at full focus ...{/cps}"
    t "{cps=20}We don't want any anxiety.{/cps}"
    e "{cps=20}I don't wanna lose.{/cps}"
    m "{cps=20}We won't I trust.{/cps}"
    u "{cps=20}I hope so.{/cps}"

    pause 2.0

    e "{cps=20}I have a cute idea.{/cps}"
    m "{cps=20}What?{/cps}"
    e "{cps=20}Take these papers and each one draw a symbol.{/cps}"
    t "{cps=20}Sounds fun.{/cps}"
    m "{cps=20}A differenet symbol on each one?{/cps}"
    e "{cps=20}NOO the same one in each paper.{/cps}"
    e "{cps=20}Userkaf draw in the second corner here.{/cps}"
    u "{cps=20}Okay Eya.{/cps}"

    menu:
        "Draw the Eye of Ra'":
            pause 2.0
            u "{cps=20}Okay done.{/cps}"
            $ papy = 1
        "Draw two pyramids":
            pause 2.0
            u "{cps=20}Okay done.{/cps}"
            $ papy = 2
        "Draw an Ankh":
            pause 2.0
            u "{cps=20}Okay done.{/cps}"
            $ papy = 3
        "Draw Kah":
            pause 2.0
            u "{cps=20}Okay done.{/cps}"
            $ papy = 4
    
    $ papyrusN = "papyrus %d" % papy 

    pause 5.0

    e "{cps=20}Okay, here everyone.{/cps}"
    pause 3.0


    e "{cps=20}The time is too late.{/cps}"
    
    menu:
        "Go with them": 
            u "{cps=20}I'll come with you.{/cps}"
            t "{cps=20}No no need, we don't want to tire you.{/cps}"
            u "{cps=20}No I insist.{/cps}"
            menu:
                "Tell Minas 'See you tommorow Minas.'":
                    u "{cps=20}See you tommorow Minas.{/cps}"
                    m "{cps=20}See you.{/cps}"
                    show minas h at p1, hideFade with dissolve
                    play sound sfx_disappear
                    hide minas h
                    show userkaf h at p2, hideFade with dissolve
                    hide userkaf h
                    play sound sfx_disappear
                    show eya h at p3, hideFade with dissolve
                    play sound sfx_disappear
                    hide eya h
                    show tausert h at p4, hideFade with dissolve
                    play sound sfx_disappear
                    hide tausert h
                    pause 1.0
                    jump d3s1
                "Tell Minas 'Why don't you come with us Minas?'":
                    u "{cps=20}Why don't you come with us Minas?{/cps}"
                    m "{cps=20}I'm tired, I'm going home.{/cps}"
                    u "{cps=20}Okay take care bro.{/cps}"
                    show minas h at p1, hideFade with dissolve
                    play sound sfx_disappear
                    hide minas h
                    show userkaf h at p2, hideFade with dissolve
                    hide userkaf h
                    play sound sfx_disappear
                    show eya h at p3, hideFade with dissolve
                    play sound sfx_disappear
                    hide eya h
                    show tausert h at p4, hideFade with dissolve
                    play sound sfx_disappear
                    hide tausert h
                    pause 1.0
                    pause 1.0
                    jump d3s1
        "Tell Minas to go with them":
            u "{cps=20}Minas can you go with them?{/cps}"
            m "{cps=20}Yeah sure.{/cps}"
            t "{cps=20}No no need, we don't want to tire you.{/cps}"
            m "{cps=20}No I insist.{/cps}"
            e "{cps=20}Where are you going Userkaf?{/cps}"
            menu:
                "Say 'I'm coming with you.'":
                    u "{cps=20}I'm coming with you.{/cps}"
                    e "{cps=20}Let's go then.{/cps}"
                    $ mincome = 1
                    show minas h at p1, hideFade with dissolve
                    play sound sfx_disappear
                    hide minas h
                    show userkaf h at p2, hideFade with dissolve
                    hide userkaf h
                    play sound sfx_disappear
                    show eya h at p3, hideFade with dissolve
                    play sound sfx_disappear
                    hide eya h
                    show tausert h at p4, hideFade with dissolve
                    play sound sfx_disappear
                    hide tausert h
                    pause 1.0
                    pause 1.0
                    jump d3s1
                "Say 'I'm going home.'":
                    u "{cps=20}I'm going home.{/cps}"
                    e "{cps=20}See you later.{/cps}"
                    t "{cps=20}Bye Userkaf.{/cps}"
                    m "{cps=20}Take care bro.{/cps}"
                    show minas h at p1, hideFade with dissolve
                    play sound sfx_disappear
                    hide minas h
                    show eya h at p3, hideFade with dissolve
                    play sound sfx_disappear
                    hide eya h
                    show tausert h at p4, hideFade with dissolve
                    play sound sfx_disappear
                    hide tausert h
                    pause 1.0
                    pause 1.0

    menu:
        "Go back":      
            show userkaf h at p2, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf h

            jump d3s01
        "Follow them":            
            show userkaf h at p2, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf h

            jump d3s11



    return

label d3s01:
    scene bg street1 n with pixellate
    play music music_night fadein 1.0

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear

    pause 1.0
    u "{cps=20}The stranger didn't show up today.{/cps}"
    
    menu:
        "Go home":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear

            hide userkaf n
            jump d3r2
        "Go to the palm tree":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear

            hide userkaf n
            jump d3p3
        "Go to the square":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear

            hide userkaf n
            jump d3q3

    return


label d3q3:
    scene bg square3 with pixellate
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
            jump d3s01
        
    return

label d3p3:
    scene bg palm3 with pixellate
    play music music_rivernight fadein 1.0
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
            jump d3s01
        
    return


label d3s1:
    scene bg eya n with pixellate
    play music music_night fadein 1.0
    pause 1.0

    $ housee = 1

    show tausert h at p1, showFade
    play sound sfx_appear

    show eya h at p2, showFade
    play sound sfx_appear

    show userkaf h at p3, showFade
    play sound sfx_appear

    if mincome == 1:
        show minas h at p4, showFade
        play sound sfx_appear

    pause 1.0

    
    if mincome == 0:
        e "{cps=20}Thank you very much Userkaf.{/cps}"
    else:
        e "{cps=20}Thank you very much guys.{/cps}"

    if mincome == 0:
        t "{cps=20}Thanks Userkaf.{/cps}"
    else:
        t "{cps=20}Thanks guys.{/cps}"
    u "{cps=20}You're welcome ...{/cps}"
    if mincome == 0:
        t "{cps=20}We're team.{/cps}"
    else:
        m "{cps=20}We're team.{/cps}"

    e "{cps=20}I hope we win.{/cps}"
    e "{cps=20}See you soon.{/cps}"
    u "{cps=20}Goodbye guys.{/cps}"
    

    if mincome == 1:
        show minas n at p4, hideFade with dissolve
        play sound sfx_disappear
        hide minas n

    show userkaf n at p3, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n


    pause 1.0

    jump d3s01

    return


label d3s11:
    scene bg eya n with pixellate
    play music music_night fadein 1.0
    pause 1.0

    $ housee = 1



    show tausert h at p1, showFade
    play sound sfx_appear
    show eya h at p2, showFade
    play sound sfx_appear

    show minas h at p4, showFade
    play sound sfx_appear

    pause 1.0

    
    e "{cps=20}Thank you very much Minas.{/cps}"
    t "{cps=20}Thanks Minas.{/cps}"
    u "{cps=20}You're welcome ...{/cps}"
    m "{cps=20}We're team.{/cps}"

    e "{cps=20}I hope we win.{/cps}"
    e "{cps=20}See you soon.{/cps}"
    m "{cps=20}Goodbye guys.{/cps}"

    show minas n at p4, hideFade with dissolve
    play sound sfx_disappear
    hide minas n

    pause 2.0

    show eya h at p2, hideFade with dissolve
    play sound sfx_disappear
    hide eya h
    show tausert h at p1, hideFade with dissolve
    play sound sfx_disappear
    hide tausert h

    pause 4.0

    show userkaf n at right, showFade
    play sound sfx_appear

    pause 1.0
    u "{cps=20}Mhm.{/cps}"
    show userkaf n at right, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n

    jump d3s01

    return



label d3r2:
    scene bg ubd3
    with pixellate
    pause 1.0

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

            if housee == 1:
                u "{cps=20}I'm so sleepy.{/cps}"
            else:
                u "{cps=20}I should have gone with them.{/cps}"

            show mirror3 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror3
            jump d3r2


        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d3k2

        "Check Eya's paper":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0

            scene bg ubd3 at showBlur
            play sound sfx_paper
            
            show expression papyrusN with dissolve

            u "{cps=20}I will never throw it.{/cps}"


            show expression papyrusN at hideFade with dissolve
            play sound sfx_disappear
            hide expression papyrusN
            jump d3r2

        "Sleep":
            play sound sfx_sleep
            jump day4

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d3s01


    return

label d3k2:
    scene bg kitchen3
    with pixellate
    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear

    pause 1.0
    
    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d3k2

    
        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d3r2    

    return    
