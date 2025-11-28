default d8sc = ""
default d8schat = 0
default d8rchat = 0
default ds8 = 0




label day8:
    $ renpy.music.set_volume(1, delay=0, channel='music')
    $ renpy.music.set_volume(0.4, delay=0, channel='music2')
    jump d8r1

    return


label d8r1:

    scene bg ubd1 with pixellate
    if(ds8 == 0):
        $ ds8 = 1
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

            u "{cps=20}Today is the last one.{/cps}"


            show mirror1 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror1
            jump d8r1

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
            jump d8r1

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d8k1

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d8s1

    return

label d8k1:
    scene bg kitchen1 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d8k1

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d8r1

    return

label d8s1:
    scene bg street1 m with pixellate
    play music music_morning fadein 1.0
    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    if(d8schat == 0):
        $ d8schat = 1
        show minas n at right, showFade
        play sound sfx_appear
        pause 1.0
        show userkaf c at left
        u "{cps=20}Minas?{/cps}"
        m "{cps=20}Hello Userkaf.{/cps}"
        u "{cps=20}Did you fake the results yesterday?{/cps}"
        show minas c at right
        m "{cps=20}No?{/cps}"
        u "{cps=20}But we heard a guard talking with the Cheif about someone who faked it.{/cps}"
        m "{cps=20}It's not me then.{/cps}"
        u "{cps=20}And where were you all day?{/cps}"
        m "{cps=20}I was just busy.{/cps}"
        u "{cps=20}Why are you carrying these apples with you?{/cps}"
        m "{cps=20}I .. I .. {nw}{/cps}"
        m "{cps=20}What are all these questions?{/cps}"
        u "{cps=20}Okay nevermind.{/cps}"
        u "{cps=20}See you in the contest.{/cps}"
        m "{cps=20}Sure.{/cps}"
        pause 1.0
        show userkaf n at left
        show minas n at right, hideFade with dissolve
        play sound sfx_disappear
        hide minas n
        pause 1.0

    menu:
        "Go back home":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d8r1
        "Go to the palm tree":
            $ d8sc = "palm"
            jump d8sp1
        "Go to the square":
            jump d8q1
        "Go to Eya":
            $ d8sc = "eya"
            jump d8sp1
        #"Go to the temple":
        #    $ d8sc = "temple"
        #    jump d8sp1


    return

label d8sp1:
    show userkaf n at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0
    
    if d8sc == "palm":
        scene bg palm1 with pixellate
        play music music_rivermorning fadein 1.0
    elif d8sc == "temple":
        scene bg street3 with pixellate
        play music music_jungle fadein 1.0

    elif d8sc == "eya":
        scene bg eya m with pixellate
        play music music_morning fadein 1.0


    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    if d8sc != "temple":
        u "{cps=20}Nothing to do here.{/cps}"
    
    menu:
        "Enter the temple" if (d8sc == "temple"):
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
                    jump d8sp1



        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d8s1

    return



label d8q1:
    scene bg square with pixellate
    play music music_morning fadein 1.0
    pause 1.0

    show userkaf n at p2, showFade
    play sound sfx_appear
    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Hi.{/cps}"
    e "{cps=20}Hi.{nw}{/cps}"
    t "{cps=20}Hi.{/cps}"

    e "{cps=20}Where's Minas?{/cps}"
    u "{cps=20}I saw him on my way.{/cps}"
    t "{cps=20}Why didn't he come with you?{/cps}"
    u "{cps=20}I don't know.{/cps}"
    e "{cps=20}That's weird.{/cps}"
    
    play sound sfx_amazed
    V "{cps=20}SILENCE.{/cps}"
    show userkaf n at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    show eya n at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya n
    show tausert n at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert n

    show cheif at center, showFade
    play sound sfx_appear
    pause 1.0

    V "{cps=10}Welcome kids ...{/cps}"
    V "{cps=10}On the last day of our contest ...{/cps}"
    V "{cps=10}The last 4 teams will compete on the title ...{/cps}"
    V "{cps=10}The Guardians Of The Nile ...{/cps}"
    V "{cps=10}We have only one game ...{/cps}"
    V "{cps=10}Each team will ride a boat ...{/cps}"
    V "{cps=10}And race in the Nile ...{/cps}"
    V "{cps=10}Get ready.{/cps}"

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

    m "{cps=20}Hello guys.{/cps}"
    show minas c at p1
    t "{cps=20}Welcome Mr. Cheater.{/cps}"
    show minas n at p1
    m "{cps=20}I'm not.{/cps}"
    t "{cps=20}Whatever.{/cps}"
    e "{cps=20}We have to focus guys.{/cps}"
    u "{cps=20}Don't worry Eya.{/cps}"

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

    jump d8q2


