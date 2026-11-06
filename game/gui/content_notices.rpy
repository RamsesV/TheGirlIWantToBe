screen content_notice_bar():

    hbox:

        xalign 1.0
        yalign 1.0

        xoffset -48
        yoffset -35

        spacing 8

        for notice_id in content_notice_ids():

            button:
                id ("content_icon_" + notice_id)

                style "content_notice_icon_button"

                action ShowMenu("content_information")

                tooltip _(CONTENT_NOTICES[notice_id][1])
                alt _(CONTENT_NOTICES[notice_id][1])

                add content_notice_icon(notice_id):
                    xalign 0.5
                    yalign 0.5

    $ content_tooltip = GetTooltip()

    if content_tooltip:

        frame:

            xalign 1.0
            yalign 1.0

            xoffset -48
            yoffset -105

            xmaximum 700

            padding (14, 10)
            background Solid("#211b29ee")

            text content_tooltip:
                size 22
                color "#f5e7d4"
                text_align 1.0

screen content_notice_body():

    vbox:
        xsize 1140
        spacing 22

        text _(CONTENT_EDITION_NAMES[CONTENT_EDITION]):
            style "content_notice_heading"

        for notice_id in content_notice_ids():

            hbox:
                spacing 20

                add content_notice_icon(notice_id)

                vbox:
                    xsize 1050
                    spacing 4

                    text _(CONTENT_NOTICES[notice_id][1]):
                        size 27
                        color "#f5e7d4"

                    text _(CONTENT_NOTICES[notice_id][2]):
                        style "content_notice_body_text"

        null height 8

        text _("Boundaries shared by both editions"):
            style "content_notice_heading"

        text "[CONTENT_BOUNDARIES!t]":
            id "content_boundaries"
            style "content_notice_body_text"

        text _("These are developer-provided content notices, not an official age rating."):
            size 21
            color "#c9bab9"


screen content_information():

    tag menu

    use game_menu(_("Content Information"), scroll="viewport"):

        use content_notice_body()


screen content_age_gate():

    modal True
    zorder 200

    add gui.main_menu_background
    add Solid("#100d17eb")

    frame:
        xalign 0.5
        yalign 0.5

        xsize 1320
        ysize 970

        padding (40, 30)
        background Solid("#211b29f5")

        vbox:
            spacing 18

            text _("Adults only — 18+"):
                size 42
                color "#f5e7d4"

            text _("Please review the content information before continuing."):
                style "content_notice_body_text"

            viewport:
                id "content_gate_viewport"

                ysize 660

                mousewheel True
                draggable True
                pagekeys True

                scrollbars "vertical"
                side_yfill True

                use content_notice_body()

            hbox:
                spacing 35

                textbutton _("I am 18 or older — Continue"):
                    id "content_age_confirm"
                    style "content_notice_action_button"
                    action Function(accept_content_notice)

                textbutton _("Exit"):
                    id "content_age_exit"
                    style "content_notice_action_button"
                    action Quit(confirm=False)

    key "game_menu" action NullAction()


style content_notice_icon_button is button:

    xysize (56, 56)
    padding (4, 4)

    background Solid("#1d1726b0")
    hover_background Solid("#9d594ed0")


style content_notice_heading is gui_text:

    size 32
    color "#ef927e"


style content_notice_body_text is gui_text:

    size 24
    color "#dfd5cf"


style content_notice_action_button is button:

    padding (14, 10)

    background Solid("#382c40")
    hover_background Solid("#714a50")


style content_notice_action_button_text is gui_text:

    size 28

    color "#f5e7d4"
    hover_color "#ffffff"