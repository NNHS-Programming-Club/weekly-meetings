def get_target(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            target = nums[i] + nums[j]
            return [i,j]
            