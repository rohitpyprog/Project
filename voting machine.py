a=b=0
for x in range(10):
   x =str(input("which team you want to vote team a or team b: "))
   if x=="a":
      a+=1
   else:
      b+=1
print("The votes of team A are :",a)
print("The votes of team B are :",b)