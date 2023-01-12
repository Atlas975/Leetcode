/*
 * @lc app=leetcode id=1855 lang=rust
 *
 * [1855] Maximum Distance Between a Pair of Values
 */

// @lc code=start
impl Solution {
    pub fn max_distance(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let (n1, n2) = (nums1.len(), nums2.len());
        let (mut i, mut j, mut mxdist) = (0, 1, 0);

        while i < n1 && j < n2 {
            if nums1[i] > nums2[j] {
                i += 1;
                j = j.max(1 + i);
            } else {
                mxdist = mxdist.max(j - i);
                j += 1;
            }
        }
        mxdist as i32
    }
}
// @lc code=end

