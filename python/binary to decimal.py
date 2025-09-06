#binary to decimal
def btodec(n):
    p2=1
    t=0
    for i in range(len(n)-1,-1,-1):
        if(n[i]=='1'):
            t+=p2
        p2=p2*2
    return t
n="1101"
print(btodec(n))
# output- 13
