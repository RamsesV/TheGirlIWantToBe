default first_arrival_approach = None


image bg arrival_hallway = "images/backgrounds/arrival_hallway.png"


label first_arrival:

    $ story_scene_id = "first_arrival / hallway"

    scene bg arrival_hallway
    show protagonist standing neutral at protagonist_left
    with Fade(0.15, 0.0, 0.15)

    "The address matches the email. The key matches the lock."
    "That should be enough to make this place feel like yours."
    "It isn't. Not yet."
    "Two bags wait at your feet. The largest box is slowly slipping out of your arms."

    if player.background_id == "bookworm":
        "You checked the route twice before leaving. Somehow, neither version mentioned the entrance steps."
        "Your phone vibrates."
        "'Made it? Call me when you're settled. Miss you already.'"
        "You smile at the message. For now, the distance is just a number on a map."

    elif player.background_id == "social_butterfly":
        "You shift the box against your hip and glance at your phone."
        "'Made it? Go meet your neighbors. I expect stories.'"
        "You send back a picture of the front door."
        "The conversation about opening the relationship had felt straightforward. Standing here alone, you realize the practical part starts now."

    else:
        "Your thumb hovers over a familiar conversation."
        "For years, arriving somewhere meant telling him you'd arrived."
        "You put the phone away. Tonight, you'll unpack first."

    "A door opens across the landing."

    show neighbor standing neutral at character_right
    with Dissolve(0.25)

    arrival_neighbor "Please tell me you're moving in."
    arrival_neighbor "Otherwise, that's a very ambitious delivery."

    "You glance down at the box. Books. Kitchen things. One shoe."
    "A reasonably accurate summary of your packing system."

    arrival_neighbor "I live across the hall from the empty apartment."
    arrival_neighbor "Well. Formerly empty, I hope."
    arrival_neighbor "I'm Claire Bennett, by the way. And you are?"

    if not protagonist_name:

        window hide
        call screen protagonist_name_choice

        $ protagonist_name = clean_protagonist_name(_return)

    arrival_you "I'm [protagonist_name]. Nice to meet you."

    $ neighbor_introduced = True

    arrival_neighbor "Nice to meet you too, [protagonist_name]."

    "Something clicks against the floor inside her apartment. Then comes a single, hopeful bark."

    arrival_neighbor "Milo. Stay."
    arrival_neighbor "That's my dog. He thinks every open door means a walk."

    "The clicking stops. A tail thumps against the doorframe instead."

    arrival_neighbor "Now, about that box."
    arrival_neighbor "Want a hand?"

    window hide
    call choose_decision(FIRST_ARRIVAL_DECISION)
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

    $ story_scene_id = "first_arrival / apartment"

    scene bg intro_apartment
    show protagonist standing neutral at protagonist_apartment_entry
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
