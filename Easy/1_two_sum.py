class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = 0
        for i in nums:
            for x in range(n+1, len(nums)):
                if i + nums[x] == target:
                    return n, x
            n += 1
a = [3,2,4]
b = 6

c = Solution
print(c.twoSum(a, b))