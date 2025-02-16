import time
import os
from gtts import gTTS

# Create sound of your own
def create_sound():
    userDecision = input("Do you want to create your own sound? (yes/no): ").lower()
    if userDecision == "yes" or userDecision == "y":
        userInput = input("Enter what you want to hear: ")
        tts = gTTS(text=userInput, lang="en")
        tts.save("alarm.wav")
    else:
        text = "Time's up!"
        tts = gTTS(text=text, lang="en")
        tts.save("alarm.wav")

#Play the sound you created
def play_beep():
    # Play the beep sound
    print("\a")
    os.system("afplay ../TimeCounter/alarm.wav")

#Count down timer function
def countdown_timer(seconds):
    create_sound()  # creating beep/alarm
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(time_format, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")
    play_beep()  # Play the beep/alarm when the timer reaches 0

#countdown_timer(10)  # 10-second countdown
countdown_duration = int(input("Enter the duration of the countdown in seconds: "))
countdown_timer(countdown_duration)