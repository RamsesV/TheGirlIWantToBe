screen decision_choice(
    decision,
    context_who=None,
    context_text="",
):

    modal True
    roll_forward False

    default show_walkthrough_setup = (
        not persistent.walkthrough_setup_done
    )

    use decision_context(context_who, context_text)

    if show_walkthrough_setup:

        hbox:
            xpos 1125
            ypos 250
            spacing 20

            text _("Walkthrough:"):
                style "story_choice_detail"
                xsize 145
                yalign 0.5

            for mode, caption in (
                ("off", _("Off")),
                ("hints", _("Hints")),
                ("full", _("Full")),
            ):

                textbutton _(caption):
                    id ("walkthrough_" + mode)
                    style "story_walkthrough_button"

                    selected (
                        persistent.walkthrough_mode == mode
                    )

                    action SetField(
                        persistent,
                        "walkthrough_mode",
                        mode,
                    )

    viewport:
        id "decision_options"

        xpos 1095
        ypos 300
        xysize (825, 460)

        mousewheel True
        draggable True

        vbox:
            spacing 12

            for option in decision["options"]:

                if decision_visible(option, player):

                    button:
                        id ("decision_option_" + option["id"])
                        style "story_choice_button"

                        sensitive decision_available(
                            option,
                            player,
                        )

                        action Return(option["id"])

                        vbox:
                            spacing 6

                            text _(option["text"]):
                                style "story_choice_text"

                            if persistent.walkthrough_mode == "hints":

                                text _(option["hint"]):
                                    id ("decision_hint_" + option["id"])
                                    style "story_choice_detail"

                            elif persistent.walkthrough_mode == "full":

                                text decision_details(option, player):
                                    id ("decision_details_" + option["id"])
                                    style "story_choice_detail"