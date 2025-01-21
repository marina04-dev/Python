friends = ["a","b","c"]
guests = ["a","L","O","T","I","R","Q","K","b","S"]
sum = 0
for friend in friends:
    if friend in guests:
       sum += 1
       
print(sum)
if sum<2:
    print("I will not come")
else:
    print("I will come")
