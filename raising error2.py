num=(input("enter a number between 5 to 9"))
if num.lower()=="quit":
    print("sorry You are quit")
elif(int(num)<5 or int(num)>9):
    raise ValueError("please enter a number between 5 and 9")
