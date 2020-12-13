n,m,T= [int(x) for x in input().split()]
charge = n
f = 0
prev=0
for i in range(m):
    
    a,b = [int(x) for x in input().split()]
    charge-=(a-prev)
    if (charge<=0):
        f = 1
        
        print("No")
        break
    charge+=b-a
    prev=b
    charge=min(charge,n)
    
charge = charge-(T-b)
if (f==0):
    if (charge<=0):
        f = 1
        print("No")
if (f==0):
    print("Yes")
    
