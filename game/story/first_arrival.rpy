default first_arrival_approach = None


define arrival_neighbor = Character(_("Neighbor"))


label first_arrival:

    scene black

    "The address matches the email. The key matches the lock."
    "That should be enough to make this place feel like yours."
    "It isn't. Not yet."

    "Two bags wait at your feet. The largest box is slowly slipping out of your arms."

    if player.background_id == "bookworm":

        "You checked the route twice before leaving."
        "Somehow, neither version mentioned the entrance steps."

        "Your phone vibrates."

        "'Made it? Call me when you're settled. Miss you already.'"

        "You smile at the message."
        "For now, the distance is just a number on a map."

    elif player.background_id == "social_butterfly":

        "You shift the box against your hip and glance at your phone."

        "'Made it? Go meet your neighbors. I expect stories.'"

        "You send back a picture of the front door."

        "The conversation about opening the relationship had felt straightforward."
        "Standing here alone, you realize the practical part starts now."

    else:

        "Your thumb hovers over a familiar conversation."
        "For years, arriving somewhere meant telling him you'd arrived."

        "You put the phone away."
        "Tonight, you'll unpack first."

    "A door opens behind you."

    arrival_neighbor "Please tell me you're moving in."

    "A woman stands in the doorway, holding a mug."

    arrival_neighbor "Otherwise, that's a very ambitious delivery."

    "You glance down at the box."

    "Books. Kitchen things. One shoe."
    "A reasonably accurate summary of your packing system."

    arrival_neighbor "I live across the hall from the empty apartment."
    arrival_neighbor "Well. Formerly empty, I hope."

    "She sets her mug down inside and holds the entrance open."

    arrival_neighbor "Want a hand?"

    call choose_decision(FIRST_ARRIVAL_DECISION)

    $ first_arrival_approach = _return

    if first_arrival_approach == "accept":

        "You give her your name and admit that the box is heavier than it looks."

        arrival_neighbor "They always are."

        "She picks up one of your bags."

        arrival_neighbor "Come on. I'll show you which stair complains the loudest."

        "By the time you reach your apartment, you know which landing light flickers and where parcels usually end up."

        "The building already feels a little less unfamiliar."

    elif first_arrival_approach == "negotiate":

        "You suggest a division of labor: she keeps the doors open, you bring everything inside."

        arrival_neighbor "Management material. I can tell."

        "She opens the door wider."

        arrival_neighbor "Fine. But if you drop that box, I'm promoting myself."

        "You make it upstairs with your belongings and most of your dignity intact."

        arrival_neighbor "We work well together. Dangerous thing to discover this early."

    elif first_arrival_approach == "notice":

        "You ask whether the side entrance shown on the building plan is still in use."

        "She looks at you, then at the steps."

        arrival_neighbor "You read the building plan?"

        "You explain that it seemed useful before moving."

        arrival_neighbor "It is useful. There's a ramp around the corner."

        "She picks up her mug."

        arrival_neighbor "I've lived here two years. You're already better prepared."

        "The second entrance makes the remaining trips considerably easier."

    else:

        "You thank her and explain that you'd like to get settled on your own."

        arrival_neighbor "Of course."

        "She steps aside, leaving the door open."

        arrival_neighbor "Across the hall if you need anything."
        arrival_neighbor "Advice is free. Coffee depends on how much I've had."

        "You smile, thank her again, and carry your things upstairs."

    "Eventually, the last bag lands inside your apartment."

    "You close the door and listen."

    "A tap runs somewhere nearby. Footsteps cross the ceiling."
    "From across the hall comes the faint sound of a cupboard closing."

    "You put your key on the kitchen counter."

    "Tomorrow, you'll need groceries."
    "Tonight, you need to find the other shoe."

    $ unlock_gallery_replay("first_arrival")

    $ renpy.end_replay()

    return