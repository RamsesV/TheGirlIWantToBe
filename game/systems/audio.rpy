# Audio channels and initial mixer volumes.
# Player preferences are managed and saved by Ren'Py.

init python:

    renpy.music.register_channel(
        "ambience",
        mixer="ambience",
        loop=True,
        stop_on_mute=False,
    )

    renpy.music.register_channel(
        "adult",
        mixer="adult",
        loop=False,
        stop_on_mute=False,
    )


default preferences.volume.ambience = 0.7
default preferences.volume.adult = 0.7