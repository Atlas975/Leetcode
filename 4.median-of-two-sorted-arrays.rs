/*
 * @lc app=leetcode id=4 lang=rust
 *
 * [4] Median of Two Sorted Arrays
 */

use core::cmp::max;
use core::cmp::min;

// @lc code=start
impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        if nums1.len() > nums2.len() {
            return Solution::find_median_sorted_arrays(nums2, nums1);
        }

        let (nhi, nlo) = (nums1.len(), nums2.len());
        let (mut l, mut r) = (0, nlo * 2);
        let (mut m1, mut m2): (usize, usize);
        let (mut l1, mut l2, mut r1, mut r2): (usize, usize, usize, usize);

        while (l <= r) {
            m2 = (l + r) / 2;
            m1 = (nhi + nlo) - m2;
            l1 = if m1 > 0 {
                nums1[(m1 - 1) / 2] as usize
            } else {
                usize::MIN
            };
            r1 = if (m1 < nhi * 2) {
                nums1[m1 / 2] as usize
            } else {
                usize::MAX
            };
            l2 = if m2 > 0 {
                nums2[(m2 - 1) / 2] as usize
            } else {
                usize::MIN
            };
            r2 = if (m2 < nlo * 2) {
                nums2[m2 / 2] as usize
            } else {
                usize::MAX
            };

            if l1 > r2 {
                l = m2 + 1;
            } else if l2 > r1 {
                r = m2 - 1;
            } else {
                return (max(l1, l2) + min(r1, r2)) as f64 / 2.0;
            }
        }
        -1.0
    }
}
// @lc code=end
