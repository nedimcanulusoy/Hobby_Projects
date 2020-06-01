import random

num_range=[]

x=int(input('Type for first range: '))
y=int(input('Type for second range: '))

for nums in range(x,y+1):
    num_range.append(nums)

for rand_num in random.sample(num_range,1):
    print('Your random number is: ',rand_num)
