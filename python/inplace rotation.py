#using two pointers technique- reversing an arr without using any slicing operator
def reve(arr):
    n=len(arr)
    l=0  #left operator
    r=n-1  #right operator
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr
arr=[1,2,3,4]
print(reve(arr))
#output- [4, 3, 2, 1]