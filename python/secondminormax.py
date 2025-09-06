#find 2nd min and 2nd max from the given arr,and also return if the elements are same or return no 2nd min and max if they dont exist.

def min22(arr):
    if len(arr)<2:
        return 
    min1=max1=arr[0]
    for num in arr:
        if num<min1:
            min1=num
        if num>max1:
            max1=num
    min2=float('inf')               #inf= infinity
    max2=float('-inf')
    for num in arr:
        if min1<num<min2:
            min2=num
        if max1>num>max2:
            max2=num
    if min1==max1:
        print("all are same")
    if min2==float('inf'):
        print("no 2nd main")
    else:
        print(min2)
    if max2==float('-inf'):
        print("no second max")
    else:
        print(max2)
arr=[2,2,2,2]
print(min22(arr))
#output-
'''all are same
no 2nd main
no second max
None'''