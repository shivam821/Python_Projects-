# from win10toast import ToastNotifier
# toaster = ToastNotifier()
# toaster.show_toast("Title","Message",duration=5)

from winotify import Notification,audio
import time

toast = Notification(app_id="Shivam_notification",title="Title",msg="Message",duration="short",icon=r"C:\idlex-1.18\Python_Projects\Windows Notification\image-files.png")
toast.set_audio(audio.SMS,loop=False)
toast.add_actions(label="Click Here",launch="https://www.freecodecamp.org/")
toast.show()