label d8q2:
    
    scene bg raceday1 with pixellate
    play music music_rivermorning fadein 1.0
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

    e "{cps=20}Ready guys?{/cps}"
    t "{cps=20}Yes leader.{/cps}"
    u "{cps=20}We will win this .. and find my dad.{/cps}"
    e "{cps=20}We will Userkaf.{/cps}"
    u "{cps=20}Eya.{/cps}"
    e "{cps=20}Yes?{/cps}"
    show eya c at p3
    u "{cps=20}Remind me to tell you something after the contest.{/cps}"
    show eya n at p3
    e "{cps=20}Sure.{/cps}"

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

    scene black with fade
    $ pau(5)
    
    scene bg raceday2 with pixellate
    play music music_rivermorning fadein 1.0
    pause 1.0


    pause 1.0    
    show userkaf h at p2, showFade
    play sound sfx_appear
    show minas h at p1, showFade
    play sound sfx_appear
    show eya h at p3, showFade
    play sound sfx_appear
    show tausert h at p4, showFade
    play sound sfx_appear
    pause 1.0


    e "{cps=20}Oh my God we did it.{/cps}"
    t "{cps=20}WE WON THE TITLE!{/cps}"
    u "{cps=20}Hahaha!{/cps}"

    V "{cps=10}Congratulations kids.{/cps}"
    V "{cps=10}You deserve this title.{/cps}"
    pause 1.0

    V "{cps=10}Userkaf I wanted to tell you something in private.{/cps}"
    u "{cps=20}Sure Cheif.{/cps}"
    pause 1.0

    show minas n at p1, hideFade with dissolve
    play sound sfx_disappear
    hide minas n
    show eya n at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya n
    show tausert n at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert n
    pause 1.0    
    show cheif at p3, showFade
    play sound sfx_appear
    pause 1.0

    show userkaf c at p2
    V "{cps=10}I know that the cheater was Minas ...{/cps}"
    V "{cps=10}And I also know that you and the girls aren't involved in this ...{/cps}"
    V "{cps=10}So I decided to turn a blind eye.{/cps}"
    u "{cps=20}How did you know it's Minas?{/cps}"
    V "{cps=10}He did a similar thing on the opening day.{/cps}"
    u "{cps=20}What did he do?{/cps}"
    show userkaf z at p2
    V "{cps=10}When he saw Eya's number .. he approached me and asked me to give him like her.{/cps}"
    show userkaf n at p2
    u "{cps=20}What did you do with him?{/cps}"
    show userkaf z at p2
    V "{cps=10}I told him that your father was the one who had the numbers.{/cps}"
    V "{cps=10}I'm afraid this is related to his disappearance.{/cps}"
    u "{cps=20}Oh my God.{/cps}"
    u "{cps=20}I can't think of him doing that.{/cps}"
    V "{cps=10}Be wise Userkaf ...{/cps}"
    V "{cps=10}You are one of the Guardians Of The Nile.{/cps}"
    show userkaf h at p2
    u "{cps=20}Thank you Cheif .. I'll find my father .. I believe.{/cps}"
    V "{cps=10}May God guide you.{/cps}"  
    pause 1.0

    show cheif at p3, hideFade with dissolve
    play sound sfx_disappear
    show userkaf n at p2
    pause 1.0

    show eya n at p3, showFade
    play sound sfx_appear
    show tausert n at p4, showFade
    play sound sfx_appear
    pause 1.0

    show eya c at p3
    show tausert c at p4
    e "{cps=20}What was he telling you?{/cps}"
    show eya z at p3
    show tausert z at p4
    u "{cps=20}He told me that he know Minas is the cheater.{/cps}"
    t "{cps=20}And he left us win?{/cps}"
    u "{cps=20}He knows we're not involved.{/cps}"
    e "{cps=20}A wise man!{/cps}"
    show eya n at p3
    show tausert n at p4
    u "{cps=20}Of course he is the Cheif.{/cps}"
    pause 1.0

    show tausert h at p4
    t "{cps=20}Will we party?{/cps}"
    show tausert n at p4
    u "{cps=20}I won't until I find my father.{/cps}"
    e "{cps=20}We will enter the temple at whatever cost.{/cps}"
    t "{cps=20}I'm with you.{/cps}"
    pause 1.0

    show tausert n at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert n
    show eya n at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya n
    show userkaf n at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n

    pause 1.0

    jump d8t1

