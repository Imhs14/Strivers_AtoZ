class Solution:
    def unionArray(self, nums1, nums2):
        i, j = 0, 0
        N = []

        def add(val):
            if not N or N[-1] != val:
                N.append(val)

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                add(nums1[i])
                i += 1
            else:
                add(nums2[j])
                j += 1

        while i < len(nums1):
            add(nums1[i])
            i += 1

        while j < len(nums2):
            add(nums2[j])
            j += 1

        return N

p = Solution()
print(p.unionArray([-3, -1, 2],[-2, 0]))

print(p.unionArray([3, 4, 6, 7, 9, 9],[1, 5, 7, 8, 8]))

print(p.unionArray([1, 2, 3, 4, 5],[1, 2, 7]))

print(p.unionArray([-2, 3],[3]))


"""
i,j = 0,0
N = []
while i < len(nums1) and j < len(nums2):

    if nums1[i] < nums2[j]:
        N.append(nums1[i])
        i += 1
    else:
        N.append(nums2[j])
        j += 1

    while i < len(nums1) and nums1[i] == N[-1]:
        i += 1
    while j < len(nums2) and nums2[j] == N[-1]:
        j += 1

while i < len(nums1):
    if nums1[i] != N[-1]:
        N.append(nums1[i])
    i += 1

while j < len(nums2):
    if nums2[j] != N[-1]:
        N.append(nums2[j])
    j += 1
return N
"""