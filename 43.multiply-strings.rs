/*
 * @lc app=leetcode id=43 lang=rust
 *
 * [43] Multiply Strings
 */

// @lc code=start
impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        let mut digits = vec![0; num1.len() + num2.len()];

        for (k, sum) in num1
            .bytes()
            .rev()
            .map(|b| b - b'0')
            .enumerate()
            .filter(|(_, n)| *n != 0)
            .flat_map(|(i, n1)| {
                num2.bytes()
                    .rev()
                    .map(|b| b - b'0')
                    .enumerate()
                    .map(move |(j, n2)| (i + j, n1 * n2))
            })
        {
            digits[k] += sum;
            digits[k + 1] += digits[k] / 10;
            digits[k] %= 10;
        }

        let digits = digits
            .into_iter()
            .rev()
            .skip_while(|&n| n == 0)
            .map(|b| (b'0' + b) as char)
            .collect::<String>();
        if digits.is_empty() {
            "0".to_string()
        } else {
            digits
        }
    }
}
// @lc code=end
