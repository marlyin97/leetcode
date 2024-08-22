class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}
        for index,num in enumerate(nums):
            if num in num_dict:
                if index - num_dict[num] <= k:
                    return True
            num_dict[num] = index
        return False        
                