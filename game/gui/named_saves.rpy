init python:

    def clean_save_title(title):
        """Keep save titles short, single-line and free of text markup."""

        title = " ".join(title.split())

        title = "".join(
            character
            for character in title
            if character not in "{}[]"
        )

        return title[:60].strip() or _("Unnamed save")


    def suggested_save_title():
        """Provide a useful title for a new manual save."""

        if player.background_id in BACKGROUNDS:
            background = _(BACKGROUNDS[player.background_id]["name"])

            return _("{background} - New beginning").format(
                background=background,
            )

        return _("New beginning")


    def named_save_action(slot, page):
        """Open naming only for normal, manual saves."""

        if main_menu or page in ("auto", "quick"):
            return FileSave(slot, page=page)

        existing_name = FileSaveName(slot, page=page)

        open_prompt = Show(
            "save_name_prompt",
            slot=slot,
            page=page,
            initial_name=existing_name or suggested_save_title(),
        )

        if FileLoadable(slot, page=page):
            return Confirm(
                _("Overwrite this save?"),
                yes=open_prompt,
            )

        return open_prompt


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
                    value ScreenVariableInputValue("draft_title")
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