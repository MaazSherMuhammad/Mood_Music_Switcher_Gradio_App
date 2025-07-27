# mood_logic.py

import random
from data import mood_song_map

mood_keywords = {
    "happy": ["happy", "joyful", "cheerful", "smiling"],
    "sad": ["sad", "down", "crying", "depressed"],
    "relaxed": ["relaxed", "calm", "chill", "peaceful"],
    "stressed": ["stressed", "anxious", "tense", "worried"],
    "excited": ["excited", "thrilled", "pumped", "energetic"]
}

def detect_mood(user_input):
    user_input = user_input.lower()
    for mood, keywords in mood_keywords.items():
        for keyword in keywords:
            if keyword in user_input:
                return mood
    return None

def suggest_song(mood):
    if mood not in mood_song_map:
        return None, None, None

    songs = mood_song_map[mood]["songs"]
    message = mood_song_map[mood]["message"]
    song_title, song_url = random.choice(songs)
    return song_title, song_url, message
