default persistent.content_notice_acceptances = {}


init python:

    def content_notice_ids(edition=None):

        if edition is None:
            edition = CONTENT_EDITION

        return CONTENT_EDITION_NOTICES[edition]


    def content_notice_key(edition=None, revision=None):

        if edition is None:
            edition = CONTENT_EDITION

        if revision is None:
            revision = CONTENT_NOTICE_REVISION

        return "{}:{}".format(edition, revision)


    def content_notice_accepted():

        return bool(
            persistent.content_notice_acceptances.get(
                content_notice_key(),
                False,
            )
        )


    def accept_content_notice():

        acceptances = dict(
            persistent.content_notice_acceptances
        )

        acceptances[content_notice_key()] = True

        persistent.content_notice_acceptances = acceptances

        renpy.save_persistent()


    def content_notice_icon(notice_id):

        index = CONTENT_NOTICES[notice_id][0]

        return Transform(
            Crop(
                (index * 96, 0, 96, 96),
                "gui/notice_icons.svg",
            ),
            zoom=0.5,
        )