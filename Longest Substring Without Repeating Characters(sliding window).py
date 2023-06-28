s = "abcabcbb"
l = 0
sett = set()
res = 0

for r in range(len(s)):
  while s[r] in sett:
    sett.remove(s[l])
    l += 1
  res = max(res,(r-l+1))
  sett.add(res[r])
return res
  
  
