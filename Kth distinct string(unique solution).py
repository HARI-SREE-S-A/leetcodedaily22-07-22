class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = []       #place holder
        x = len(arr)   #length of array
        for i in range(0,x):
            c = arr.count(arr[i]) #counting number of repeating strings
            if c ==1:
                cnt.append(arr[i]) #creating and appending new-list
        l = len(cnt)+1
        if k in range(0,l): # checking with k
            b = cnt[k-1]
            return b
        
        else:
            return("")
        
        
