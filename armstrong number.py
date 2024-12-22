x=int(input("enter a number"))
fe=x
sum=0
while fe>0:
    k= fe % 10
    sum=sum+k**3
    fe//=10
if x==sum:
    print("yes it is a armstrong number")
else:
    print("not an armstrong")
# emp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10