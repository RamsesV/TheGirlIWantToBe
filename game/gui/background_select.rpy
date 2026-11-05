define BACKGROUND_DESCRIPTIONS = {
    "bookworm": _(
        "You’ve always felt more at home among bookshelves than on a sports "
        "field. Well-read and curious, you’d rather figure things out than "
        "be the loudest voice in the room. Your long, happy relationship "
        "has been a steady part of your life—but since your move, your "
        "boyfriend is miles away. Now there’s a new place to settle into, "
        "new people to meet, and a world of experiences you’ve only ever "
        "read about."
    ),

    "girl_next_door": _(
        "You’ve always enjoyed a little bit of everything without finding "
        "that one thing that defines you. For years, a happy relationship "
        "was part of the future you pictured—but when you decided to move, "
        "you and your boyfriend chose to go your separate ways. Now you’re "
        "settling into a new place, single for the first time in a long "
        "while. You don’t have it all figured out yet, and for once, that "
        "feels like an opportunity."
    ),

    "social_butterfly": _(
        "You’ve never had much trouble making friends—or talking people "
        "into your plans. Between team sports, parties, and a busy social "
        "life, your schedule rarely stayed empty for long. Moving away "
        "meant leaving familiar faces behind, including your boyfriend. "
        "Neither of you wanted to end a long, happy relationship, so you "
        "agreed to open it. Now you’re finding your feet in a new place, "
        "and you’ve already spotted a few people you’d like to meet."
    ),
}


screen background_select():

    modal True
    roll_forward False

    default selected_background = None

    add Solid("#14111c")

    vbox:
        xalign 0.5
        ypos 50
        spacing 20

        text _("Who were you before you arrived?"):
            xalign 0.5
            size 46
            color "#ffffff"

        text _("Choose your background. Your story is still yours to shape."):
            xalign 0.5
            size 24
            color "#c4bccc"

        hbox:
            xalign 0.5
            spacing 24

            for background_id in (
                "bookworm",
                "girl_next_door",
                "social_butterfly",
            ):

                button:
                    id ("background_" + background_id)

                    xysize (560, 730)
                    padding (24, 24)

                    background Solid("#25202f")
                    hover_background Solid("#342a43")
                    selected_background Solid("#49305e")
                    selected_hover_background Solid("#583970")

                    selected (selected_background == background_id)
                    action SetScreenVariable(
                        "selected_background",
                        background_id,
                    )

                    vbox:
                        spacing 20

                        # Placeholder for a future portrait.
                        frame:
                            xysize (512, 150)
                            padding (0, 0)
                            background Solid("#19151f")

                            text _("Portrait coming soon"):
                                align (0.5, 0.5)
                                size 22
                                color "#9b8fa8"

                        text _(BACKGROUNDS[background_id]["name"]):
                            size 36
                            color "#ffffff"

                        text _("INT {intellect}   STA {stamina}   CHA {charisma}").format(
                            **BACKGROUNDS[background_id]["attributes"]
                        ):
                            size 24
                            color "#d7b4f5"

                        text _(BACKGROUND_DESCRIPTIONS[background_id]):
                            xsize 512
                            size 23
                            color "#e1dbe6"

        textbutton _("Begin"):
            id "background_begin"

            xalign 0.5
            xysize (320, 64)

            background Solid("#7844a3")
            hover_background Solid("#9557c6")
            insensitive_background Solid("#302a38")

            text_size 30
            text_color "#ffffff"
            text_insensitive_color "#81768b"
            text_xalign 0.5
            text_yalign 0.5

            sensitive (selected_background is not None)
            action Return(selected_background)