/*
 * @lc app=leetcode id=7 lang=rust
 *
 * [7] Reverse Integer
 */

// @lc code=start
impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let sign = 1 - (x < 0) as i64 * 2;
        let mut x = (x as i64) * sign;
        let mut res = 0;
        while x > 0 {
            res *= 10;
            res += x % 10;
            x /= 10;
        }
        if res <= i32::MAX as i64 { (res * sign) as i32 } else { 0 }
    }


}
// @lc code=end

