label choose_decision(decision):

    call screen decision_choice(decision)

    $ decision_result = _return

    $ selected_option = next(
        option
        for option in decision["options"]
        if option["id"] == decision_result
    )

    $ apply_decision(selected_option, player)

    return decision_result


label decision_demo:

    call choose_decision(ARRIVAL_DECISION)

    if _return == "guided":
        "You ask for help and let someone show you around."

    elif _return == "lead":
        "You gather the newcomers and organize the afternoon."

    elif _return == "study":
        "You spend the afternoon preparing for your first week."

    else:
        "You explore the neighborhood at your own pace."

    "Decision test complete. You can check your updated values in Character."

    return