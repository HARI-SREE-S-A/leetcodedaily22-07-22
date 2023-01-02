s = "pwwkew"
k = list(s)
mapp={}
i,l,r = 0,0,0
maxx = 0
x = []
for i in range(len(s)):
    if k[i] not in mapp:
        mapp[s[i]] = s.count(s[i])
        print(k[i])
       
       
for y in  mapp.values() :
    if y>1:
        x.append(y)
    
        
