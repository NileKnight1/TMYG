default d9sc = ""
default d9pap = 0
default d9let = 0
default ds9 = 0

label day9:
    $ renpy.music.set_volume(1, delay=0, channel='music')
    $ renpy.music.set_volume(0.4, delay=0, channel='music2')
    
    jump d9r1

label d9r1:

    scene bg ubd1 with pixellate
    if(ds9 == 0):
        $ ds9 = 1
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

            u "{cps=20}I'm confessing today.{/cps}"


            show mirror1 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror1
            jump d9r1

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
            jump d9r1

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d9k1

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d9s1

    return

label d9k1:
    scene bg kitchen1 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d9k1

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d9r1

    return

label d9s1:
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
            jump d9r1
        "Go to the palm tree":
            $ d9sc = "palm"
            jump d9sp1
        "Go to the square":
            $ d9sc = "square"
            jump d9sp1
        "Go to Eya":
            $ d9sc = "eya"
            jump d9e1
        "Go to the temple":
            $ d9sc = "temple"
            jump d9sp1


    return

label d9sp1:
    show userkaf n at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0
    
    if d9sc == "palm":
        scene bg palm1 with pixellate
        play music music_rivermorning fadein 1.0
    elif d9sc == "temple":
        scene bg street3 with pixellate
        play music music_jungle fadein 1.0
    elif d9sc == "square":
        scene bg square with pixellate
        play music music_morning fadein 1.0
    elif d9sc == "eya":
        scene bg eya m with pixellate
        play music music_morning fadein 1.0


    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    if d9sc != "temple":
        u "{cps=20}Nothing to do here.{/cps}"
    
    menu:
        "Enter the temple" if (d9sc == "temple"):
            show userkaf n at center, hideFade with dissolve
            hide userkaf n
            pause 1.0
            scene bg temple4 with pixellate
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
                    jump d9sp1



        "Go back":
            show userkaf n at center, hideFade with dissolve
            hide userkaf n
            pause 1.0
            jump d9s1

    return


label d9e1:
    scene bg eya m with pixellate
    play music music_morning fadein 1.0
    pause 1.0

    show userkaf n at right, showFade
    play sound sfx_appear
    pause 1.0

    u "{cps=20}Eya!{/cps}"
    pause 1.0

    show eya n at left, showFade
    play sound sfx_appear
    pause 1.0    

    e "{cps=20}Hi Userkaf.{/cps}"
    u "{cps=20}Hey Eya.{/cps}"
    e "{cps=20}How is your dad now?{/cps}"
    u "{cps=20}He's getting better?{/cps}"
    show eya h at left
    e "{cps=20}Great.{/cps}"
    pause 1.0
    show eya c at left
    show userkaf h at right
    u "{cps=20}Eya ...{w=0.5}{nw}{/cps}"
    u "{cps=20}I ...{nw}{/cps}"
    e "{cps=20}You what?{/cps}"
    show userkaf b at right
    play music2 music_calm fadein 1.0
    u "{cps=20}Do you know when a puzzle is missing a piece?{/cps}"
    u "{cps=20}Or seeing a pink flower growing between tress?{/cps}"
    u "{cps=20}Or when someone sees his future fate?{/cps}"
    u "{cps=20}Or when someone finds his soulmate?{/cps}"
    show eya h at left
    e "{cps=20}Oh my God you're a poet.{/cps}"
    u "{cps=20}You liked it?{/cps}"
    show eya c at left
    e "{cps=20}Yeah .. who did you write it to?{/cps}"
    u "{cps=20}For my soulmate.{/cps}"
    e "{cps=20}Cute .. what's her name?{/cps}"
    u "{cps=20}Her name is {w=0.4}Eya.{/cps}"
    show eya z at left
    e "{cps=20}Wow we share the same name.{/cps}"
    play sound sfx_rewind
    stop music2
    show userkaf n at right
    show eya n at left
    u "{cps=20}Why are you acting dumb Eya?{/cps}"
    e "{cps=20}I'm not.{/cps}"
    u "{cps=20}You never expected that I love you??{/cps}"
    e "{cps=20}No.{/cps}"
    u "{cps=20}Forget it.{/cps}"
    e "{cps=20}Userkaf .. you're a great person but ...{/cps}"
    u "{cps=20}What?{/cps}"
    e "{cps=20}I like Minas.{/cps}"
    u "{cps=20}Okay.{/cps}"
    e "{cps=20}Then what?{/cps}"
    u "{cps=20}I'm done.{/cps}"
    e "{cps=20}See you then.{/cps}"
    pause 1.0
    show eya n at left, hideFade with dissolve
    play sound sfx_disappear
    hide eya n
    pause 1.0
    show userkaf s at right

    menu:
        "Go back":
            show userkaf s at right, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            pause 1.0
            jump d9s2

