# Input screens contain presentation and interaction.
# Validation and save rules live in systems/.

screen protagonist_name_choice():

    modal True
    roll_forward False

    default draft = PROTAGONIST_NAMES[0]

    use decision_context(
        _("Neighbor"),
        neighbor_introduction_text(),
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

                for suggested in PROTAGONIST_NAMES:

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

                    length PROTAGONIST_NAME_MAX_LENGTH
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


screen save_name_prompt(slot, page, initial_name):

    modal True
    zorder 200

    default draft_title = initial_name

    add Solid("#000000b0")

    frame:
        align (0.5, 0.5)
        xsize 950
        padding (40, 35)
        background Solid("#25202f")

        vbox:
            spacing 24

            text _("Name your save"):
                size 40
                color "#ffffff"

            text _("Enter a name or keep the suggested title."):
                size 24
                color "#c4bccc"

            frame:
                xfill True
                padding (18, 14)
                background Solid("#14111c")

                input:
                    id "save_title_input"

                    value ScreenVariableInputValue(
                        "draft_title"
                    )

                    length 60
                    exclude "{}[]\n\r"

                    size 28
                    color "#ffffff"
                    xsize 820

            hbox:
                spacing 40

                textbutton _("Save"):
                    id "save_title_confirm"

                    action [
                        SetVariable(
                            "save_name",
                            clean_save_title(draft_title),
                        ),
                        FileSave(
                            slot,
                            page=page,
                            confirm=False,
                            action=Hide("save_name_prompt"),
                        ),
                    ]

                textbutton _("Cancel"):
                    id "save_title_cancel"
                    action Hide("save_name_prompt")

    key "game_menu" action Hide("save_name_prompt")