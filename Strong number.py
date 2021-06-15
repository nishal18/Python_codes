import math
strong=[]
    
def digfun(n):
    temp=n
    sum=0
    while(n!=0):
        dig=n%10
        sum=sum+math.factorial(dig)
        n=n//10
    if (sum==temp):
        strong.append("yes")
    else:
        strong.append("no")


input_array=[145,375,100,2,10]
for i in (input_array):
    digfun(i)











