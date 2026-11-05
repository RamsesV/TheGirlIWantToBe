testsuite decision_tests:

    setup:
        $ persistent.decision_tests_original_mode = persistent.walkthrough_mode

    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

        pause until screen "main_menu"
        run Start()

        $ persistent.walkthrough_mode = "off"

        advance until screen "background_select"
        click id "background_bookworm"
        click id "background_begin"

        advance until screen "choice"
        click "Leave unchanged"

        advance until screen "decision_choice"

    teardown:
        $ persistent.walkthrough_mode = persistent.decision_tests_original_mode
        $ persistent.decision_tests_original_mode = None

    testcase walkthrough_and_effects:

        assert not id "decision_hint_study"
        assert not id "decision_details_study"

        click id "walkthrough_hints"
        assert id "decision_hint_study"
        assert not id "decision_details_study"

        click id "walkthrough_full"
        assert id "decision_details_study"
        assert not id "decision_hint_study"

        # Switching display modes must not award points.
        assert eval (player.attributes["intellect"] == 5)
        assert eval (player.submission == 5)

        click id "decision_option_study"

        advance until "Decision test complete."

        assert eval (player.attributes["intellect"] == 6)
        assert eval (player.submission == 5)

        advance until screen "main_menu"

    testcase requirements_and_limits:

        python:
            subject = PlayerState()
            subject.attributes["intellect"] = 5

            study = next(
                option
                for option in ARRIVAL_DECISION["options"]
                if option["id"] == "study"
            )

            subject.arousal = 6
            assert decision_available(study, subject)

            subject.arousal = 7
            assert not decision_available(study, subject)

            try:
                apply_decision(study, subject)
            except ValueError:
                pass
            else:
                raise AssertionError("Locked choice was accepted.")

            assert subject.attributes["intellect"] == 5

            subject.arousal = 0

            apply_decision(
                {"id": "upper_limit", "effects": {"arousal": 20}},
                subject,
            )
            assert subject.arousal == 10

            apply_decision(
                {"id": "lower_limit", "effects": {"arousal": -20}},
                subject,
            )
            assert subject.arousal == 0

            apply_decision(
                {"id": "two_points", "effects": {"dominance": 2}},
                subject,
            )
            assert subject.dominance == 2