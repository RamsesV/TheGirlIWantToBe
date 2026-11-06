testsuite first_arrival_tests:

    setup:
        $ persistent.arrival_test_mode = persistent.walkthrough_mode
        $ persistent.arrival_test_visibility = persistent.show_unavailable_choices

    before testcase:

        if not screen "main_menu":

            if eval main_menu:
                run ShowMenu("main_menu")
            else:
                run MainMenu(confirm=False)

        pause until screen "main_menu"
        run Start()

        $ persistent.walkthrough_setup_done = False
        $ persistent.walkthrough_mode = "off"
        $ persistent.show_unavailable_choices = False

        advance until screen "background_select"

    after testcase:
        run MainMenu(confirm=False)
        pause until screen "main_menu"

    teardown:
        $ persistent.walkthrough_mode = persistent.arrival_test_mode
        $ persistent.show_unavailable_choices = persistent.arrival_test_visibility
        $ persistent.arrival_test_mode = None
        $ persistent.arrival_test_visibility = None

    testcase bookworm_accepts_help:
        click id "background_bookworm"
        click id "background_begin"
        advance until screen "protagonist_name_choice"
        click id "protagonist_name_confirm"
        advance until screen "decision_choice"

        assert eval (protagonist_outfit == "bookworm")
        assert eval (npc_outfits["neighbor"] == "casual")
        assert eval renpy.showing("protagonist standing neutral")
        assert eval renpy.showing("neighbor standing neutral")
        assert id "decision_option_notice"
        assert not id "decision_option_negotiate"

        click id "decision_option_accept"
        advance until "Tomorrow, groceries."

        assert eval (first_arrival_approach == "accept")
        assert eval (player.attributes["intellect"] == 5)
        assert eval (player.submission == 5)
        assert eval (not renpy.showing("neighbor"))

    testcase bookworm_finds_second_entrance:
        click id "background_bookworm"
        click id "background_begin"
        advance until screen "protagonist_name_choice"
        click id "protagonist_name_confirm"
        advance until screen "decision_choice"
        click id "decision_option_notice"
        advance until "Tomorrow, groceries."
        assert eval (first_arrival_approach == "notice")

    testcase social_butterfly_makes_deal:
        click id "background_social_butterfly"
        click id "background_begin"
        advance until screen "protagonist_name_choice"
        click id "protagonist_name_confirm"
        advance until screen "decision_choice"

        assert eval (protagonist_outfit == "social_butterfly")
        assert id "decision_option_negotiate"
        assert not id "decision_option_notice"

        click id "decision_option_negotiate"
        advance until "Tomorrow, groceries."
        assert eval (first_arrival_approach == "negotiate")
        assert eval (player.dominance == 5)

    testcase girl_next_door_moves_in_alone:
        click id "background_girl_next_door"
        click id "background_begin"
        advance until screen "protagonist_name_choice"
        click id "protagonist_name_confirm"
        advance until screen "decision_choice"

        assert eval (protagonist_outfit == "girl_next_door")
        assert not id "decision_option_negotiate"
        assert not id "decision_option_notice"

        click id "decision_option_alone"
        advance until "Tomorrow, groceries."
        assert eval (first_arrival_approach == "alone")

    testcase replay_preserves_outfit_and_approach:

        click id "background_bookworm"
        click id "background_begin"

        advance until screen "protagonist_name_choice"

        click id "name_preset_chloe"
        click id "protagonist_name_confirm"

        advance until screen "decision_choice"
        click id "decision_option_notice"

        advance until screen "choice"

        run ShowMenu("replay_gallery")
        pause until screen "replay_gallery"

        click id "gallery_replay_first_arrival"

        advance until screen "decision_choice"

        assert eval (_in_replay == "first_arrival")
        assert eval (player.background_id == "girl_next_door")
        assert eval (protagonist_outfit == "girl_next_door")
        assert eval (protagonist_name == "Emma")

        click id "decision_option_accept"

        advance until screen "replay_gallery"

        assert eval (protagonist_outfit == "bookworm")
        assert eval (protagonist_name == "Chloe")
        assert eval (first_arrival_approach == "notice")

        click "Return"
        pause until screen "choice"

    testcase walkthrough_setup_only_once:

        click id "background_bookworm"
        click id "background_begin"
        advance until screen "protagonist_name_choice"
        click id "protagonist_name_confirm"

        advance until screen "decision_choice"

        assert id "walkthrough_hints"
        assert id "decision_context_text"
        assert eval (decision_context_text == "Want a hand?")

        click id "walkthrough_hints"
        click id "decision_option_accept"

        advance until screen "choice"

        assert eval persistent.walkthrough_setup_done
        assert eval (persistent.walkthrough_mode == "hints")

        click "Leave unchanged"
        advance until screen "decision_choice"

        assert not id "walkthrough_hints"
        assert id "decision_hint_study"
