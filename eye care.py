import time
import winsound
from playsound import playsound
from plyer import notification
def song():
    playsound('C:\\Users\\Hp\\Music\\mmm\\timer.mp3')
from win10toast import ToastNotifier
def timer(reminder):
    notificator =ToastNotifier()
    song()
    notificator.show_toast("Now You Can Continue :)",reminder,duration=20)
if __name__ == "__main__":
    while True:
        words="Meet You Next Time :)"
        notification.notify(
        title="Please Follow 20 20 20 Rule :)",
        message="Basically, every 20 minutes spent using a screen; you should try to look away at something that is 20 feet away from you for a total of 20 seconds.",
        app_icon = r"C:\Users\Hp\Desktop\python\icon.ico" ,
        timeout=20
        )
        timer(words)
        time.sleep(20*60)