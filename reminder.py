import time
import os
from datetime import datetime, timedelta

from gtts import gTTS
from playsound import playsound


text, lang = "Drink some water!", "en"
audio_file = "audio.mp3"
minutes_60 = 60 * 30

if not os.path.exists(os.path.join(os.path.dirname(__file__), audio_file)):
    tts_obj = gTTS(text=text, lang=lang, slow=False)
    tts_obj.save(audio_file)

# ToDo - integrate with google calendars
# So this sound doesn't play when I am in a meeting!
while True:
    hour_in_india = (datetime.utcnow() + timedelta(hours=5, minutes=30)).time().hour
    should_play_sound = True if hour_in_india > 8 and hour_in_india < 20 else False
    if should_play_sound:
        playsound(audio_file)
    time.sleep(minutes_60)
