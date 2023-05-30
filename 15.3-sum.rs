/*
 * @lc app=leetcode id=15 lang=rust
 *
 * [15] 3Sum
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort_unstable();
        let mut res = vec![];
        let n = nums.len();

        let mut first_idx = HashMap::new(); // get the first index of each val
        for (i, &num) in nums.iter().take(n - 2).enumerate() {
            first_idx.entry(num).or_insert(i);
        }

        for (cur, l) in first_idx {
            let (mut m, mut r) = (l + 1, n - 1);
            while m < r {
                let s = cur + nums[m] + nums[r];
                if s < 0 {
                    m += 1;
                } else if s > 0 {
                    r -= 1;
                } else {
                    res.push(vec![cur, nums[m], nums[r]]);
                    m += 1;
                    while nums[m] == nums[m - 1] && m < r {
                        m += 1;
                    }
                }
            }
        }
        res
    }
}
// @lc code=end
