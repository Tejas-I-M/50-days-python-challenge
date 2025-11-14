"""
Day 04 - Two Sum
"""

from typing import List, Tuple, Optional

def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    
    seen = {}

   
    for i, val in enumerate(nums):
        
        need = target - val

        
        if need in seen:
            return (seen[need], i)

       
        seen[val] = i

    
    return None
