define FIRST_ARRIVAL_DECISION = {
    "prompt": _("The woman waits beside the open door. How do you respond?"),

    "options": (
        {
            "id": "accept",
            "text": _("Accept her help and introduce yourself."),
            "hint": _("A friendly first introduction."),
            "path": _("A helping hand"),
            "effects": {},
        },
        {
            "id": "negotiate",
            "text": _("Offer her a deal: she holds the door, you handle the boxes."),
            "hint": _("Use your social confidence to make an arrangement."),
            "path": _("A small agreement"),
            "requires": (
                ("attributes.charisma", 4, None),
            ),
            "effects": {},
        },
        {
            "id": "notice",
            "text": _("Point out the second entrance on the building plan."),
            "hint": _("Use the information you read before moving."),
            "path": _("Another way in"),
            "requires": (
                ("attributes.intellect", 4, None),
            ),
            "effects": {},
        },
        {
            "id": "alone",
            "text": _("Thank her, but finish moving in by yourself."),
            "hint": _("Keep this first evening to yourself."),
            "path": _("Your own space"),
            "effects": {},
        },
    ),
}