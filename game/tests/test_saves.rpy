testsuite save_tests:

    setup:
        $ persistent.save_test_state = {
            "original_page": FileCurrentPage(),
            "original_mode": persistent.walkthrough_mode,
            "original_visibility": persistent.show_unavailable_choices,
            "owns_slot": False,
        }

    before testcase:
        $ persistent.save_test_state["owns_slot"] = False

        # Never overwrite an existing save.
        assert eval (1 not in FileUsedSlots(page="9999"))

        if not screen "main_menu":
            run MainMenu(confirm=False)

        pause until screen "main_menu"
        run Start("test_start")

        $ persistent.walkthrough_mode = "off"
        $ persistent.show_unavailable_choices = False

        advance until screen "background_select"
        click id "background_bookworm"
        click id "background_begin"
        advance until screen "phone"
        click id "phone_close"
        advance until screen "protagonist_name_choice"
        click id "protagonist_name_confirm"

        advance until screen "decision_choice"
        click id "decision_option_accept"

        advance until screen "choice"
        click "Leave unchanged"

        advance until screen "decision_choice"

    after testcase:
        # Only delete a slot created by this test.
        if eval persistent.save_test_state["owns_slot"]:
            if eval FileLoadable(1, page="9999"):
                run FileDelete(
                    1,
                    page="9999",
                    confirm=False,
                )

        $ persistent.save_test_state["owns_slot"] = False

        run FilePage(
            persistent.save_test_state["original_page"]
        )

    teardown:
        $ persistent.walkthrough_mode = persistent.save_test_state["original_mode"]
        $ persistent.show_unavailable_choices = persistent.save_test_state["original_visibility"]
        $ persistent.save_test_state = None

    testcase named_save_and_load:

        assert eval (player.background_id == "bookworm")
        assert eval (player.arousal == 0)

        run ShowMenu("save")
        pause until screen "save"

        run FilePage(9999)

        click id "file_slot_1"
        pause until screen "save_name_prompt"

        # Clear the suggested name and enter a custom title.
        keysym "K_END"
        keysym "K_BACKSPACE" repeat 60
        type "Automated save"

        $ persistent.save_test_state["owns_slot"] = True

        click id "save_title_confirm"
        pause until not screen "save_name_prompt"

        assert eval FileLoadable(1, page="9999")
        assert eval (FileSaveName(1, page="9999") == "Automated save")

        # Cancelling overwrite must preserve the existing save.
        click id "file_slot_1"
        pause until screen "confirm"

        click "No"
        pause until not screen "confirm"

        assert eval (FileSaveName(1, page="9999") == "Automated save")

        # Confirm overwrite and change the title.
        click id "file_slot_1"
        pause until screen "confirm"

        click "Yes"
        pause until screen "save_name_prompt"

        keysym "K_END"
        keysym "K_BACKSPACE" repeat 60
        type "Renamed automated save"

        click id "save_title_confirm"
        pause until not screen "save_name_prompt"

        assert eval (
            FileSaveName(1, page="9999")
            == "Renamed automated save"
        )

        click "Return"
        pause until screen "decision_choice"

        # Change the current state after saving.
        $ player.change_arousal(7)
        assert eval (player.arousal == 7)

        run ShowMenu("load")
        pause until screen "load"

        run FilePage(9999)

        click id "file_slot_1"
        pause until screen "confirm"

        click "Yes"
        pause until screen "decision_choice"

        # Loading must restore the saved state.
        assert eval (player.background_id == "bookworm")
        assert eval (player.attributes["intellect"] == 5)
        assert eval (player.submission == 5)
        assert eval (player.arousal == 0)

        assert eval (
            FileSaveName(1, page="9999")
            == "Renamed automated save"
        )

        click id "decision_option_independent"
        advance until screen "main_menu"

    testcase cancel_save_name:

        $ persistent.save_test_state["old_name"] = save_name

        run ShowMenu("save")
        pause until screen "save"

        run FilePage(9999)

        click id "file_slot_1"
        pause until screen "save_name_prompt"

        keysym "K_END"
        keysym "K_BACKSPACE" repeat 60
        type "This must not be saved"

        click id "save_title_cancel"
        pause until not screen "save_name_prompt"

        assert eval (1 not in FileUsedSlots(page="9999"))

        assert eval (
            save_name
            == persistent.save_test_state["old_name"]
        )

        click "Return"
        pause until screen "decision_choice"

        click id "decision_option_independent"
        advance until screen "main_menu"

    testcase decision_rollback:

        assert eval (player.submission == 5)

        click id "decision_option_guided"

        advance until "You ask for help and let someone show you around."

        assert eval (player.submission == 6)

        # Simulate the player's rollback key.
        keysym "rollback"
        pause until screen "decision_choice"

        assert eval (player.submission == 5)
        assert eval (player.attributes["intellect"] == 5)

        # Selecting again must award exactly one point.
        click id "decision_option_guided"

        advance until "You ask for help and let someone show you around."

        assert eval (player.submission == 6)

        advance until screen "main_menu"