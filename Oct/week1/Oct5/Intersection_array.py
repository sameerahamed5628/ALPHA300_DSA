class Solution(object):
    def intersection(self, nums1, nums2):
        cmn=set()
        for num in nums1:
            if num in nums2:
                cmn.add(num)
        return list(cmn)