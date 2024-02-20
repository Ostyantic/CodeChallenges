# Given an array of integers (nums) and an integer (target), return indices of the two numbers such
# that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    if not nums:
        return "empty list"

    dupe = nums

    for i1, num1 in enumerate(nums):
        for i2, num2 in enumerate(dupe):
            if i1 == i2:
                continue
            if num1 + num2 == target:
                # print([i1, i2])
                return [i1, i2]

    # for i1 in range(len(nums)):
    #     for i2, num in enumerate(nums):
    #         if i1 == i2:
    #             continue
    #         if nums[i1] + num == target:
    #             print([i1, i2])
    #             return [i1, i2]