label d9r2:

    scene bg ubd1 with pixellate
    play music music_morning fadein 1.0
    show userkaf s at left, showFade
    play sound sfx_appear
    pause 1.0


    menu:
        "Look in the mirror":
            show userkaf s at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            pause 1.0

            scene bg ubd1 at showBlur
            play sound sfx_magic
            
            
            show mirror8 with dissolve

            u "{cps=20}I don't want to live.{/cps}"


            show mirror8 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror8
            jump d9r2

        "Check Eya's paper":
            show userkaf s at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            pause 1.0

            scene bg ubd1 at showBlur
            play sound sfx_paper
            
            show expression papyrusN with dissolve

            " "


            show expression papyrusN at hideFade with dissolve
            play sound sfx_disappear
            hide expression papyrusN
            jump d9r2

        "Go to the kitchen":
            show userkaf s at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            jump d9k2

        "Go out":
            show userkaf s at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            jump d9s2

    return

label d9k2:
    scene bg kitchen1 with pixellate

    pause 1.0
    show userkaf s at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Suicide":
            play sound sfx_faintdrop
            scene bg kitchen1-4
            show userkaf s at left

            pause 1.0

            

            show umom s at right with vpunch
            um "{cps=20}Userkaf nooo.{/cps}"
            um "{cps=20}WHAT ARE YOU DOING?{/cps}"
            u "{cps=20}I'm tired of life ...{nw}{/cps}"
            u "{cps=20}Everything is against me ...{nw}{/cps}"
            u "{cps=20}Even the girl I loved the most ...{/cps}"
            um "{cps=20}Who is she?{/cps}"
            u "{cps=20}She was in my team.{/cps}"
            um "{cps=20}You have to know that life is always hard.{/cps}"
            um "{cps=20}And we never get everything we want.{/cps}"
            um "{cps=20}You have to belive that God has written the better for you.{/cps}"
            um "{cps=20}Just wait Userkaf ...{/cps}"
            um "{cps=20}Just wait.{/cps}"
            u "{cps=20}But I wanted her.{/cps}"
            u "{cps=20}I never felt alike that feeling.{/cps}"
            u "{cps=20}She is ...{nw}{/cps}"
            u "{cps=20}She is a princess!{/cps}"
            um "{cps=20}I feel you Userkaf.{/cps}"
            um "{cps=20}You'll meet a better one.{/cps}"
            show userkaf h at left
            um "{cps=20}Remember my words.{/cps}"
            u "{cps=20}Thank you mom.{/cps}"
            um "{cps=20}Someone left you a letter .. I put it in your room.{/cps}"
            u "{cps=20}I will check it out.{/cps}"
            pause 1.0
            show userkaf h at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf h
            pause 1.0

            jump d9r3
            

        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d9k2

        "Go back to your room":
            show userkaf s at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            pause 1.0
            jump d9r2

    return



label d9s2:
    scene bg street1 m with pixellate
    play music music_morning fadein 1.0
    pause 1.0
    show userkaf s at left, showFade
    play sound sfx_appear
    pause 1.0


    menu:
        "Go back home":
            show userkaf s at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            jump d9r2
        "Go to the palm tree":
            $ d9sc = "palm"
            jump d9sp2
        "Go to the square":
            $ d9sc = "square"
            jump d9sp2
        "Go to the temple":
            $ d9sc = "temple"
            jump d9sp2


    return

