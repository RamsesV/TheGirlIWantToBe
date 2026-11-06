# Walkthrough preferences persist across playthroughs.
default persistent.walkthrough_mode = "off"
default persistent.show_unavailable_choices = False
default persistent.walkthrough_setup_done = False

# Context is saved with the current decision.
default decision_context_who = None
default decision_context_text = ""

# Display names used by the full walkthrough.
define DECISION_VALUE_LABELS = {
    "attributes.intellect": _("Intellect"),
    "attributes.stamina": _("Stamina"),
    "attributes.charisma": _("Charisma"),
    "submission": _("Submission"),
    "dominance": _("Dominance"),
    "corruption": _("Corruption"),
    "arousal": _("Arousal"),
}


init python:

    def decision_value(actor, key):
        """Read a supported player value."""

        parts = key.split(".")

        if len(parts) == 2 and parts[0] in (
            "attributes", "skills", "preferences"
        ):
            values = getattr(actor, parts[0])

            if parts[0] != "preferences" and parts[1] not in values:
                raise ValueError("Unknown decision value: " + key)

            return values.get(parts[1], 0)

        if key in (
            "submission", "dominance", "corruption", "arousal"
        ):
            return getattr(actor, key)

        raise ValueError("Unknown decision value: " + key)


    def decision_available(option, actor):
        """Check all requirements without changing anything."""

        for key, minimum, maximum in option.get("requires", ()):
            value = decision_value(actor, key)

            if minimum is not None and value < minimum:
                return False

            if maximum is not None and value > maximum:
                return False

        return True


    def decision_visible(
        option,
        actor,
        mode=None,
        show_unavailable=None,
    ):
        """Determine visibility without changing availability."""

        if mode is None:
            mode = persistent.walkthrough_mode

        if show_unavailable is None:
            show_unavailable = persistent.show_unavailable_choices

        return (
            decision_available(option, actor)
            or mode == "full"
            or show_unavailable
        )


    def decision_target(actor, key, amount):
        """Calculate the resulting value, including limits."""

        value = max(0, decision_value(actor, key) + amount)

        if key == "arousal":
            value = min(10, value)

        return value


    def apply_decision(option, actor):
        """Apply effects only if the choice is available."""

        if not decision_available(option, actor):
            raise ValueError(
                "Decision requirements are not met: " + option["id"]
            )

        # Validate every effect before changing any values.
        updates = [
            (key, decision_target(actor, key, amount))
            for key, amount in option.get("effects", {}).items()
        ]

        for key, value in updates:
            if "." in key:
                group, name = key.split(".")
                getattr(actor, group)[name] = value
            else:
                setattr(actor, key, value)


    def decision_details(option, actor):
        """Build the full walkthrough from actual decision data."""

        lines = []

        for key, minimum, maximum in option.get("requires", ()):
            name = _(DECISION_VALUE_LABELS[key])

            if minimum is not None:
                lines.append(
                    _("Requires {name} >= {value}").format(
                        name=name,
                        value=minimum,
                    )
                )

            if maximum is not None:
                lines.append(
                    _("Requires {name} <= {value}").format(
                        name=name,
                        value=maximum,
                    )
                )

        for key, amount in option.get("effects", {}).items():
            name = _(DECISION_VALUE_LABELS[key])

            change = (
                decision_target(actor, key, amount)
                - decision_value(actor, key)
            )

            lines.append(
                _("{name}: {change:+d}").format(
                    name=name,
                    change=change,
                )
            )

        if not option.get("effects"):
            lines.append(_("No stat changes."))

        lines.append(
            _("Path: {path}").format(path=_(option["path"]))
        )

        return " | ".join(lines)

    def story_decision_context(decision):
        """Snapshot the previous line before opening the decision screen."""

        if _history_list:
            entry = _history_list[-1]
            return entry.who, entry.what

        return None, _(decision["prompt"])


    def finish_walkthrough_setup():
        """Confirm the first walkthrough choice across playthroughs."""

        if not persistent.walkthrough_setup_done:
            persistent.walkthrough_setup_done = True
            renpy.save_persistent()