init python:

    def make_audio_check_tone(frequency, filename):
        import io
        import math
        import struct
        import wave

        sample_rate = 22050
        duration = 2.0
        sample_count = int(sample_rate * duration)
        frames = bytearray()

        for index in range(sample_count):
            time = index / sample_rate

            # Short fades prevent clicks at the loop boundary.
            envelope = min(
                1.0,
                time / 0.03,
                (duration - time) / 0.03,
            )

            sample = int(
                32767
                * 0.15
                * envelope
                * math.sin(2.0 * math.pi * frequency * time)
            )

            frames.extend(struct.pack("<h", sample))

        buffer = io.BytesIO()

        with wave.open(buffer, "wb") as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(sample_rate)
            wav.writeframes(frames)

        return AudioData(buffer.getvalue(), filename)


define audio.check_music = make_audio_check_tone(
    220, "check_music.wav"
)

define audio.check_ambience = make_audio_check_tone(
    330, "check_ambience.wav"
)

define audio.check_sound = make_audio_check_tone(
    440, "check_sound.wav"
)

define audio.check_adult = make_audio_check_tone(
    660, "check_adult.wav"
)


screen audio_check_panel():

    modal True

    add Solid("#15151f")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 25

        text _("Audio Check"):
            size 42

        text _("Start individual tones or play all four together."):
            size 24

        hbox:
            spacing 25

            textbutton _("Music"):
                selected renpy.music.is_playing(channel="music")

                action Play(
                    "music",
                    audio.check_music,
                    loop=True,
                    fadein=0.5,
                )

            textbutton _("Ambience"):
                selected renpy.music.is_playing(channel="ambience")

                action Play(
                    "ambience",
                    audio.check_ambience,
                    loop=True,
                    fadein=0.5,
                )

            textbutton _("Sound Effects"):
                selected renpy.music.is_playing(channel="sound")

                action Play(
                    "sound",
                    audio.check_sound,
                    loop=True,
                    fadein=0.5,
                )

            textbutton _("Adult Sounds"):
                selected renpy.music.is_playing(channel="adult")

                action Play(
                    "adult",
                    audio.check_adult,
                    loop=True,
                    fadein=0.5,
                )

        hbox:
            spacing 25

            textbutton _("Play All"):

                selected (
                    renpy.music.is_playing(channel="music")
                    and renpy.music.is_playing(channel="ambience")
                    and renpy.music.is_playing(channel="sound")
                    and renpy.music.is_playing(channel="adult")
                )

                action [
                    Play("music", audio.check_music, loop=True),
                    Play("ambience", audio.check_ambience, loop=True),
                    Play("sound", audio.check_sound, loop=True),
                    Play("adult", audio.check_adult, loop=True),
                ]

            textbutton _("Stop All"):
                action [
                    Stop("music", fadeout=0.5),
                    Stop("ambience", fadeout=0.5),
                    Stop("sound", fadeout=0.5),
                    Stop("adult", fadeout=0.5),
                ]

            textbutton _("Test Replay"):
                action Replay(
                    "audio_check_replay",
                    scope={"quick_menu": False},
                    locked=False,
                )

        use audio_preferences()

        textbutton _("End Test"):
            action Return()


label audio_check:

    if not config.developer:
        return

    scene black

    stop music
    stop ambience
    stop sound
    stop adult

    call screen audio_check_panel

    stop music
    stop ambience
    stop sound
    stop adult

    $ renpy.full_restart()


label audio_check_replay:

    scene black

    stop music
    stop ambience
    stop sound
    stop adult

    python:
        renpy.music.play(
            audio.check_music,
            channel="music",
            loop=True,
            fadein=1.0,
        )

        renpy.music.play(
            audio.check_ambience,
            channel="ambience",
            loop=True,
            fadein=1.0,
        )

        renpy.music.play(
            audio.check_sound,
            channel="sound",
            loop=True,
        )

        renpy.music.play(
            audio.check_adult,
            channel="adult",
            loop=True,
        )

    "Audio replay test. All four channels are playing."
    "Open Preferences to check the volume and mute controls."

    stop music fadeout 1.0
    stop ambience fadeout 1.0
    stop sound fadeout 1.0
    stop adult fadeout 1.0

    "The test tones should now have faded out."

    $ renpy.end_replay()

    return