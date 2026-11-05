label start:

    scene black

    "Every new beginning starts somewhere."
    "Choose your background."

    call choose_background

    call player_state_test

    "End of the first prototype."

    return


label choose_background:

    menu:
        "Which background fits you?"

        "Bookworm":
            $ chosen_background = "bookworm"

        "Girl Next Door":
            $ chosen_background = "girl_next_door"

        "Social Butterfly":
            $ chosen_background = "social_butterfly"

    # Always create fresh state before applying a background.
    $ player = PlayerState()
    $ player.apply_background(chosen_background, BACKGROUNDS[chosen_background])

    return


label player_state_test:

    $ background_name = BACKGROUNDS[player.background_id]["name"]

    "Background: [background_name]"
    "INT: [player.attributes['intellect']] | STA: [player.attributes['stamina']] | CHA: [player.attributes['charisma']]"
    "Submission: [player.submission] | Dominance: [player.dominance]"
    "Corruption: [player.corruption] | Arousal: [player.arousal]"

    "Manual skill: [player.skills['manual']]"
    "Body awareness: [player.skills['body_awareness']]"
    "Submission practice: [player.skills['submission']]"
    "Dominance practice: [player.skills['dominance']]"

    "Relationship status: [player.relationship_status]"

    menu:
        "Test the arousal limit?"

        "Add 20 points":
            $ player.change_arousal(20)

        "Subtract 20 points":
            $ player.change_arousal(-20)

        "Leave unchanged":
            pass

    "Arousal: [player.arousal]"

    return