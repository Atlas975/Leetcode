/*
 * @lc app=leetcode id=1465 lang=rust
 *
 * [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
 */

// @lc code=start
impl Solution {
    pub fn max_area(
        h: i32,
        w: i32,
        mut horizontal_cuts: Vec<i32>,
        mut vertical_cuts: Vec<i32>,
    ) -> i32 {
        let max_gap = |cuts: &Vec<i32>, size: i32| {
            let gap = cuts[0].max(size - cuts[cuts.len() - 1]);
            gap.max(cuts.windows(2).fold(gap, |gap, w| gap.max(w[1] - w[0])))
        };
        horizontal_cuts.sort_unstable();
        vertical_cuts.sort_unstable();
        ((max_gap(&horizontal_cuts, h) as i64 * max_gap(&vertical_cuts, w) as i64)
            % (10i64.pow(9) + 7)) as i32
    }
}
// @lc code=end
