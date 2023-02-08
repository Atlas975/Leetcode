/*
 * @lc app=leetcode id=2064 lang=rust
 *
 * [2064] Minimized Maximum of Products Distributed to Any Store
 */

// @lc code=start
impl Solution {
    fn minimized_maximum(n: i32, quantities: Vec<i32>) -> i32 {
        let (mut l, mut r) = (1, 1_000_000_000);

        while l < r {
            let mid = (l + r) / 2;
            let sum = quantities
                .iter()
                .fold(0, |acc, &x| acc + (x + mid - 1) / mid);
            if sum <= n {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        l
    }
}
// @lc code=end
