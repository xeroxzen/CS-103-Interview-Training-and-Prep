def first_missing_positive(nums):
    """
    Given an unsorted integer array nums, 
    find the smallest missing positive integer.

    Follow up: Could you implement an algorithm that runs in 
    O(n) time and uses constant extra space.?

    Constraints:

    0 <= nums.length <= 300
    -231 <= nums[i] <= 231 - 1

    >>> lst_1 = [1, 2, 0]
    >>> first_missing_positive(lst_1) == 3
    True
    >>> lst_2 = [3,4,-1,1]
    >>> first_missing_positive(lst_2) == 2
    True
    >>> lst_3 = [7,8,9,11,12]
    >>> first_missing_positive(lst_3) == 1
    True
    """
    nums.sort()
    missing_positive = -1
    for i in range(1, len(nums)):
        if i not in nums:
            missing_positive = i
            return missing_positive
        # else:
            # return missing_positive
    if missing_positive == -1:
        return nums[-1] + 1
