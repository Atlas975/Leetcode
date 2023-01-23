/*
 * @lc app=leetcode id=33 lang=rust
 *
 * [33] Search in Rotated Sorted Array
 */

// @lc code=start
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        fn bin_search(nums: &Vec<i32>, l: usize, r: usize, target: i32) -> i32 {
            if l > r {
                return -1;
            }
            let m = l + (r - l) / 2;
            let mid = nums[m];

            if target == mid {
                return m as i32;
            }
            if nums[l] <= mid {
                if target > mid || target < nums[l] {
                    return bin_search(nums, m + 1, r, target);
                }
                return bin_search(nums, l, m - 1, target);
            }
            if target < mid || target > nums[r] {
                return bin_search(nums, l, m - 1, target);
            }
            bin_search(nums, m + 1, r, target)
        }
        bin_search(&nums, 0, nums.len() - 1, target)
    }
}
// @lc code=end

