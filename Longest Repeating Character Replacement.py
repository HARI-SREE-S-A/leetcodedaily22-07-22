s = "ABAB"
k = 2




l = 0
res = 0
mapp = {}
maxf = 0

for r in range(len(s)):
  mapp[s[r]] = 1+ mapp.get(s[r],0)
  maxf = max(maxf,mapp[s[r]])
  while (r - l +1) - maxf > k:
    map[s[l]] -= 1
    l =+ 1
  res = max(res,r-l+1)
resturn(res)
