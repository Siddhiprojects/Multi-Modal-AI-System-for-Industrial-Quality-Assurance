#Functions Recursions
'''def factorial(n):
if (n==0 or n==1):   #base case
return 1
else:
    return n*factorial(n-1)'''

#P1 sum of first n numbers
'''def sum(n):
    if(n == 1): 
        return 1
    else:
        return n + sum(n-1)
num = int(input("enter number"))
print(sum(num))'''
#P2 *** n=3
#   **
#   *
'''def star(n):
    if(n == 1):
        print("*")
    else:
        print("*"*n)
        star(n-1)
num = int(input("enter number"))
star(num)'''
