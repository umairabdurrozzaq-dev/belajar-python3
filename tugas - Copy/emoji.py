def convert_moot(lit_mood):
    mood_map = {
        "senang": "🤣",
        "biasa": "😒",
        "sedih": "😭",
        "semangat": "😁"
    }

    return list(map(lambda m: mood_map.get(m, "🤷‍♂️"), lit_mood))