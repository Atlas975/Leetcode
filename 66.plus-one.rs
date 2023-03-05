/*
 * @lc app=leetcode id=66 lang=rust
 *
 * [66] Plus One
 */

// @lc code=start
impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        for dig in digits.iter_mut().rev() {
            if *dig < 9 {
                *dig += 1;
                return digits;
            }
            *dig = 0;
        }
        digits.insert(0, 1);
        digits
    }

}
// @lc code=end

