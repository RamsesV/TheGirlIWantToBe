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

            background = _(
                BACKGROUNDS[player.background_id]["name"]
            )

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
            initial_name=(
                existing_name or suggested_save_title()
            ),
        )

        if FileLoadable(slot, page=page):

            return Confirm(
                _("Overwrite this save?"),
                yes=open_prompt,
            )

        return open_prompt