default first_arrival_approach = None

image bg arrival_hallway = "images/backgrounds/arrival_hallway.png"
image bg arrival_hallway_neighbor_open = Transform(
    "images/backgrounds/arrival_hallway_neighbor_open.png",
    xysize=(1920, 1080)
)

image arrival_boxes = "images/props/arrival_moving_boxes.png"

image neighbor_dog standing alert = (
    "images/characters/neighbor_dog/standing_alert.png"
)

image arrival_door_foreground = Crop(
    (1710, 0, 210, 1080),
    "images/backgrounds/arrival_hallway.png"
)

transform arrival_boxes_position:
    xysize (440, 440)
    anchor (0.5, 1.0)
    pos (850, 970)


transform arrival_dog_doorway:
    xysize (480, 480)
    anchor (0.5, 1.0)
    pos (1770, 950)

label first_arrival:

    $ story_scene_id = "first_arrival / hallway"

    scene bg arrival_hallway
    show arrival_boxes at arrival_boxes_position zorder 5
    show protagonist standing neutral at protagonist_left zorder 20
    with Fade(0.15, 0.0, 0.15)

    "The address matches the email. The key matches the lock."
    "That should be enough to make this place feel like yours."
    "It isn't. Not yet."
    "Two bags and a small stack of boxes wait beside you."
    "Your arms still ache from carrying everything up the stairs."

    if player.background_id == "bookworm":
        "You checked the route twice before leaving. Somehow, neither version mentioned the entrance steps."
        "Your phone vibrates."
        "'Made it? Call me when you're settled. Miss you already.'"
        "You smile at the message. For now, the distance is just a number on a map."

    elif player.background_id == "social_butterfly":
        "You rest a hand on the largest box and glance at your phone."
        "'Made it? Go meet your neighbors. I expect stories.'"
        "You send back a picture of the front door."
        "The conversation about opening the relationship had felt straightforward. Standing here alone, you realize the practical part starts now."

    else:
        "Your thumb hovers over a familiar conversation."
        "For years, arriving somewhere meant telling him you'd arrived."
        "You put the phone away. Tonight, you'll unpack first."

    "A door opens across the landing."

    show neighbor standing neutral at character_right zorder 20
    with Dissolve(0.25)

    show neighbor standing neutral at character_right
    with Dissolve(0.25)

    arrival_neighbor "Please tell me you're moving in."
    arrival_neighbor "Otherwise, that's a very ambitious delivery."

    "You glance down at the box. Books. Kitchen things. One shoe."
    "A reasonably accurate summary of your packing system."

    arrival_neighbor "I live across the hall from the empty apartment."
    arrival_neighbor "Well. Formerly empty, I hope."
    arrival_neighbor "[neighbor_introduction_text()]"

    if not protagonist_name:

        window hide
        call screen protagonist_name_choice

        $ protagonist_name = clean_protagonist_name(_return)

    arrival_you "I'm [protagonist_name]. Nice to meet you."

    $ neighbor_introduced = True

    arrival_neighbor "Nice to meet you too, [protagonist_name]."

    "Something clicks against the floor inside her apartment."
    "A German Shepherd peers through the open doorway, ears pricked."

    show neighbor_dog standing alert at arrival_dog_doorway zorder 10
    show arrival_door_foreground zorder 15:
        pos (1710, 0)
    with Dissolve(0.25)

    "He gives a single, hopeful bark."

    arrival_neighbor "[neighbor_dog_name]. Stay."
    arrival_neighbor "That's my dog. He thinks every open door means a walk."

    "He stays in the doorway, watching you with considerable interest."

    arrival_neighbor "Now, about that box."
    arrival_neighbor "Want a hand?"

    window hide

    call choose_decision({
        "prompt": _("Want a hand?"),

        "options": (
            {
                "id": "accept",
                "text": _("Accept her help."),
                "hint": _("Accept a helping hand from your new neighbor."),
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
    })

    $ first_arrival_approach = _return

    if first_arrival_approach == "accept":
        arrival_you "Actually... an extra pair of hands would be great."
        "You admit that the box is heavier than it looks."
        arrival_neighbor "They always are."
        "She picks up one of your bags."
        arrival_neighbor "Come on. Before that box makes the decision for you."
        "By the time everything is inside, you know which landing light flickers and where parcels usually end up."
        "The building already feels a little less unfamiliar."

    elif first_arrival_approach == "negotiate":
        arrival_you "You handle the doors, I'll handle the boxes. Deal?"
        arrival_neighbor "Management material. I can tell."
        "She holds your apartment door open."
        arrival_neighbor "Fine. But if you drop that box, I'm promoting myself."
        "You get your belongings inside with most of your dignity intact."
        arrival_neighbor "We work well together. Dangerous thing to discover this early."

    elif first_arrival_approach == "notice":
        arrival_you "Is the side entrance still in use? The building plan showed another way in."
        arrival_neighbor "You read the building plan?"
        arrival_you "It seemed useful before moving."
        arrival_neighbor "It is useful. There's a ramp around the corner."
        arrival_neighbor "I've lived here two years. You're already better prepared."
        "The second entrance makes the remaining trips considerably easier."

    else:
        arrival_you "Thanks, but I think I've got this."
        arrival_neighbor "Of course. Across the hall if you need anything."
        arrival_neighbor "Advice is free. Coffee depends on how much I've had."
        "You smile, thank her again, and carry your things inside."

    hide arrival_boxes
    with Dissolve(0.3)

    "At last, the landing is clear."

    $ story_scene_id = "first_arrival / apartment"

    scene bg intro_apartment
    show protagonist standing neutral at protagonist_far_right
    with Fade(0.15, 0.0, 0.15)

    "Eventually, the last bag lands inside your apartment."
    "You close the door and listen."
    "A tap runs somewhere nearby. Footsteps cross the ceiling."
    "From across the hall comes the faint sound of a cupboard closing."
    "You put your key on the kitchen counter."

    arrival_you "Tomorrow, groceries. Tonight... the other shoe."

    $ unlock_gallery_replay("first_arrival")
    $ renpy.end_replay()

    window hide
    scene black
    with Dissolve(0.25)

    $ story_scene_id = None

    return
