s = "ABAB"
k = 2




l = 0
res = 0
mapp = {}
maxf = 0

for r in range(len(s)):
  mapp[s[r]] = 1+ mapp.get(s[r],0)
  maxf = max(maxf,mapp[s[r]])
  
