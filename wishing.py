import time
import 
engine=pyttsx3.init()
engine.say("hello sir")
hour = int(time.strftime("%H"))
print(hour)
if(hour>0 and hour<12):
    engine.say("Good Morning sir")
elif(hour>=12 and hour<16):
    engine.say("Good Afternoon sir")
elif(hour>16 and hour<24):
    engine.say("good night sir")
engine.runAndWait()
