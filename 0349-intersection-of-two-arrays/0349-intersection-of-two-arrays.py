from collections import Counter

class Solution(object):
    def intersection(self, nums1, nums2):
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        return list((cnt1&cnt2).keys())
        