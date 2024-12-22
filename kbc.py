import pyttsx3
engine=pyttsx3.init()
engine.say("Your first question is on your screen")
engine.runAndWait()
s=0
x="what is computer"
print(x)
engine.say(x)
engine.runAndWait()
y=str(input("your options are: a) a machine b)a human c) a animal d) a bird"))
engine.say("your options are: a) a machine b)a human c) a animal")
engine.runAndWait()
a="a machine"
b="a human"
c="a animal"
d="a bird"
if y==a:
    s+=1000
    print("Correct you won 1000 rupees")
    engine.say("Correct you won 1000 rupees")
    engine.runAndWait()
else:
    print("wrong answer")
    engine.say("wrong answer")
    engine.runAndWait()
engine.say("Your second question is on your screen")
engine.runAndWait()
k="what is python"
print(k)
engine.say(k)
engine.runAndWait()
y=str(input("your options are: a) a snake b)a human c) a animal d) a bird"))
engine.say("your options are: a) a snake b)a human c) a animal")
engine.runAndWait()
a="a snake"
b="a human"
c="a animal"
d="a bird"
if y==a:
    s+=1000
    print("Correct you won 1000 rupees")
    engine.say("Correct you won 1000 rupees")
    engine.runAndWait()
else:
    print("wrong answer")
    engine.say("wrong answer")
    engine.runAndWait()
engine.runAndWait()