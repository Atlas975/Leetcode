/*
 * @lc app=leetcode id=842 lang=rust
 *
 * [842] Split Array into Fibonacci Sequence
 */

// @lc code=start
use std::i32;

impl Solution {
    pub fn split_into_fibonacci(num: String) -> Vec<i32> {
        let mx = i32::MAX;
        let mut dp = vec!

        for i in 0..num.len() {
            let mut cur = vec![0; num.len()];
            let (mut split, mut dm) = (0, -1);

            for j in (0..i+1).rev() {
                if j == i {
                    cur[j] = 1;
                } else if num[j] == '0' {
                    cur[j] = 0;
                } else {
                    let mut a = num[j..i+1].parse::<i32>().unwrap();
                    if a > mx {
                        cur[j] = 0;
                    } else {
                        cur[j] = dp[i+1][j+1];
                        if cur[j] == 1 {
                            split = 1;
                            dm = j as i32;
                        }
                    }
                }
            }
        }




    }
}
// @lc code=end