label d9sp2:
    show userkaf s at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf s
    pause 1.0
    
    if d9sc == "palm":
        scene bg palm1 with pixellate
        play music music_rivermorning fadein 1.0
    elif d9sc == "temple":
        scene bg street3 with pixellate
        play music music_jungle fadein 1.0
    elif d9sc == "square":
        scene bg square with pixellate
        play music music_morning fadein 1.0


    pause 1.0
    show userkaf s at center, showFade
    play sound sfx_appear
    pause 1.0

    if d9sc != "temple":
        u "{cps=20}Nothing to do here.{/cps}"
    
    menu:
        "Enter the temple" if (d9sc == "temple"):
            show userkaf s at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            pause 1.0
            
            scene bg temple4 with pixellate
            pause 1.0
            show userkaf s at center, showFade
            play sound sfx_appear
            pause 1.0
            u "{cps=20}Nothing to do here.{/cps}"
            menu:
                "Go back":
                    show userkaf s at center, hideFade with dissolve
                    play sound sfx_disappear
                    hide userkaf s
                    pause 1.0
                    jump d9sp2



        "Go back":
            show userkaf s at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf s
            pause 1.0
            jump d9s2

    return


label d9r3:

    scene bg ubd1 with pixellate
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
            
            
            show mirror8 with dissolve

            if(d9let == 0):
                u "{cps=20}She doesn't deserve me.{/cps}"
            else:
                u "{cps=20}Let's party.{/cps}"


            show mirror8 at hideFade with dissolve
            play sound sfx_disappear
            hide mirror8
            jump d9r3

        "Read the letter":
            $ d9let = 1
            play sound sfx_magic
            e "{cps=20}Sorry for what I've said ... {w=0.2}Meet us under the palm tree ... {w=0.3} Waiting for you!{/cps}"
            jump d9r3

        "Bring Eya's paper" if(d9pap == 0):
            play sound sfx_magic
            $ d9pap = 1
            jump d9r3

        "Go to the kitchen":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d9k3

        "Go out":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            jump d9s3

    return

label d9k3:
    scene bg kitchen1-4 with pixellate

    pause 1.0
    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0

    menu:
        "Eat an apple":
            play sound sfx_apple
            u "{cps=20}Tasty.{/cps}"
            jump d9k3

        "Go back to your room":
            show userkaf n at left, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d9r3

    return

label d9s3:
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
            jump d9r3
        "Go to the palm tree":
            if (d9let == 1):
                show userkaf n at left, hideFade with dissolve
                play sound sfx_disappear
                hide userkaf n
                jump d9p1
            $ d9sc = "palm"
            jump d9sp3
        "Go to the square":
            $ d9sc = "square"
            jump d9sp3
        "Go to the temple":
            $ d9sc = "temple"
            jump d9sp3


    return

label d9sp3:
    show userkaf n at left, hideFade with dissolve
    play sound sfx_disappear
    hide userkaf n
    pause 1.0
    
    if d9sc == "palm":
        scene bg palm1 with pixellate
        play music music_morning fadein 1.0
    elif d9sc == "temple":
        scene bg street3 with pixellate
        play music music_jungle fadein 1.0
    elif d9sc == "square":
        scene bg square with pixellate
        play music music_morning fadein 1.0


    pause 1.0
    show userkaf n at center, showFade
    play sound sfx_appear
    pause 1.0

    if d9sc != "temple":
        u "{cps=20}Nothing to do here.{/cps}"
    
    menu:
        "Enter the temple" if (d9sc == "temple"):
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            scene bg temple4 with pixellate
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
                    jump d9sp3



        "Go back":
            show userkaf n at center, hideFade with dissolve
            play sound sfx_disappear
            hide userkaf n
            pause 1.0
            jump d9s3

    return

