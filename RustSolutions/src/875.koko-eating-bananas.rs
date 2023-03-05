/*
 * @lc app=leetcode id=875 lang=rust
 *
 * [875] Koko Eating Bananas
 */

// @lc code=start
impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut lo = 1;
        let mut hi = *piles.iter().max().unwrap();

        while lo < hi {
            let k = (lo + hi) / 2;
            let time:i32 = piles.iter().map(|&p| (p + k - 1) / k).sum();
            if time > h {
                lo = k + 1;
            } else {
                hi = k;
            }
        }

        return hi;
    }
}
// @lc code=end

