import math 
n,m = [int(x) for x in input().split()]
l =  [int(x) for x in input().split()]
l.sort()
if (len(l)==0):
    print(1)
else:
    arr = []
    if (l[0]!=1):
        arr.append(l[0]-1)
    if (l[-1]!=n):
        arr.append(n-l[-1])
    for i in range(m-1):
        if (l[i+1]-l[i]-1!=0):
            arr.append(l[i+1]-l[i]-1)
    
    
    ans = 0
    if (len(arr)==0):
        print(0)
    else:
        m = min(arr)
        
        if (m==0):
            print(0)
        else:
            
            for i in arr:
                ans+=math.ceil(i/m)
            print(ans)
