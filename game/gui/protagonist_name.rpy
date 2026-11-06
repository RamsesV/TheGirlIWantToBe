screen protagonist_name_choice():

    modal True
    roll_forward False

    default draft = "Emma"

    use decision_context(
        _("Neighbor"),
        _("I'm Claire Bennett, by the way. And you are?"),
    )

    frame:
        xpos 1095
        ypos 300
        xsize 825

        padding (30, 24)
        background Solid("#211b29ef")

        vbox:
            spacing 20
            xsize 765

            text _("What's your name?"):
                font "fonts/CormorantGaramond-Regular.otf"
                size 42
                color "#f5e7d4"

            hbox:
                spacing 30

                for suggested in ("Emma", "Olivia", "Chloe"):

                    textbutton suggested:
                        id ("name_preset_" + suggested.lower())
                        style "story_walkthrough_button"
                        text_size 28

                        selected (draft == suggested)

                        action SetScreenVariable(
                            "draft",
                            suggested,
                        )

            text _("Or enter your own:"):
                size 23
                color "#c9bab9"

            frame:
                xfill True
                padding (16, 12)
                background Solid("#382b40")

                input:
                    id "protagonist_name_input"

                    value ScreenVariableInputValue("draft")

                    length 24
                    pixel_width 700
                    exclude "{}[]\n\r"
                    copypaste True

                    size 30
                    color "#f5e7d4"

                    action If(
                        bool(clean_protagonist_name(draft)),
                        Return(clean_protagonist_name(draft)),
                        NullAction(),
                    )

            textbutton _("Introduce yourself"):
                id "protagonist_name_confirm"
                style "story_walkthrough_button"
                text_size 26

                sensitive bool(clean_protagonist_name(draft))

                action Return(
                    clean_protagonist_name(draft)
                )