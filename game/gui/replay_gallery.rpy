screen replay_gallery():

    tag menu

    use game_menu(_("Replay Gallery"), scroll="viewport"):

        vbox:
            spacing 28

            hbox:
                spacing 50

                textbutton _("Unlock all replays"):
                    id "gallery_unlock_all"

                    selected persistent.gallery_unlock_all
                    action Function(toggle_gallery_unlock_all)

                textbutton _("Reset gallery"):
                    id "gallery_reset"

                    action Confirm(
                        _(
                            "Reset all earned replay unlocks? "
                            "'Unlock all replays' will also be switched off."
                        ),
                        yes=Function(reset_gallery),
                        confirm_selected=True,
                    )

            if persistent.gallery_unlock_all:
                text _("All installed replays are available."):
                    size 24
                    color "#d7b4f5"

            else:
                text _("Replays unlock as you discover them in the story."):
                    size 24
                    color "#bcb4c7"

            for entry in gallery_entries():

                button:
                    id ("gallery_replay_" + entry["id"])

                    xsize 1200
                    padding (24, 24)

                    background Solid("#30263c")
                    hover_background Solid("#55356e")
                    insensitive_background Solid("#211d27")

                    sensitive gallery_available(entry)
                    action gallery_replay_action(entry)

                    vbox:
                        spacing 12

                        text _(entry["title"]):
                            size 34

                            color (
                                "#ffffff"
                                if gallery_available(entry)
                                else "#81768b"
                            )

                        text _(entry["description"]):
                            size 24
                            color "#bcb4c7"

                        if persistent.gallery_unlocks.get(
                            entry["id"], False
                        ):
                            text _("Unlocked by playing"):
                                size 22
                                color "#b9d7b1"

                        elif persistent.gallery_unlock_all:
                            text _("Available through Unlock all"):
                                size 22
                                color "#d7b4f5"

                        else:
                            text _("Locked"):
                                size 22
                                color "#81768b"