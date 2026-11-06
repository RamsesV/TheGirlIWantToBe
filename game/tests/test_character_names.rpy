testsuite character_name_tests:

    before testcase:

        if not screen "main_menu":

            if eval main_menu:
                run ShowMenu("main_menu")
            else:
                run MainMenu(confirm=False)

        pause until screen "main_menu"
        run Start()

        advance until screen "background_select"

        click id "background_girl_next_door"
        click id "background_begin"

        advance until screen "phone"
        click id "phone_close"
        advance until screen "protagonist_name_choice"

    after testcase:

        run MainMenu(confirm=False)
        pause until screen "main_menu"

    testcase preset_names:

        assert id "name_preset_emma"
        assert id "name_preset_olivia"
        assert id "name_preset_chloe"

        click id "name_preset_olivia"
        click id "protagonist_name_confirm"

        advance until screen "decision_choice"

        assert eval (protagonist_name == "Olivia")
        assert eval neighbor_introduced
        assert eval bool(neighbor_name.strip())
        assert eval bool(neighbor_dog_name.strip())

        assert eval (
            neighbor_name in neighbor_introduction_text()
        )

    testcase custom_name_and_empty_input:

        click id "protagonist_name_input"

        keysym "K_END"
        keysym "K_BACKSPACE" repeat 30

        type "   "
        keysym "K_RETURN"

        assert screen "protagonist_name_choice"

        type "Avery"
        click id "protagonist_name_confirm"

        advance until screen "decision_choice"

        assert eval (protagonist_name == "Avery")