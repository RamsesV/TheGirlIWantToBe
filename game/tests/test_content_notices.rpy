testsuite content_notice_tests:

    setup:

        $ persistent.content_tests_backup = dict(persistent.content_notice_acceptances)

    before testcase:

        $ persistent.content_notice_acceptances = {}

        if not screen "main_menu":

            if eval main_menu:
                run ShowMenu("main_menu")

            else:
                run MainMenu(confirm=False)

        pause until screen "main_menu"

    after testcase:

        if screen "content_age_gate":
            run Hide("content_age_gate")

        run ShowMenu("main_menu")

        pause until screen "main_menu"

    teardown:

        $ persistent.content_notice_acceptances = dict(persistent.content_tests_backup)
        $ persistent.content_tests_backup = None

        $ renpy.save_persistent()

    testcase edition_profiles:

        assert eval ("adult" in content_notice_ids("standard"))
        assert eval ("ai" in content_notice_ids("standard"))

        assert eval ("incest" not in content_notice_ids("standard"))
        assert eval ("animals" not in content_notice_ids("standard"))

        assert eval ("incest" in content_notice_ids("enhanced"))
        assert eval ("animals" in content_notice_ids("enhanced"))

        assert eval (
            content_notice_key("standard", 1)
            != content_notice_key("enhanced", 1)
        )

        assert eval (
            content_notice_key("standard", 1)
            != content_notice_key("standard", 2)
        )

    testcase confirmation_and_information:

        assert eval not content_notice_accepted()

        run Show("content_age_gate")

        pause until screen "content_age_gate"

        click id "content_age_confirm"

        assert eval content_notice_accepted()

        run Hide("content_age_gate")

        pause until not screen "content_age_gate"

        click id "content_icon_adult"

        pause until screen "content_information"

        scroll amount 30 pos (0.8, 0.5)

        assert id "content_boundaries"

        click "Return"

        pause until screen "main_menu"