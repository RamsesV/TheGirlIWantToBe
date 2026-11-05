screen decision_choice(decision):

    modal True
    roll_forward False

    add Solid("#14111c")

    vbox:
        xalign 0.5
        ypos 90
        spacing 24

        text _(decision["prompt"]):
            xsize 1500
            size 36
            color "#ffffff"

        hbox:
            spacing 24

            text _("Walkthrough:"):
                size 24

            for mode, caption in (
                ("off", _("Off")),
                ("hints", _("Hints")),
                ("full", _("Full")),
            ):

                textbutton _(caption):
                    id ("walkthrough_" + mode)
                    text_size 24
                    selected (
                        persistent.walkthrough_mode == mode
                    )
                    action SetField(
                        persistent,
                        "walkthrough_mode",
                        mode,
                    )

        for option in decision["options"]:

            vbox:
                xsize 1500
                spacing 8

                button:
                    id ("decision_option_" + option["id"])

                    xfill True
                    padding (20, 14)

                    background Solid("#30263c")
                    hover_background Solid("#55356e")
                    insensitive_background Solid("#211d27")

                    sensitive decision_available(option, player)
                    action Return(option["id"])

                    text _(option["text"]):
                        size 28
                        color (
                            "#ffffff"
                            if decision_available(option, player)
                            else "#81768b"
                        )

                if persistent.walkthrough_mode == "hints":

                    text _(option["hint"]):
                        id ("decision_hint_" + option["id"])
                        size 22
                        color "#cbb5df"

                elif persistent.walkthrough_mode == "full":

                    text decision_details(option, player):
                        id ("decision_details_" + option["id"])
                        xsize 1500
                        size 22
                        color "#cbb5df"