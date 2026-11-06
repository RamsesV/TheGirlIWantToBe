# Character identity and appearance.
# Preserve saved variable names when reorganizing this module.

default protagonist_name = ""
default protagonist_outfit = "girl_next_door"

default neighbor_introduced = False

default npc_outfits = {
    "neighbor": "casual",
}


define PROTAGONIST_NAMES = (
    "Emma",
    "Olivia",
    "Chloe",
)

define PROTAGONIST_NAME_MAX_LENGTH = 24

define neighbor_name = "Claire Morgan"
define neighbor_dog_name = "Milo"


define arrival_you = Character(
    "[protagonist_name or _('You')]"
)

define arrival_neighbor = Character(
    "[neighbor_name if neighbor_introduced else _('Neighbor')]"
)


init python:

    def clean_protagonist_name(value):
        """Keep player names short and free of text markup."""

        for character in "{}[]":
            value = value.replace(character, "")

        return (
            " ".join(value.split())
            [:PROTAGONIST_NAME_MAX_LENGTH]
            .strip()
        )


    def neighbor_introduction_text():
        """Use the same introduction in dialogue and the name screen."""

        return _("I'm {name}, by the way. And you are?").format(
            name=neighbor_name,
        )


# Outfit selection is dynamic; pose and expression remain explicit.
image protagonist standing neutral = "images/characters/protagonist/[protagonist_outfit]/standing_neutral.png"

image neighbor standing neutral = "images/characters/neighbor/[npc_outfits['neighbor']]/standing_neutral.png"


# Matching sprites use a 1024 x 1536 canvas.
# Set facing explicitly so moving a character resets any previous flip.
transform protagonist_left:
    xalign 0.22
    yalign 1.0

    zoom 0.70
    xzoom -1.0


transform protagonist_center:
    xalign 0.5
    yalign 1.0

    zoom 0.70
    xzoom 1.0


transform protagonist_right:
    xalign 0.78
    yalign 1.0

    zoom 0.70
    xzoom 1.0


transform protagonist_apartment_entry:
    xalign 0.93
    yalign 1.0

    zoom 0.70
    xzoom 1.0


transform character_left:
    xalign 0.22
    yalign 1.0

    zoom 0.70
    xzoom 1.0


transform character_center:
    xalign 0.5
    yalign 1.0

    zoom 0.70
    xzoom 1.0


transform character_right:
    xalign 0.78
    yalign 1.0

    zoom 0.70
    xzoom -1.0