# Display metadata only. Saved values remain in PlayerState.
define PLAYER_SKILL_LABELS = (
    ("oral", _("Oral")),
    ("manual", _("Manual skill")),
    ("body_awareness", _("Body awareness")),
    ("anal", _("Anal")),
    ("toys", _("Toy knowledge")),
    ("dominance", _("Dominance practice")),
    ("submission", _("Submission practice")),
)

define PLAYER_PREFERENCE_LABELS = (
    ("oral", _("Oral")),
    ("anal", _("Anal")),
    ("roleplay", _("Roleplay")),
    ("group", _("Group intimacy")),
    ("bdsm", _("BDSM")),
    ("toys", _("Toys")),
)

define PLAYER_RELATIONSHIP_LABELS = {
    "long_distance": _("Long-distance relationship"),
    "single": _("Single"),
    "open": _("Open relationship"),
}


screen player_stats():
    tag menu

    default current_tab = "overview"

    use game_menu(_("Character"), scroll="viewport"):
        vbox:
            spacing 28

            if player.background_id is None:
                text _("Choose a background to view your character.")

            else:
                text _(BACKGROUNDS[player.background_id]["name"]):
                    size 42
                    color gui.accent_color

                text _(PLAYER_RELATIONSHIP_LABELS.get(
                    player.relationship_status,
                    _("Unknown relationship status"),
                ))

                hbox:
                    spacing 32

                    textbutton _("Overview"):
                        id "player_stats_tab_overview"
                        selected (current_tab == "overview")
                        action SetScreenVariable("current_tab", "overview")

                    textbutton _("Skills"):
                        id "player_stats_tab_skills"
                        selected (current_tab == "skills")
                        action SetScreenVariable("current_tab", "skills")

                    textbutton _("Preferences"):
                        id "player_stats_tab_preferences"
                        selected (current_tab == "preferences")
                        action SetScreenVariable("current_tab", "preferences")

                if current_tab == "overview":
                    text _("Attributes"):
                        size 36
                        color gui.accent_color

                    text _("Intellect (INT): [player.attributes['intellect']]"):
                        id "stat_intellect"
                    text _("Stamina (STA): [player.attributes['stamina']]")
                    text _("Charisma (CHA): [player.attributes['charisma']]")

                    text _("Development"):
                        size 36
                        color gui.accent_color

                    text _("Submission: [player.submission]")
                    text _("Dominance: [player.dominance]")
                    text _("Corruption: [player.corruption]")
                    text _("Arousal: [player.arousal] / 10")

                elif current_tab == "skills":
                    text _("Skills"):
                        size 36
                        color gui.accent_color

                    for skill_id, skill_label in PLAYER_SKILL_LABELS:
                        text _("{label}: {value}").format(
                            label=_(skill_label),
                            value=player.skills.get(skill_id, 0),
                        ):
                            id ("skill_" + skill_id)

                elif current_tab == "preferences":
                    text _("Preferences"):
                        size 36
                        color gui.accent_color

                    text _("A value of 0 means no established preference."):
                        size 24
                        color "#bcb4c7"

                    for preference_id, preference_label in PLAYER_PREFERENCE_LABELS:
                        text _("{label}: {value}").format(
                            label=_(preference_label),
                            value=player.get_preference(preference_id),
                        ):
                            id ("preference_" + preference_id)

                textbutton _("Back to game"):
                    id "player_stats_close"
                    action Return()
