screen decision_preferences():

    vbox:
        spacing 16

        hbox:
            spacing 60

            vbox:
                style_prefix "radio"
                xsize 480

                label _("Walkthrough")

                textbutton _("Off"):
                    id "pref_walkthrough_off"
                    action SetField(
                        persistent, "walkthrough_mode", "off"
                    )

                textbutton _("Hints"):
                    id "pref_walkthrough_hints"
                    action SetField(
                        persistent, "walkthrough_mode", "hints"
                    )

                textbutton _("Full"):
                    id "pref_walkthrough_full"
                    action SetField(
                        persistent, "walkthrough_mode", "full"
                    )

            vbox:
                style_prefix "radio"
                xsize 600

                label _("Unavailable choices")

                textbutton _("Hide"):
                    id "pref_unavailable_hide"
                    action SetField(
                        persistent,
                        "show_unavailable_choices",
                        False,
                    )

                textbutton _("Show"):
                    id "pref_unavailable_show"
                    action SetField(
                        persistent,
                        "show_unavailable_choices",
                        True,
                    )

        text _("Full walkthrough always shows unavailable choices."):
            size 22
            color "#bcb4c7"

        null height 20