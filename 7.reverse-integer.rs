/*
 * @lc app=leetcode id=7 lang=rust
 *
 * [7] Reverse Integer
 */

// @lc code=start
impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let sign: i64 = if x < 0 { -1 } else { 1 };
        let mut x: i64 = (x as i64) * sign;
        let mut res: i64 = 0;
        while x > 0 {
            res *= 10;
            res += x % 10;
            x /= 10;
        }
        if res > i32::MAX as i64 {
            return 0;
        }
        (res * sign) as i32
    }

}
// @lc code=end

