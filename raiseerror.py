n=int(input("enter a number for multiplication"))
k=int(input("enter a number until table is running"))
if k<0:
    raise ValueError("please enter a positive number")
for i in range(1,k+1):
    print("the table is:",n*i)