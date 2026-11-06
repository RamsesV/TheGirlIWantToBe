    def gallery_replay_action(entry):
        """Give the replay independent player and appearance state."""

        replay_player = PlayerState()

        background_id = entry["background"]

        replay_player.apply_background(
            background_id,
            BACKGROUNDS[background_id],
        )

        return Replay(
            entry["label"],
            scope={
                "player": replay_player,
                "quick_menu": False,

                "protagonist_outfit": background_id,

                "npc_outfits": {
                    "neighbor": "casual",
                },

                "protagonist_name": PROTAGONIST_NAMES[0],
                "neighbor_introduced": False,
            },
            locked=not gallery_available(entry),
        )