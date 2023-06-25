height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

l = 0
r = len(height)-1
res = 0
while l < r:
    area = (r-l) * min(height[l],height[r])
    res = max(res,area)
    if height[l] < height[r]:
        l+=1
    else:
        r-=1
print(res)


\\\\\\\\\\\\\\\Brute force////////////////////////



height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


res = 0

for i in range(0,len(height)-1):
    for j in range(i+1,len(height)):
        area = (j-i) * min(height[i],height[j])
        res = max(res,area)
print(res)



