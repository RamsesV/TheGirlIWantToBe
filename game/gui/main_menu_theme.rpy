init python:

    def main_menu_title_text():

        title = _(config.name)

        return title.replace(
            " I Want to Be",
            "\nI {font=fonts/CormorantGaramond-Italic.otf}"
            "{color=#ef927e}Want{/color}{/font} to Be",
            1,
        )


style main_menu_vbox:

    xpos 90
    ypos 75

    xanchor 0.0
    yanchor 0.0

    xoffset 0
    yoffset 0

    xsize 740
    spacing 12


style main_menu_title:

    font "fonts/CormorantGaramond-Regular.otf"

    size 120
    bold False
    italic False

    color "#f5e7d4"

    xsize 740
    text_align 0.0

    layout "greedy"
    line_spacing -12

    outlines [
        (0, "#17121c80", 0, 2),
    ]


style main_menu_version:

    font gui.interface_text_font

    xpos 90
    yalign 1.0

    xanchor 0.0
    xoffset 0
    yoffset -35

    size 22
    color "#c9bab9"

    outlines [
        (0, "#17121c80", 0, 1),
    ]


style title_navigation_vbox is vbox
style title_navigation_button is navigation_button
style title_navigation_button_text is navigation_button_text


style title_navigation_button:

    size_group "title_navigation"

    padding (0, 8)

    background None
    hover_background None
    selected_background None


style title_navigation_button_text:

    font gui.interface_text_font

    size 32

    xalign 0.0
    text_align 0.0

    idle_color "#e3d4c7"
    hover_color "#ef927e"
    selected_color "#ef927e"
    insensitive_color "#8e818b"

    outlines [
        (0, "#17121c80", 0, 1),
    ]