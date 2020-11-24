"""
Candy

Solution
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
"""

# O(N) time and O(2N) space

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        n = len(ratings)
        
        left = [0] * n
        right = [0] * n
        left[0], right[-1] = 1, 1
        
        for i in range(1, n):
            left[i] = left[i-1] + 1 if ratings[i] > ratings[i-1] else 1
        
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] + 1 if ratings[i] > ratings[i+1] else 1
            
        ans = 0
        
        for i in range(n):
            ans += max(left[i], right[i])
        
        return ans


# O(N) time and O(1) space
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        n = len(ratings)
        ans = 1
        up = down = peak = 0
        
        for i in range(1, n):
            # If Ascending
            if ratings[i] > ratings[i-1]:
                up += 1
                peak = up
                down = 0
                ans += 1 + up
                
            # If Descending
            elif ratings[i] < ratings[i-1]:
                down += 1
                up = 0
                ans += 1 + down
                
                # If peak is larger or equal to down, We can reduce 1 from answer that we added with down
                if peak >= down:
                    ans -= 1

            # If Equal
            else:
                up = down = peak = 0
                ans += 1
        
        return ans
