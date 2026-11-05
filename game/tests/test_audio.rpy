testsuite audio_tests:

    setup:

        python:
            if persistent.audio_tests_backup is None:
                audio_backup = {}

                for mixer in ("music", "sfx", "ambience", "adult", "voice"):
                    was_muted = preferences.get_mute(mixer)

                    # Read the stored volume even when muted.
                    preferences.set_mute(mixer, False)

                    audio_backup[mixer] = {
                        "volume": preferences.get_mixer(mixer),
                        "muted": was_muted,
                    }

                    preferences.set_mute(mixer, was_muted)

                persistent.audio_tests_backup = audio_backup

    before testcase:

        if not screen "main_menu":
            if eval main_menu:
                run ShowMenu("main_menu")
            else:
                run MainMenu(confirm=False)

        pause until screen "main_menu"

        python:
            for mixer in ("music", "sfx", "ambience", "adult", "voice"):
                preferences.set_mute(mixer, False)

        # Use the same volume scale as preferences.get_mixer().
        run Function(preferences.set_mixer, "music", 0.6)
        run Function(preferences.set_mixer, "sfx", 0.6)
        run Function(preferences.set_mixer, "ambience", 0.4)
        run Function(preferences.set_mixer, "adult", 0.7)

        run ShowMenu("preferences")
        pause until screen "preferences"

        # Bring the audio controls into the visible content area.
        scroll amount 30 pos (0.8, 0.5)
        pause 0.2

    after testcase:

        if eval main_menu:
            run ShowMenu("main_menu")
        else:
            run MainMenu(confirm=False)

        pause until screen "main_menu"

    teardown:

        python:
            if persistent.audio_tests_backup is not None:

                for mixer, settings in persistent.audio_tests_backup.items():
                    preferences.set_mute(mixer, False)
                    preferences.set_mixer(mixer, settings["volume"])
                    preferences.set_mute(mixer, settings["muted"])

                persistent.audio_tests_backup = None

            renpy.save_persistent()

    testcase independent_mute_and_volume:

        assert id "audio_volume_music"
        assert id "audio_volume_sfx"
        assert id "audio_volume_ambience"
        assert id "audio_volume_adult"

        # Check the initial volume values.
        assert eval abs(preferences.get_mixer("music") - 0.6) < 0.001
        assert eval abs(preferences.get_mixer("sfx") - 0.6) < 0.001
        assert eval abs(preferences.get_mixer("ambience") - 0.4) < 0.001
        assert eval abs(preferences.get_mixer("adult") - 0.7) < 0.001

        # Muting adult sounds must leave the other mixers unmuted.
        click id "audio_mute_adult"

        assert eval preferences.get_mute("adult")
        assert eval not preferences.get_mute("music")
        assert eval not preferences.get_mute("sfx")
        assert eval not preferences.get_mute("ambience")

        # Unmuting must restore the previous volume.
        click id "audio_mute_adult"

        assert eval not preferences.get_mute("adult")
        assert eval abs(preferences.get_mixer("adult") - 0.7) < 0.001

        # Changing ambience must leave the adult volume unchanged.
        run Function(preferences.set_mixer, "ambience", 0.2)

        assert eval abs(preferences.get_mixer("ambience") - 0.2) < 0.001
        assert eval abs(preferences.get_mixer("adult") - 0.7) < 0.001

        click id "audio_mute_ambience"

        assert eval preferences.get_mute("ambience")
        assert eval not preferences.get_mute("adult")

        # Mute All must also include the custom mixers.
        click id "audio_mute_all"

        assert eval preferences.get_mute("music")
        assert eval preferences.get_mute("sfx")
        assert eval preferences.get_mute("ambience")
        assert eval preferences.get_mute("adult")

        click id "audio_mute_all"

        assert eval not preferences.get_mute("music")
        assert eval not preferences.get_mute("sfx")
        assert eval not preferences.get_mute("ambience")
        assert eval not preferences.get_mute("adult")

        # Global muting must preserve the chosen volume values.
        assert eval abs(preferences.get_mixer("music") - 0.6) < 0.001
        assert eval abs(preferences.get_mixer("sfx") - 0.6) < 0.001
        assert eval abs(preferences.get_mixer("ambience") - 0.2) < 0.001
        assert eval abs(preferences.get_mixer("adult") - 0.7) < 0.001