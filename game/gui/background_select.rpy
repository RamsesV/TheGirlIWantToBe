screen background_select():

    modal True
    roll_forward False

    default selected_background = None

    add Solid("#1b1521")

    text _("Who were you before you arrived?"):
        xalign 0.5
        ypos 32

        font "fonts/CormorantGaramond-Regular.otf"
        size 58
        color "#f5e7d4"

    text _("Choose your background. Your story is still yours to shape."):
        xalign 0.5
        ypos 105

        size 24
        color "#c9bab9"

    add Solid("#ef927e40"):
        xpos 96
        ypos 148
        xysize (1728, 2)

    hbox:
        xalign 0.5
        ypos 170
        spacing 24

        for background_id in (
            "bookworm",
            "girl_next_door",
            "social_butterfly",
        ):

            button:
                id ("background_" + background_id)

                style "background_card"

                selected (selected_background == background_id)

                action SetScreenVariable(
                    "selected_background",
                    background_id,
                )

                vbox:
                    xsize 512
                    spacing 12

                    text _(BACKGROUNDS[background_id]["name"]):
                        xalign 0.5

                        font "fonts/CormorantGaramond-Regular.otf"
                        size 44

                        color (
                            "#ef927e"
                            if selected_background == background_id
                            else "#f5e7d4"
                        )

                    fixed:
                        xysize (512, 460)

                        add BACKGROUND_PORTRAITS[background_id]:
                            xalign 0.5
                            yalign 0.5

                            xysize (304, 456)

                    text _("INT {intellect}   STA {stamina}   CHA {charisma}").format(
                        **BACKGROUNDS[background_id]["attributes"]
                    ):
                        xalign 0.5

                        size 24
                        color "#e3d4c7"

                    add Solid(
                        "#ef927e"
                        if selected_background == background_id
                        else "#594351"
                    ):
                        xalign 0.5
                        xysize (160, 3)

    vbox:
        xpos 96
        ypos 840

        xsize 1200
        spacing 10

        if selected_background is not None:

            text _(BACKGROUNDS[selected_background]["name"]):
                font "fonts/CormorantGaramond-Regular.otf"

                size 34
                color "#ef927e"

            text _(BACKGROUND_DESCRIPTIONS[selected_background]):
                xsize 1200

                size 23
                color "#e3d4c7"

        else:

            text _("Every story starts somewhere."):
                font "fonts/CormorantGaramond-Regular.otf"

                size 34
                color "#ef927e"

            text _("Select a background above to read her story and confirm your choice."):
                xsize 1200

                size 23
                color "#c9bab9"

    textbutton _("Begin"):
        id "background_begin"

        style "background_begin_button"

        xpos 1504
        ypos 930

        sensitive (selected_background is not None)

        action Return(selected_background)


style background_card is button:

    xysize (560, 640)
    padding (24, 20)

    background Solid("#2b2232")
    hover_background Solid("#382a3c")

    selected_background Solid("#44303b")
    selected_hover_background Solid("#4e3743")


style background_begin_button is button:

    xysize (320, 68)
    padding (12, 8)

    background Solid("#ef927e")
    hover_background Solid("#f5b09b")

    insensitive_background Solid("#352b3d")


style background_begin_button_text is gui_text:

    size 30

    color "#211b29"
    hover_color "#211b29"
    insensitive_color "#8e818b"

    xalign 0.5
    yalign 0.5