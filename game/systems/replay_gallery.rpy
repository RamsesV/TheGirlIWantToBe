default persistent.gallery_unlocks = {}
default persistent.gallery_unlock_all = False


init python:

    def gallery_entries():
        """Only list registered scenes whose labels are installed."""

        return [
            entry
            for entry in GALLERY_REPLAYS
            if renpy.has_label(entry["label"])
        ]


    def gallery_available(entry):
        """Keep earned unlocks separate from the unlock-all override."""

        return (
            renpy.has_label(entry["label"])
            and (
                persistent.gallery_unlock_all
                or persistent.gallery_unlocks.get(
                    entry["id"], False
                )
            )
        )


    def unlock_gallery_replay(replay_id):
        """Earn unlocks during normal play, never during a replay."""

        if renpy.store._in_replay:
            return

        if not any(
            entry["id"] == replay_id
            for entry in gallery_entries()
        ):
            raise ValueError("Unknown replay: " + replay_id)

        if not persistent.gallery_unlocks.get(replay_id, False):
            unlocks = dict(persistent.gallery_unlocks)
            unlocks[replay_id] = True

            persistent.gallery_unlocks = unlocks
            renpy.save_persistent()


    def toggle_gallery_unlock_all():
        persistent.gallery_unlock_all = (
            not persistent.gallery_unlock_all
        )

        renpy.save_persistent()


    def reset_gallery():
        persistent.gallery_unlocks = {}
        persistent.gallery_unlock_all = False

        renpy.save_persistent()


    def gallery_replay_action(entry):
        """Give the replay independent player data."""

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
                "npc_outfits": {"neighbor": "casual"},
            },
            locked=not gallery_available(entry),
        )