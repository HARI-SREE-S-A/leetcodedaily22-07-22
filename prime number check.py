number = 11
counter = 0
for i in range(2,number+1):
    if number%i == 0:
        counter += 1
        print(counter)
if counter == 1:
    print("y")
else:
    print("n")
