/*
 * @lc app=leetcode id=43 lang=rust
 *
 * [43] Multiply Strings
 */

// @lc code=start
impl Solution {
    pub fn multiply(num1: String, num2: String) -> String {
        if num1 == "0" || num2 == "0" {
            "0".to_owned()
        } else {
            num1.bytes()
                .rev()
                .map(|b| b - b'0')
                .enumerate()
                .filter(|(_, n)| *n != 0)
                .flat_map(|(i, n1)| {
                    num2.bytes()
                        .rev()
                        .enumerate()
                        .map(move |(j, n2)| (i + j, n1 * (n2 - b'0')))
                })
                .fold(vec![0; num1.len() + num2.len()], |mut digits, (k, sum)| {
                    digits[k] += sum;
                    digits[k + 1] += digits[k] / 10;
                    digits[k] %= 10;
                    digits
                })
                .into_iter()
                .rev()
                .skip_while(|&n| n == 0)
                .map(|b| (b'0' + b) as char)
                .collect()
        }
    }
}
// @lc code=end
    