default protagonist_name = ""
default neighbor_introduced = False
default dog_sitting_lead_known = False

define neighbor_name = "Claire Bennett"
define neighbor_dog_name = "Milo"

define arrival_you = Character(
    "[protagonist_name or _('You')]"
)

define arrival_neighbor = Character(
    "[neighbor_name if neighbor_introduced else _('Neighbor')]"
)


init python:

    def clean_protagonist_name(value):

        # Prevent names from introducing text tags or interpolation.
        for character in "{}[]":
            value = value.replace(character, "")

        # Normalize whitespace and limit the displayed name.
        return " ".join(value.split())[:24].strip()