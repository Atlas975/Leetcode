/*
 * @lc app=leetcode id=2446 lang=rust
 *
 * [2446] Determine if Two Events Have Conflict
 */

// @lc code=start
impl Solution {
    pub fn have_conflict(event1: Vec<String>, event2: Vec<String>) -> bool {
        event1[0] <= event2[1] && event1[1] >= event2[0]
    }
    
}
// @lc code=end