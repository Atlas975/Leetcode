/*
 * @lc app=leetcode id=746 lang=rust
 *
 * [746] Min Cost Climbing Stairs
 */

// @lc code=start
impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let (mut a, mut b) = (cost[0], cost[1]);
        for c in cost[2..].into_iter() {
            let tmp = a.min(b);
            a = b;
            b = tmp + c;
        }
        a.min(b)
    }
}
// @lc code=end

