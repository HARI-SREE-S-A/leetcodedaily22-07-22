nums = [100,4,200,1,3,2,5,6]
num = sorted(nums)
b = []
for n in num:
    if n-1 not in num:
        current_n = n
        current_seq = [current_n]
        while current_n + 1 in num:
            current_n += 1
            current_seq.append(current_n)
        if len(b) < len(current_seq):
            b = current_seq
print(b)