label d8t1:
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

    t "{cps=20}What will we do if the monster came again?{/cps}"
    u "{cps=20}I have a plan.{/cps}"
    t "{cps=20}Great.{/cps}"

    pause 1.0
    show tausert n at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert n
    show eya n at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya n
    show userkaf n at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0

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
    t "{cps=20}What are we waiting for? Let's enter.{/cps}"
    u "{cps=20}We're waiting for him.{/cps}"
    show eya c at p3
    t "{cps=20}Who?{/cps}"
    u "{cps=20}The monster.{/cps}"
    e "{cps=20}You got crazy I guess.{/cps}"
    show tausert n at p4
    show eya n at p3
    u "{cps=20}Nah.{/cps}"

    pause 1.0

    show userkaf d at p2
    show eya s at p3
    show tausert s at p4
    show monster at p1, showFade
    play sound sfx_appear
    pause 1.0
    play sound sfx_monster
    pause 1.0

    u "{cps=20}Hiii.{nw}{/cps}"
    u "{cps=20}Into the temple let's goooo.{nw}{/cps}"

    show userkaf d at p2, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf d
    pause 0.2
    show eya s at p3, hideFade with dissolve
    play sound sfx_disappear
    hide eya s
    pause 0.2
    show tausert s at p4, hideFade with dissolve
    play sound sfx_disappear
    hide tausert s
    pause 0.2
    show monster at p1, hideFade with dissolve
    play sound sfx_disappear
    hide monster

    pause 1.0

    scene bg temple1 with pixellate
    play music music_temple fadein 1.0
    pause 1.0

    show userkaf d at p2, showFade
    play sound sfx_appear
    pause 0.2
    show eya s at p3, showFade
    play sound sfx_appear
    pause 0.2
    show tausert s at p4, showFade
    play sound sfx_appear
    pause 0.2
    show monster at p1, showFade
    play sound sfx_appear
    pause 1.0
    play sound sfx_monster
    pause 1.0

    t "{cps=20}Do something Userkaf!{/cps}"
    u "{cps=20}Close the door Eya!{/cps}"

    play sound sfx_temple1
    scene bg temple2 with vpunch
    show monster at p1
    show userkaf d at p2
    show eya s at p3
    show tausert s at p4
    pause 1.0

    show monster at p2 with moveinright
    play sound sfx_monster


    menu:
        "Kick him":
            play sound sfx_push
            show monster at p1 with vpunch
            pause 1.0
            play sound sfx_colapse
            scene black
            $ pau(2) 
            scene bg temple3 with vpunch

    show userkaf h at p2
    show eya z at p3
    show tausert z at p4
    
    e "{cps=20}Oh my God!{/cps}"
    t "{cps=20}Is he dead?{/cps}"
    u "{cps=20}I hope.{/cps}"
    show userkaf n at p2
    show eya n at p3
    show tausert n at p4
    pause 1.0

    u "{cps=20}Now search the place.{/cps}"
    
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
    play sound sfx_temple1
    scene temple4
    
    pause 1.0   

    e "{cps=20}There are some apples here.{/cps}"
    u "{cps=20}Apples? Mhm.{/cps}"
    pause 0.3

    t "{cps=20}Lot of dust here.{/cps}"
    e "{cps=20}Expected.{/cps}"
    pause 0.2

    u "{cps=20}EUREKA.{/cps}"
    u "{cps=20}Come here guys.{/cps}"

    play sound sfx_temple2
    $ pau(2)
    scene temple5 with pixellate
    pause 1.0

    show udad s at p4
    show userkaf z at p3, showFade
    play sound sfx_appear 
    show eya z at p2, showFade
    play sound sfx_appear 
    show tausert z at p1, showFade
    play sound sfx_appear 
    pause 1.0


    u "{cps=20}Dad! DAD!{/cps}"
    ud "{cps=20}Uhewhkaf!{/cps}"
    
    show userkaf s at p3
    show eya s at p2
    show tausert s at p1

    u "{cps=20}He cut your tongue??{/cps}"
    ud "{cps=20}Heah.{/cps}"
    e "{cps=20}That's harsh.{/cps}"
    ud "{cps=20}Keh keh fohm khe mohgkeh.{/cps}"
    u "{cps=20}What are you trying to say?{/cps}"
    ud "{cps=20}KEH KEEEH.{/cps}"
    e "{cps=20}I think he is saying take care.{/cps}"
    t "{cps=20}Don't worry Mr. Userkaf smashed the monster.{/cps}"
    ud "{cps=20}Phewhh.{/cps}"

    show userkaf h at p3
    show eya h at p2
    show tausert h at p1
    u "{cps=20}Let's take you home dad, mom misses you.{/cps}"
    pause 1.0

    show udad s at p4, hideFade with dissolve
    play sound sfx_disappear
    hide udad s
    show userkaf h at p3, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf h
    show eya h at p2, hideFade with dissolve
    play sound sfx_disappear
    hide eya h
    show tausert h at p1, hideFade with dissolve
    play sound sfx_disappear
    hide tausert h

    pause 1.0

    jump d8st1

