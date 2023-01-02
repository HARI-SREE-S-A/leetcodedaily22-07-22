s = "pwwkew"
k = list(s)
mapp={}
i,l,r = 0,0,0
maxx = 0
x = []
for i in range(len(s)):
    if k[i] in mapp:
        print(k[i])
        mapp[i].append(s[i])
    else:
        mapp[i] = s.count(s[i])
for y in  mapp.values() :
    if y>1:
        x.append(y)
    
        
        
        
        
        
print(x)
       
