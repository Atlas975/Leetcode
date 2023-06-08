#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#


# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = total // k
        
        if total % k != 0:
            return False
        subset = [0] * k
        nums.sort()

        def dfs(i):
            if i == -1:
                return all(s == target for s in subset)
            
            for j in range(k):
                subset[j] += nums[i]
                if subset[j] <= target and dfs(i - 1):
                    return True
                subset[j] -= nums[i]
                if subset[j] == 0: # no need to try other empty subsets
                    break
            return False

        return dfs(len(nums) - 1)


# @lc code=end
