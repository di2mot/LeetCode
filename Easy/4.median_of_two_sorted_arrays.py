'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n3 = nums1 + nums2
        n3.sort()

        l_list = len(n3)

        if l_list % 2 == 0:
            n4 = n3[(l_list//2)-1:(l_list//2)+1]
            return float(sum(n4) / len(n4))
        
        else:
            return float(n3[len(n3) // 2])

        print(n4)
        su = sum(n3)
        res = su / len(n3)
        return res

a = [0, 0]
c = [0, 0]
s = Solution()
b = s.findMedianSortedArrays(a, c)
print(b)

'''
Runtime: 88 ms, faster than 83.03% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.7 MB, less than 24.69% of Python3 online submissions for Median of Two Sorted Arrays.
'''