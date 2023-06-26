prices = [7,1,5,3,6,4]

res =0
lowest = prioces[0]

for p in prices:
  if p < lowest:
    lowest = p
  res = max(res,(n-lowest))
return res
