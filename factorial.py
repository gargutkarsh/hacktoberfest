n=int(input("enter the number"))
f=1
i=1
if(n<0):
    print("factorial does not exist")
elif(n==0):
    print("factorial of zero is one")
else:
    while i<=n:
        f=f*i
        i+=1
print(f)        
        
    
