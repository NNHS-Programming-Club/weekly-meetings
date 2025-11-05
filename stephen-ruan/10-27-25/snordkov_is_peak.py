nums = input().split()
target = input()
output = []
for i in range (len(nums)):
    for j in range (len(nums)):
        if int(nums[i]) + int(nums[j]) == int(target):
            output.append(nums[i])
            output.append(nums[j])
            print(output)
            quit()