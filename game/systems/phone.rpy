default phone_unlocked = False
default phone_threads = {}


define PHONE_CONTACTS = {
    "partner": {"name": _("Boyfriend")},
    "ex": {"name": _("Ex")},
}


init python:

    def phone_add_message(
        contact_id,
        message_id,
        text,
        outgoing=False,
        image=None,
    ):
        """Add a message once without modifying shared chat data."""

        if contact_id not in PHONE_CONTACTS:
            raise ValueError(
                "Unknown phone contact: " + contact_id
            )

        messages = list(
            store.phone_threads.get(contact_id, ())
        )

        if any(
            message["id"] == message_id
            for message in messages
        ):
            return

        messages.append({
            "id": message_id,
            "text": text,
            "outgoing": outgoing,
            "image": image,
        })

        threads = dict(store.phone_threads)
        threads[contact_id] = messages

        store.phone_threads = threads
        store.phone_unlocked = True