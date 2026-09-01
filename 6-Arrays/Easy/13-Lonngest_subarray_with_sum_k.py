class Solution:
    def longestSubarray(self, nums, k):
        prefix_sum = 0
        hsh = {0:-1}
        long = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            v = prefix_sum - k

            if v in hsh:
                length = i - hsh[v]
                long = max(long,length)

            if prefix_sum not in hsh:
                hsh[prefix_sum] = i

        return long
        
p = Solution()
print(p.longestSubarray([10, 5, 2, 7, 1, 9],15))

print(p.longestSubarray([-3, 2, 1],6))
"""

def longest_subarray_with_sum_k(arr, k):
    prefix_sum_map = {0: -1}  # seed: sum=0 occurs at index -1
    running_sum = 0
    longest = 0

    for j in range(len(arr)):
        running_sum += arr[j]
        need = running_sum - k

        if need in prefix_sum_map:
            length = j - prefix_sum_map[need]
            longest = max(longest, length)

        # only store first occurrence — don't overwrite
        if running_sum not in prefix_sum_map:
            prefix_sum_map[running_sum] = j

    return longest

print(longest_subarray_with_sum_k([1, 2, -2, 1],1))"""
