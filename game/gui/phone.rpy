screen phone(
    contact_id=None,
    forced=False,
    day="Today",
    clock="17:42",
):

    modal True
    zorder 300
    roll_forward False

    default active_contact = (
        contact_id or next(iter(phone_threads), None)
    )

    key "game_menu" action If(
        forced,
        Return(),
        Hide("phone"),
    )

    # Cover the scene while focusing on the phone.
    # Show the current scene with a soft focus effect.
    add Layer("master"):
        blur 18.0

    # Darken it slightly so the phone remains the focus.
    add Solid("#080c1470")

    fixed:
        xysize (560, 980)
        align (0.5, 0.5)

        add "gui/phone_shell.svg"

        # Phone status bar.
        text clock:
            font gui.interface_text_font
            size 22
            color "#dce5e9"
            pos (46, 30)
            substitute False

        # Conversation header.
        add Solid("#1f2c34"):
            pos (20, 91)
            xysize (520, 102)

        button:
            id "phone_close"

            pos (27, 104)
            xysize (48, 70)
            padding (0, 0)

            background None
            hover_background None

            action If(
                forced,
                Return(),
                Hide("phone"),
            )

            text "‹":
                font gui.interface_text_font
                size 48
                color "#dce5e9"
                align (0.5, 0.5)

        add "gui/phone_avatar.svg":
            pos (83, 110)

        text _(PHONE_CONTACTS.get(active_contact, {}).get("name", "Messages")):
            font gui.interface_text_font
            size 26
            color "#e9edef"

            pos (165, 112)
            xmaximum 340
            substitute False

        text _("Messages"):
            font gui.interface_text_font
            size 18
            color "#a7b4bb"
            pos (165, 150)

        # Scrollable conversation.
        viewport:
            id "phone_messages"

            pos (36, 213)
            xysize (488, 560)

            mousewheel True
            draggable True
            yinitial 1.0

            vbox:
                xsize 488
                spacing 14

                frame:
                    xalign 0.5
                    padding (14, 6)

                    background Transform(
                        Frame("gui/phone_round.svg", 20, 20),
                        matrixcolor=TintMatrix("#18252d"),
                    )

                    text _(day):
                        font gui.interface_text_font
                        size 18
                        color "#a7b4bb"

                for message in phone_threads.get(
                    active_contact, ()
                ):

                    frame:
                        xmaximum 430

                        xalign (
                            1.0 if message["outgoing"]
                            else 0.0
                        )

                        padding (16, 12)

                        background Transform(
                            Frame("gui/phone_round.svg", 20, 20),
                            matrixcolor=TintMatrix(
                                "#005c4b" if message["outgoing"]
                                else "#202c33"
                            ),
                        )

                        vbox:
                            spacing 8

                            if message["image"]:

                                add message["image"]:
                                    xysize (398, 224)

                            text message["text"]:
                                id (
                                    "phone_message_"
                                    + message["id"]
                                )

                                font gui.interface_text_font
                                size 24
                                color "#e9edef"

                                xmaximum 398
                                line_spacing 3
                                substitute False

                            if message["outgoing"]:

                                text "✓✓":
                                    font gui.interface_text_font
                                    size 16
                                    color "#53bdeb"
                                    xalign 1.0

        # Decorative composer; replies are controlled by the story.
        frame:
            pos (36, 800)
            xysize (488, 56)
            padding (18, 10)

            background Transform(
                Frame("gui/phone_round.svg", 20, 20),
                matrixcolor=TintMatrix("#202c33"),
            )

            text _("Message"):
                font gui.interface_text_font
                size 23
                color "#8696a0"
                yalign 0.5

        # Put the phone away using its home indicator.
        button:
            id "phone_home"

            pos (244, 870)
            xysize (72, 72)
            padding (0, 0)

            background None
            hover_background None

            action If(
                forced,
                Return(),
                Hide("phone"),
            )

            text "○":
                font "DejaVuSans.ttf"
                size 64

                color "#dce5e9"
                hover_color "#ffffff"

                align (0.5, 0.5)