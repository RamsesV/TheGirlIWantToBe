# Independent outfits for all NPCs.
# Saved and restored along with normal game progress.
default npc_outfits = {
    "neighbor": "casual",
}


image neighbor standing neutral = "images/characters/neighbor/[npc_outfits['neighbor']]/standing_neutral.png"


# Shared positions for sprites on a 1024 x 1536 canvas.
transform character_left:
    xalign 0.22
    yalign 1.0

    zoom 0.70
    xzoom 1.0


transform character_center:
    xalign 0.5
    yalign 1.0

    zoom 0.70
    xzoom 1.0


transform character_right:
    xalign 0.78
    yalign 1.0

    zoom 0.70
    xzoom -1.0