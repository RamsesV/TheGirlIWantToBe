init python:

    class PlayerState:
        """Mutable player data stored in saves."""

        def __init__(self):
            self.background_id = None
            self.relationship_status = None

            self.attributes = {
                "intellect": 3,
                "stamina": 3,
                "charisma": 3,
            }

            self.submission = 0
            self.dominance = 0
            self.corruption = 0
            self.arousal = 0

            self.skills = {
                "oral": 0,
                "manual": 3,
                "body_awareness": 3,
                "anal": 0,
                "toys": 0,
                "dominance": 0,
                "submission": 0,
            }

            self.preferences = {}

        def apply_background(self, background_id, profile):
            """Apply starting data to a fresh player object."""

            self.background_id = background_id
            self.relationship_status = profile["relationship_status"]

            # Copy mutable data instead of sharing profile dictionaries.
            self.attributes = dict(profile["attributes"])

            self.submission = profile["submission"]
            self.dominance = profile["dominance"]

            self.skills.update(profile["skills"])
            self.preferences = dict(profile["preferences"])

        def change_arousal(self, amount):
            """Keep arousal between 0 and 10."""

            self.arousal = max(0, min(10, self.arousal + amount))

        def get_preference(self, preference_id):
            """Preferences without an assigned value start at zero."""

            return self.preferences.get(preference_id, 0)


default player = PlayerState()