label d8st1:
    scene bg street1 e with pixellate
    play music music_wind fadein 1.0
    
    pause 1.0

    

    show udad s at p4, showFade
    play sound sfx_appear
    show userkaf n at p3, showFade
    play sound sfx_appear
    show eya n at p2, showFade
    play sound sfx_appear
    show tausert n at p1, showFade
    play sound sfx_appear


    u "{cps=20}Time is late .. go home guys.{/cps}"
    t "{cps=20}Are you sure? Don't you need anything?{/cps}"
    u "{cps=20}No no don't worry ...{/cps}"
    show userkaf h at p3
    u "{cps=20}I don't know how to thank you guys .. I love you.{/cps}"
    show eya h at p2
    show tausert h at p1
    e "{cps=20}You're our friend Userkaf .. no need to thank us.{/cps}"
    pause 0.5
    show eya c at p2
    show userkaf b at p3
    e "{cps=20}What did you want to tell me?{/cps}"
    u "{cps=20}I will tell you tomorrow Eya.{/cps}"
    show eya h at p2
    show userkaf h at p3
    e "{cps=20}I'll wait.{/cps}"
    pause 0.3
    t "{cps=20}See you soon.{/cps}"
    e "{cps=20}Bye.{/cps}"


    pause 1.0
    show tausert h at p1, hideFade with dissolve
    play sound sfx_disappear
    hide tausert h
    show eya h at p2, hideFade with dissolve
    play sound sfx_disappear
    hide eya h
    pause 1.0

    u "{cps=20}Let's go dad.{/cps}"

    pause 1.0
    show udad s at p4, hideFade with dissolve
    play sound sfx_disappear
    hide udad s
    show userkaf h at p3, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf h
    pause 1.0

    jump d8r2




label d8r2:
    scene bg ubd3 with pixellate
    play music music_night fadein 1.0

    if(d8rchat == 0):
        pause 1.0
        $ d8rchat = 1
        show userkaf h at p4, showFade
        play sound sfx_appear
        show udad s at p3, showFade
        play sound sfx_appear
        pause 1.0

        u "{cps=20}Mooom.{/cps}"
        pause 0.3
        show umom h at p2, showFade
        play sound sfx_appear
        pause 1.0

        um "{cps=20}Where were you?! .. I missed you so much.{/cps}"
        show udad h at p3
        ud "{cps=20}Mee koh.{/cps}"
        show umom s at p2
        show udad s at p3
        um "{cps=20}Where is your tongue?{/cps}"
        show userkaf s at p4
        u "{cps=20}He was kidnapped and .. {w=0.2}he cut his tongue.{/cps}"
        um "{cps=20}I will take care of him .. you rest Userkaf.{/cps}"
        show userkaf h at p4
        show udad h at p3
        show umom h at p2
        u "{cps=20}Okay mom.{/cps}"
        pause 1.0

        show umom h  at p2, hideFade with dissolve
        play sound sfx_disappear
        hide umom h
        show udad h at p3, hideFade with dissolve
        play sound sfx_disappear
        hide udad h
        pause 1.0

        show userkaf h at p4, hideFade with dissolve
        play sound sfx_disappear
        hide userkaf h


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

            u "{cps=20}Finally I can sleep.{/cps}"


            show mirror3 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror3
            jump d8r2

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
            jump d8r2

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d8k2

        "Sleep":
            scene black with dissolve
            pause 2.0
            "{cps=20}This could be a beautiful end for the story ...{/cps}"
            "{cps=20}But there is a heart waiting to be set free.{/cps}"
            pause 2.0
            play sound sfx_sleep
            jump day9

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d8s2

    return

label d8k2:
    scene bg kitchen3 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d8k2

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d8r2

    return

label d8s2:
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
            jump d8r2
        "Go to the palm tree":
            $ d8sc = "palm"
            jump d8sp2
        "Go to the square":
            $ d8sc = "square"
            jump d8sp2
        "Go to Eya":
            $ d8sc = "eya"
            jump d8sp2



    return

label d8sp2:
    show userkaf n at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0
    
    if d8sc == "palm":
        scene bg palm3 with pixellate
        play music music_rivernight fadein 1.0
    elif d8sc == "temple":
        scene bg street3 with pixellate
        play music music_jungle fadein 1.0
    elif d8sc == "eya":
        scene bg eya n with pixellate
        play music music_night fadein 1.0
    elif d8sc == "square":
        scene bg square3 with pixellate
        play music music_night fadein 1.0


    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    if d8sc != "temple":
        u "{cps=20}Nothing to do here.{/cps}"
    
    menu:
        "Enter the temple" if (d8sc == "temple"):
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
                    jump d8sp1



        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d8s2

    return





























