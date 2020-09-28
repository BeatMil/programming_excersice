import random
array=list(range(10,20))
evennum=[x for x in array if x%2==0]
oddnum=[x for x in array if x%2!=0]
print('odd number is: ',oddnum)
print('even number is: ',evennum)
print('oddcount: ',len(oddnum))
print('evencount: ',len(oddnum))
num=random.randint(1,10)