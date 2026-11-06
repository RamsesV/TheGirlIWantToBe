testsuite gallery_tests:

    before testcase:

        if not screen "main_menu":

            if eval main_menu:
                run ShowMenu("main_menu")

            else:
                run MainMenu(confirm=False)

        pause until screen "main_menu"

        $ persistent.gallery_unlocks = {}
        $ persistent.gallery_unlock_all = False

        run ShowMenu("replay_gallery")
        pause until screen "replay_gallery"

    testcase unlock_all_preserves_earned_unlocks:

        assert eval (
            not gallery_available(GALLERY_REPLAYS[0])
        )

        click id "gallery_unlock_all"

        assert eval persistent.gallery_unlock_all
        assert eval gallery_available(GALLERY_REPLAYS[0])
        assert eval (persistent.gallery_unlocks == {})

        click id "gallery_unlock_all"

        assert eval (
            not gallery_available(GALLERY_REPLAYS[0])
        )

        $ unlock_gallery_replay("arrival")

        assert eval (
            persistent.gallery_unlocks == {"arrival": True}
        )

        click id "gallery_unlock_all"
        click id "gallery_unlock_all"

        assert eval gallery_available(GALLERY_REPLAYS[0])

        assert eval (
            persistent.gallery_unlocks == {"arrival": True}
        )

    testcase reset_confirmation:

        $ unlock_gallery_replay("arrival")

        click id "gallery_unlock_all"

        click id "gallery_reset"
        pause until screen "confirm"

        click "No"
        pause until not screen "confirm"

        assert eval persistent.gallery_unlock_all

        assert eval (
            persistent.gallery_unlocks == {"arrival": True}
        )

        click id "gallery_reset"
        pause until screen "confirm"

        click "Yes"
        pause until not screen "confirm"

        assert eval (persistent.gallery_unlocks == {})
        assert eval (persistent.gallery_unlock_all is False)

        assert eval (
            not gallery_available(GALLERY_REPLAYS[0])
        )

    testcase replay_does_not_earn_unlock:

        click id "gallery_unlock_all"
        click id "gallery_replay_arrival"

        advance until "The street outside is unfamiliar"

        assert eval (_in_replay == "memory_arrival")

        advance until screen "replay_gallery"

        assert eval (persistent.gallery_unlocks == {})

        click id "gallery_unlock_all"

        assert eval (
            not gallery_available(GALLERY_REPLAYS[0])
        )

    testcase replay_preserves_player_state:

        click "Start"

        advance until screen "background_select"

        click id "background_bookworm"
        click id "background_begin"

        advance until screen "decision_choice"
        click id "decision_option_accept"

        advance until screen "choice"

        assert eval (
            persistent.gallery_unlocks.get("arrival", False)
        )

        $ player.change_arousal(4)

        $ persistent.gallery_replay_snapshot = (
            dict(player.attributes),
            player.submission,
            player.dominance,
            player.corruption,
            player.arousal,
            dict(player.skills),
            dict(player.preferences),
            player.background_id,
            player.relationship_status,
        )

        run ShowMenu("replay_gallery")
        pause until screen "replay_gallery"

        click id "gallery_replay_arrival"

        advance until "The street outside is unfamiliar"

        assert eval (_in_replay == "memory_arrival")

        # The replay uses an independent, predefined character.
        assert eval (
            player.background_id == "girl_next_door"
        )

        advance until screen "replay_gallery"

        assert eval (
            persistent.gallery_replay_snapshot == (
                dict(player.attributes),
                player.submission,
                player.dominance,
                player.corruption,
                player.arousal,
                dict(player.skills),
                dict(player.preferences),
                player.background_id,
                player.relationship_status,
            )
        )

        click "Return"
        pause until screen "choice"

        assert eval (player.arousal == 4)

        click "Leave unchanged"

        advance until screen "decision_choice"
        click id "decision_option_independent"

        advance until screen "main_menu"