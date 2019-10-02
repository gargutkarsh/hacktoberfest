n=int(input("enter any 3 digit no."))
temp=n
sum=0
if(n<=999):
    while (n>0):
        dig=n%10
        sum=sum+dig**3
        n=n//10
    if(temp==sum):
        print("entered number is armstrong no.")
    else:
        print("no. is not armstrong")
else:
    print("enter number less than 999")
