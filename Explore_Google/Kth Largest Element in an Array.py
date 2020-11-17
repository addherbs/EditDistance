"""
Kth Largest Element in an Array

Solution
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappush, heappop
        
        heap = []
        
        for elem in nums:
            if len(heap) < k:
                heappush(heap, elem)
            else:
                val = heappop(heap)
                if elem > val:
                    heappush(heap, elem)
                else:
                    heappush(heap, val)
                    
        return heappop(heap)

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            start_index = left
            
            for i in range(left, right):
                if pivot > nums[i]:
                    nums[i], nums[start_index] = nums[start_index], nums[i]
                    start_index += 1
            
            nums[right], nums[start_index] = nums[start_index], nums[right]
            return start_index
        
        def selection_algorithm(left, right, k_smallest):
            if left == right:
                return nums[left]
            
            pivot_index = partition(left, right, k_smallest)
            if pivot_index == k_smallest:
                return nums[pivot_index]
            if k_smallest < pivot_index:
                return selection_algorithm(left, pivot_index - 1, k_smallest)
            else:
                return selection_algorithm(pivot_index + 1, right, k_smallest)
        
        return selection_algorithm(0, len(nums) - 1, len(nums) - k)