label d9p1:
    scene bg palm1 with pixellate
    play music music_rivermorning fadein 1.0

    pause 1.0
    $ renpy.music.set_volume(0.8, delay=0, channel='music')
    $ renpy.music.set_volume(0.2, delay=0, channel='music2')
    play music2 music_mis fadein 1.0

    show userkaf n at left, showFade
    play sound sfx_appear
    pause 1.0
    show userkaf c at left
    u "{cps=20}Where are they?{/cps}"
    
    play sound sfx_confusion
    ss "{cps=20}Who are they?{/cps}"
    show stranger at right, showFade
    play sound sfx_sudden
    pause 1.0

    u "{cps=20}What are you doing here?{/cps}"
    ss "{cps=20}Meeting you.{/cps}"
    u "{cps=20}Huh?{/cps}"
    u "{cps=20}You sent me the letter?{/cps}"
    ss "{cps=20}I did.{/cps}"
    u "{cps=20}How did you know my house.{/cps}"
    ss "{cps=20}It doesn't matter.{/cps}"
    u "{cps=20}Why do you limp?{/cps}"
    ss "{cps=20}Because of you.{/cps}"
    u "{cps=20}You're acting weird today.{/cps}"
    show stranger at left with moveinright
    play sound sfx_push
    show stranger at right
    show userkaf s at left 
    ss "{cps=20}Am I?{/cps}"
    u "{cps=20}Why are you hitting me?{/cps}"
    show stranger at left with moveinright
    play sound sfx_push

    show stranger at right
    ss "{cps=20}Because you deserve death.{/cps}"
    show userkaf d at left
    u "{cps=20}Hit me one more time.{/cps}"
    ss "{cps=20}Sure.{nw}{/cps}"
    show stranger at left with moveinright
    stop music2
    play sound sfx_stab
    $ renpy.music.set_volume(0.1, delay=0, channel='music2')
    show stranger c1 at right    
    ss "{cps=20}Ahhh.{/cps}"

    u "{cps=20}Who sent you?{/cps}"
    play sound sfx_faintdrop
    show stranger c2 at right
    ss "{cps=20}No one.{/cps}"
    play sound sfx_amazed
    show stranger c3 at right


    play music2 music_mine fadein 2.0
    show userkaf z at left
    u "{cps=20}You were the stranger all time?{/cps}"
    m "{cps=20}I was.{/cps}"
    show userkaf n at left
    u "{cps=20}And you were the monster, weren't you?{/cps}"
    show stranger c4 at right
    m "{cps=20}I was.{/cps}"
    show stranger c3 at right

    u "{cps=20}Why? Why did you do all of this?{/cps}"
    m "{cps=20}I just wanted what you wanted.{/cps}"
    u "{cps=20}Eya?{/cps}"
    m "{cps=20}Yes.{/cps}"
    u "{cps=20}You won her .. she loves you.{/cps}"
    show stranger c4 at right

    m "{cps=20}I know.{/cps}"
    show stranger c3 at right
    u "{cps=20}And my father?{/cps}"
    m "{cps=20}He threatened me because he saw me cheating in the draw numbers.{/cps}"
    m "{cps=20}So I kidnapped him and cut his tongue to prevent him saying my name again.{/cps}"
    u "{cps=20}You are a monster.{/cps}"
    m "{cps=20}I know.{/cps}"
    u "{cps=20}But you lost everything in the end.{/cps}"
    m "{cps=20}At least I didn't lost alone.{/cps}"
    u "{cps=20}I never expected all that from you Minas.{/cps}"
    u "{cps=20}You were my best friend!{/cps}"
    m "{cps=20}Love is a disease.{/cps}"
    u "{cps=20}That's true.{/cps}"
    m "{cps=20}So what now?{/cps}"
    u "{cps=20}Everyone gets what he deserves.{/cps}"
    m "{cps=20}And what do you deserve?{/cps}"
    u "{cps=20}To rule Egypt.{/cps}"
    show stranger c4 at right
    m "{cps=20}You never failed to make me laugh.{/cps}"
    show stranger c3 at right
    u "{cps=20}Now goodbye.{/cps}"
    m "{cps=20}Are you leaving me?{/cps}"

    menu:
        "Push him":
            stop music2
            scene black
            play sound sfx_push
            pause 1.0
            play sound sfx_water
            $ pau(2)
            play sound sfx_sun fadeout 1.0
            stop music fadeout 3.0
            u "{cps=20}Your dinner is served.{/cps}"
            

    ""
    return

























