def ArmValue(input1,input2):
    oddSum=0
    evenSum=0
    for i in input2:
        if(i%2==0):
            evenSum+=i
        else:
            oddSum+=i
    if(oddSum%2==0):
        return evenSum+oddSum
    else:
        return abs(evenSum-oddSum)
    
input1=5
input2= [1,2,3,4,5]
print(ArmValue(input1,input2))