class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0
        merged = [0] * (len(nums1) + len(nums2))
        
        while True:
            if i == len(nums1):
                while j < len(nums2):
                    merged[i + j] = nums2[j]
                    j += 1
                break
            elif j == len(nums2):
                while i < len(nums1):
                    merged[i + j] = nums1[i]
                    i += 1
                break
            elif nums1[i] < nums2[j]:
                merged[i + j] = nums1[i]
                i += 1
            else:
                merged[i + j] = nums2[j]
                j += 1
        
        if len(merged) % 2 == 0:
            return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2.0
        else:
            return merged[len(merged) // 2]