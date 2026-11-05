label story_preview:

    if not config.developer:
        return

    scene black

    call choose_background
    call first_arrival

    "End of the arrival preview."

    $ renpy.full_restart()