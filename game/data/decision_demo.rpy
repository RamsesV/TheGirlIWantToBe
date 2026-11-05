define ARRIVAL_DECISION = {
    "prompt": _(
        "You have an afternoon to settle in. What do you do?"
    ),

    "options": (
        {
            "id": "guided",
            "text": _("Ask someone to show you around."),
            "hint": _("Let someone else take the lead."),
            "path": _("Guided introduction"),
            "effects": {
                "submission": 1,
            },
        },

        {
            "id": "lead",
            "text": _(
                "Take charge and organize a tour for the newcomers."
            ),
            "hint": _("Assert yourself and lead the group."),
            "path": _("Group organizer"),
            "requires": (
                ("attributes.charisma", 4, None),
            ),
            "effects": {
                "dominance": 2,
            },
        },

        {
            "id": "study",
            "text": _(
                "Study the campus guide and plan your first week."
            ),
            "hint": _("Use your knowledge and focus."),
            "path": _("Campus preparation"),
            "requires": (
                ("attributes.intellect", 4, None),
                ("arousal", None, 6),
            ),
            "effects": {
                "attributes.intellect": 1,
            },
        },

        {
            "id": "independent",
            "text": _("Take a quiet walk on your own."),
            "hint": _("Explore at your own pace."),
            "path": _("Independent exploration"),
            "effects": {},
        },
    ),
}