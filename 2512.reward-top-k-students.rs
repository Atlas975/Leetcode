/*
 * @lc app=leetcode id=2512 lang=rust
 *
 * [2512] Reward Top K Students
 */

// @lc code=start
use std::collections::HashSet;

impl Solution {
    pub fn top_students(
        positive_feedback: Vec<String>,
        negative_feedback: Vec<String>,
        report: Vec<String>,
        student_id: Vec<i32>,
        k: i32,
    ) -> Vec<i32> {
        let pos: HashSet<_> = positive_feedback.into_iter().collect();
        let neg: HashSet<_> = negative_feedback.into_iter().collect();
        let mut res: Vec<_> = student_id
            .into_iter()
            .zip(report)
            .map(|(id, report)| {
                let mut points = 0;
                for word in report.split_ascii_whitespace() {
                    if pos.contains(word) {
                        points += 3;
                    } else if neg.contains(word) {
                        points -= 1;
                    }
                }
                (id, points)
            })
            .collect();

        res.sort_unstable_by(|a, b| b.1.cmp(&a.1).then(a.0.cmp(&b.0)));
        res.into_iter().take(k as usize).map(|(id, _)| id).collect()
    }
}
// @lc code=end
