nums = [-1,0,1,2,-1,-4]
target = 0
b = []
nums = sorted(nums)


for i,n in enumerate(nums):
    if i > 0 and n == nums[i-1]:
        continue
    l = i+1
    r = len(nums)-1

    while l < r:
        summ = nums[i] + nums[l] + nums[r]
        if summ > target:
            r-=1
        elif summ < target:
            l+=1
        else:
            b.append([nums[i],nums[l],nums[r]])
            l+=1
            r-=1
            while l < r and nums[l] == nums[l-1]:
                r-=1
print(b)


