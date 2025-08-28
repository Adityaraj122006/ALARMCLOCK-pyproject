
import datetime
import time
import pygame

alarm_time = input("ENTER THE ALARM TIME(HH:MM:SS) : ")

def set_alarm(alarm_time):
    print(f"THE ALARM WAS SET FOR : {alarm_time}")
    sound_file = "alarmsound.mp3.mp3"
    is_running = True

    while is_running :
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time :
            print("TIME'S UP, WAKE UP !")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)

set_alarm(alarm_time)