# Native dialogue styles, also used by the decision context.
style window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 300
    padding (0, 0)
    background None


style say_label:
    font "fonts/CormorantGaramond-Regular.otf"
    size 46
    color "#ef927e"

    xpos 150
    ypos 22
    xanchor 0.0
    yanchor 0.0

    outlines [(1, "#1b152180", 0, 1)]


style say_dialogue:
    font gui.text_font
    size 30
    color "#f5e7d4"

    xpos 150
    ypos 90
    xsize 1580

    line_spacing 6
    adjust_spacing False

    outlines [(1, "#1b152180", 0, 1)]


style story_quick_menu is hbox:
    xalign 1.0
    xoffset -70

    yalign 1.0
    yoffset -16

    spacing 26


style story_quick_button is button:
    padding (0, 6)
    background None
    hover_background None
    selected_background None


style story_quick_button_text is default:
    font gui.interface_text_font
    size 22

    color "#c9bab9"
    hover_color "#ef927e"
    selected_color "#ef927e"
    insensitive_color "#827582"


style story_choice_button is button:
    xsize 825
    yminimum 58
    padding (26, 10)

    background Solid("#211b29df")
    hover_background Solid("#44303bf0")
    insensitive_background Solid("#211b29c0")


style story_choice_text is default:
    font gui.interface_text_font
    size 27

    color "#f5e7d4"
    hover_color "#ef927e"
    insensitive_color "#a395a4"

    xsize 773
    line_spacing 3


style story_choice_detail is default:
    font gui.interface_text_font
    size 21
    color "#c9bab9"

    xsize 773
    line_spacing 3


style story_choice_caption is story_choice_text:
    color "#ef927e"


style story_walkthrough_button is story_quick_button

style story_walkthrough_button_text is story_quick_button_text:
    size 20


screen story_dialogue_background():

    add "gui/dialogue_gradient.svg":
        xysize (1920, 300)
        yalign 1.0


screen decision_context(who, what):

    use story_dialogue_background

    fixed:
        xysize (1920, 300)
        yalign 1.0

        if who is not None:

            text who:
                style "say_label"
                substitute False

            add Solid("#ef927e"):
                xpos 150
                ypos 76
                xysize (65, 2)

        text what:
            id "decision_context_text"
            style "say_dialogue"

            substitute False
            slow_cps False

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