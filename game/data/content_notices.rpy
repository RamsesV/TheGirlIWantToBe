# Select the notice profile for this distribution.
define CONTENT_EDITION = "standard"

# Increase when revised notices require a new confirmation.
define CONTENT_NOTICE_REVISION = 1


define CONTENT_EDITION_NAMES = {
    "standard": _("Standard Edition"),
    "enhanced": _("Enhanced Edition"),
}


# Each entry contains: icon index, title, explanation.
define CONTENT_NOTICES = {

    "adult": (
        0,
        _("Adults only! 18+"),
        _("Intended exclusively for adults aged 18 or older."),
    ),

    "sex": (
        1,
        _("Sexual content"),
        _("Explicit sexual content and nudity."),
    ),

    "violence": (
        2,
        _("Violence"),
        _("Depictions of physical violence."),
    ),

    "alcohol": (
        3,
        _("Alcohol"),
        _("References to or depictions of alcohol consumption."),
    ),

    "drugs": (
        4,
        _("Drugs"),
        _("References to or depictions of recreational drug use."),
    ),

    "language": (
        5,
        _("Strong language"),
        _("Swearing and strong language."),
    ),

    "ai": (
        6,
        _("AI-generated media"),
        _("Includes AI-generated artwork and video."),
    ),

    "incest": (
        7,
        _("Incest themes"),
        _("This edition includes incest themes involving adult characters."),
    ),

    "animals": (
        8,
        _("Sexual content involving animals"),
        _("This edition includes sexual content involving animals."),
    ),
}


# Keep these lists consistent with the actual distribution content.
define CONTENT_EDITION_NOTICES = {

    "standard": (
        "adult",
        "sex",
        "violence",
        "alcohol",
        "drugs",
        "language",
        "ai",
    ),

    "enhanced": (
        "adult",
        "sex",
        "violence",
        "alcohol",
        "drugs",
        "language",
        "ai",
        "incest",
        "animals",
    ),
}


define CONTENT_BOUNDARIES = _p("""
Every character depicted in a sexual context is an adult aged 18 or older.

No sexual content involving minors or pedophilic themes.

No hate content, racism, or racist hate speech.

These boundaries apply to all editions, including optional scenes, replays, and future updates.
""")