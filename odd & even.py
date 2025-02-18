a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
odd=[]
even=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even:",even)
print("Odd",odd)