default story_debug_visible = False


init python:

    def story_debug_rows():

        screen_names = (
            "say",
            "choice",
            "decision_choice",
            "background_select",
            "preferences",
            "save",
            "load",
            "replay_gallery",
        )

        active = [
            name
            for name in screen_names
            if renpy.get_screen(name)
        ]

        tags = sorted(
            renpy.get_showing_tags(layer="master")
        )

        background = (
            renpy.get_attributes("bg", layer="master")
            or ()
        )

        filename, line = renpy.get_filename_line()

        return (
            ("Scene", story_scene_id or "-"),
            ("Screens", ", ".join(active) or "-"),
            (
                "BG",
                "bg " + " ".join(background)
                if background
                else "-",
            ),
            ("Image tags", ", ".join(tags) or "-"),
            ("Background", str(player.background_id)),
            (
                "Outfits",
                protagonist_outfit
                + " / neighbor: "
                + npc_outfits["neighbor"],
            ),
            (
                "Walkthrough",
                persistent.walkthrough_mode
                + " / setup: "
                + str(persistent.walkthrough_setup_done),
            ),
            ("Choice", str(first_arrival_approach)),
            (
                "Source",
                "{}:{}".format(filename, line),
            ),
        )


    if config.developer:
        config.overlay_screens.append("story_debug")


screen story_debug():

    zorder 2000

    if config.developer:

        key "K_F3" action ToggleVariable(
            "story_debug_visible"
        )

        if story_debug_visible:

            frame:
                xpos 20
                ypos 20
                xsize 650

                padding (14, 10)
                background Solid("#18121ee6")

                vbox:
                    spacing 3

                    text "STORY DEBUG · F3":
                        size 18
                        color "#ef927e"

                    for caption, value in story_debug_rows():

                        text (caption + ": " + value):
                            size 18
                            color "#f5e7d4"
                            substitute False