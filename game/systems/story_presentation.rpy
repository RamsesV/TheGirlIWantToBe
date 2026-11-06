default persistent.walkthrough_setup_done = False

default decision_context_who = None
default decision_context_text = ""

default story_scene_id = None


init python:

    def story_decision_context(decision):

        if _history_list:
            entry = _history_list[-1]
            return entry.who, entry.what

        return None, _(decision["prompt"])


    def finish_walkthrough_setup():

        if not persistent.walkthrough_setup_done:
            persistent.walkthrough_setup_done = True
            renpy.save_persistent()