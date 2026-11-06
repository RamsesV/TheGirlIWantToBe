# Current story location for development tools.
default story_scene_id = None

label start:

    scene black

    "Every new beginning starts somewhere."

    call intro_setting

    call choose_background

    call memory_arrival

    call first_arrival

    call player_state_test

    call decision_demo

    "End of the first prototype."

    return


label choose_background:

    # Hide the dialogue quick menu during background selection.
    $ quick_menu = False

    call screen background_select

    $ chosen_background = _return
    $ quick_menu = True

    # Apply the confirmed selection to fresh player state.
    $ player = PlayerState()
    $ player.apply_background(
        chosen_background,
        BACKGROUNDS[chosen_background],
    )

    $ protagonist_outfit = chosen_background

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