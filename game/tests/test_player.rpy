testsuite global:

    teardown:
        exit

testsuite player_tests:

    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

        pause until screen "main_menu"
        run Start()
        advance until screen "background_select"

    testcase bookworm:
        click id "background_bookworm"
        click id "background_begin"
        advance until screen "choice"

        assert eval (player.background_id == "bookworm")
        assert eval (player.relationship_status == "long_distance")
        assert eval (player.attributes == {"intellect": 5, "stamina": 1, "charisma": 3})
        assert eval (player.submission == 5)
        assert eval (player.dominance == 0)
        assert eval (player.corruption == 0)
        assert eval (player.arousal == 0)

        assert eval (player.skills == {"oral": 0, "manual": 3, "body_awareness": 3, "anal": 0, "toys": 0, "dominance": 0, "submission": 2})
        assert eval (player.preferences == {"oral": 3, "roleplay": 3})

        click "Add 20 points"
        advance until "Arousal: 10"
        assert eval (player.arousal == 10)
        advance until screen "decision_choice"
        click id "decision_option_independent"
        advance until screen "main_menu"

    testcase girl_next_door:
        click id "background_girl_next_door"
        click id "background_begin"
        advance until screen "choice"

        assert eval (player.background_id == "girl_next_door")
        assert eval (player.relationship_status == "single")
        assert eval (player.attributes == {"intellect": 3, "stamina": 3, "charisma": 3})
        assert eval (player.submission == 0)
        assert eval (player.dominance == 0)
        assert eval (player.corruption == 0)
        assert eval (player.arousal == 0)

        assert eval (player.skills == {"oral": 0, "manual": 3, "body_awareness": 3, "anal": 0, "toys": 0, "dominance": 0, "submission": 0})
        assert eval (player.preferences == {"group": 3, "anal": 3})

        click "Subtract 20 points"
        advance until "Arousal: 0"
        assert eval (player.arousal == 0)
        advance until screen "decision_choice"
        click id "decision_option_independent"
        advance until screen "main_menu"

    testcase social_butterfly:
        click id "background_social_butterfly"
        click id "background_begin"
        advance until screen "choice"

        assert eval (player.background_id == "social_butterfly")
        assert eval (player.relationship_status == "open")
        assert eval (player.attributes == {"intellect": 1, "stamina": 3, "charisma": 5})
        assert eval (player.submission == 0)
        assert eval (player.dominance == 5)
        assert eval (player.corruption == 0)
        assert eval (player.arousal == 0)

        assert eval (player.skills == {"oral": 0, "manual": 3, "body_awareness": 3, "anal": 0, "toys": 0, "dominance": 2, "submission": 0})
        assert eval (player.preferences == {"bdsm": 3, "toys": 3})

        click "Leave unchanged"
        advance until "Arousal: 0"
        assert eval (player.arousal == 0)
        advance until screen "decision_choice"
        click id "decision_option_independent"
        advance until screen "main_menu"

    testcase arousal_calculation:
        python:
            # Use an independent object without altering the active player.
            subject = PlayerState()

            assert subject.arousal == 0

            subject.change_arousal(1)
            assert subject.arousal == 1

            subject.change_arousal(2)
            assert subject.arousal == 3

            subject.change_arousal(-1)
            assert subject.arousal == 2

            subject.change_arousal(0)
            assert subject.arousal == 2

            subject.change_arousal(20)
            assert subject.arousal == 10

            subject.change_arousal(1)
            assert subject.arousal == 10

            subject.change_arousal(-3)
            assert subject.arousal == 7

            subject.change_arousal(-20)
            assert subject.arousal == 0

            subject.change_arousal(-1)
            assert subject.arousal == 0


testsuite character_menu_tests:

    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

        pause until screen "main_menu"
        run Start()
        advance until screen "background_select"

    testcase bookworm_overview:
        click id "background_bookworm"
        click id "background_begin"
        advance until screen "choice"

        $ stats_before = (dict(player.attributes), player.submission, player.dominance, player.corruption, player.arousal, dict(player.skills), dict(player.preferences), player.background_id, player.relationship_status)

        click id "quick_player_stats"
        pause until screen "player_stats"
        assert id "stat_intellect"

        click id "player_stats_tab_skills"
        assert id "skill_submission"

        click id "player_stats_tab_preferences"
        assert id "preference_oral"

        click id "player_stats_close"
        pause until not screen "player_stats"
        assert screen "choice"
        assert eval (stats_before == (dict(player.attributes), player.submission, player.dominance, player.corruption, player.arousal, dict(player.skills), dict(player.preferences), player.background_id, player.relationship_status))

        click "Leave unchanged"
        advance until screen "decision_choice"
        click id "decision_option_independent"
        advance until screen "main_menu"

    testcase girl_next_door_overview:
        click id "background_girl_next_door"
        click id "background_begin"
        advance until screen "choice"

        $ stats_before = (dict(player.attributes), player.submission, player.dominance, player.corruption, player.arousal, dict(player.skills), dict(player.preferences), player.background_id, player.relationship_status)

        click id "quick_player_stats"
        pause until screen "player_stats"
        assert id "stat_intellect"

        click id "player_stats_tab_skills"
        assert id "skill_submission"

        click id "player_stats_tab_preferences"
        assert id "preference_group"

        click id "player_stats_close"
        pause until not screen "player_stats"
        assert screen "choice"
        assert eval (stats_before == (dict(player.attributes), player.submission, player.dominance, player.corruption, player.arousal, dict(player.skills), dict(player.preferences), player.background_id, player.relationship_status))

        click "Leave unchanged"
        advance until screen "decision_choice"
        click id "decision_option_independent"
        advance until screen "main_menu"

    testcase social_butterfly_overview:
        click id "background_social_butterfly"
        click id "background_begin"
        advance until screen "choice"

        $ stats_before = (dict(player.attributes), player.submission, player.dominance, player.corruption, player.arousal, dict(player.skills), dict(player.preferences), player.background_id, player.relationship_status)

        click id "quick_player_stats"
        pause until screen "player_stats"
        assert id "stat_intellect"

        click id "player_stats_tab_skills"
        assert id "skill_dominance"

        click id "player_stats_tab_preferences"
        assert id "preference_bdsm"

        click id "player_stats_close"
        pause until not screen "player_stats"
        assert screen "choice"
        assert eval (stats_before == (dict(player.attributes), player.submission, player.dominance, player.corruption, player.arousal, dict(player.skills), dict(player.preferences), player.background_id, player.relationship_status))

        click "Leave unchanged"
        advance until screen "decision_choice"
        click id "decision_option_independent"
        advance until screen "main_menu"
