screen audio_mixer_controls(title, mixer):

    vbox:
        style_prefix "slider"

        xsize 550
        spacing 12

        label title

        bar:
            id ("audio_volume_" + mixer)
            value MixerValue(mixer)
            xsize 525

        textbutton _("Mute"):
            id ("audio_mute_" + mixer)
            style "mute_all_button"
            action ToggleMute(mixer)


screen audio_preferences():

    vbox:
        spacing 30

        hbox:
            spacing 60
            box_wrap True

            use audio_mixer_controls(_("Music Volume"), "music")
            use audio_mixer_controls(_("Ambience Volume"), "ambience")

        hbox:
            spacing 60
            box_wrap True

            use audio_mixer_controls(_("Sound Effects Volume"), "sfx")
            use audio_mixer_controls(_("Adult Sounds Volume"), "adult")

        if config.has_voice:
            use audio_mixer_controls(_("Voice Volume"), "voice")

        textbutton _("Mute All"):
            id "audio_mute_all"
            style "mute_all_button"
            action Preference("all mute", "toggle")