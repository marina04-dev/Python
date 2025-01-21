nums = []
zeroten = []
tentohundred = []
hundredplus = []
while True:
    given_nums = input("Please give a number (0 or end to exit): ")
    if (given_nums != "0" and given_nums != "end"):
        nums.append(given_nums)
    else:
        break
zeroten = [index for index,position in enumerate(given_nums) if int(position)>=1 and int(position)<=10]
tentohundred = [index for index,position in enumerate(given_nums) if int(position)>=11 and int(position)<=100]
hundredplus = [index for index,position in enumerate(given_nums) if int(position)>=101 and int(position)<=1000]
print("")
print(f"There are{len(zeroten)} numbers in the list between 0 and 10.")
for index in zeroten:
    print(f"Value{given_nums[index]} at index {index}")
print(f"There are{len(tentohundred)} numbers in the list between 10 and 100.")
for index in tentohundred:
    print(f"Value{given_nums[index]} at index {index}")
print(f"There are{len(hundredplus)} numbers in the list between 100 and 1000.")
for index in hundredplus:
    print(f"Value{given_nums[index]} at index {index}")

