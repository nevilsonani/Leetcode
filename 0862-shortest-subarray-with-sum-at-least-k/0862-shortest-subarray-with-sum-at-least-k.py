from collections import deque
from itertools import accumulate
from math import inf

class Solution:
    def shortest_subarray(self, nums: List[int], k: int) -> int:
        # Calculate the prefix sums of nums with an initial value of 0
        prefix_sums = list(accumulate(nums, initial=0))
        # Initialize a double-ended queue to store indices
        indices_deque = deque()
        # Set the initial answer to infinity, as we are looking for the minimum
        min_length = inf
      
        # Enumerate over the prefix sums to find the shortest subarray
        for current_index, current_sum in enumerate(prefix_sums):
            # If the current_sum minus the sum at the front of the deque is at least k,
            # update the min_length and pop from the deque
            while indices_deque and current_sum - prefix_sums[indices_deque[0]] >= k:
                min_length = min(min_length, current_index - indices_deque.popleft())
            # Remove indices from the back of the deque if their prefix sums are greater 
            # than or equal to current_sum, as they are not useful anymore
            while indices_deque and prefix_sums[indices_deque[-1]] >= current_sum:
                indices_deque.pop()
            # Add the current index to the back of the deque
            indices_deque.append(current_index)
      
        # Return -1 if no such subarray exists, otherwise the length of the shortest subarray
        return -1 if min_length == inf else min_length