#To count the number of factors of a given number
n=int(input("Enter a number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(f"The number of factors of {n} is {count}")

#decrease time complexity to O(sqrt(n)) and increase efficiency
'''n=int(input("Enter a number: "))
print(f"The factors of {n} are: ", end="")
for i in range(1, int(n**0.5)+1):
    if n%i==0:
        print(i, end=" ")
        if i != n//i:
            count=2
            print(n//i, end=" ")
        else:
            count+=1'''

#to print all the factors of a given number
'''n=int(input("Enter a number: "))
print(f"The factors of {n} are: ", end="")
for i in range(1,n+1):
    if n%i==0:
        print(i, end=" ")'''
