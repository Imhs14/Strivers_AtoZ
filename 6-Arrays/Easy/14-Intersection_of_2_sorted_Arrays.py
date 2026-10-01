class Solution:
    def intersectionArray(self, nums1, nums2):
        i,j = 0,0
        intersect = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersect.append(nums1[i])
                i,j = i +  1, j + 1
            else:
                if nums1[i] > nums2[j]:
                    j += 1
                else:
                    i += 1
        return intersect

s = Solution()
print(s.intersectionArray([1, 2, 2, 3, 5], [1, 2, 7]))
print(s.intersectionArray([1, 2, 2, 3, 3, 3],[2, 3, 3, 4, 5, 7]))