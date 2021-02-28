#JAMES STEVEN C. DULANGON
from gpiozero import DigitalOutputDevice, DigitalInputDevice
from time import sleep
from signal import pause

lock1 = DigitalOutputDevice(17, active_high= False, initial_value=False)
lock1 = DigitalOutputDevice(18, active_high= False, initial_value=False)

fbsignal1 = DigitalInputDevice(27,pull_up= True,bounce_time= 0.001)
fbsignal2 = DigitalInputDevice(22,pull_up= True, bounce_time= 0.001)

print("test")

def lock1_openMsg():
     print("LOCK 1 OPENN!")
     
def lock1_closeMsg():
     print("LOCK 1 CLOSED")
  
def lock2_openMsg():
     print("LOCK 2 OPEN!")

def lock2_closeMsg():
     print("LOCK 2 CLOSED")

fbsignal1.when_deactivated = lock1_openMsg
fbsignal1.when_activated = lock1_closeMsg  
fbsignal2.when_deactivated = lock2_openMsg
fbsignal2.when_activated = lock2_closeMsg  
        
        
pause()


