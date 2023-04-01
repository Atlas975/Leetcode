/*
 * @lc app=leetcode id=567 lang=rust
 *
 * [567] Permutation in String
 */

// @lc code=start
impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let (n1, n2) = (s1.len(), s2.len());
        if n1 > n2 {
            return false;
        }

        let getidx = |c: u8| (c - b'a') as usize;
        let (s1bytes, s2bytes) = (s1.as_bytes(), s2.as_bytes());
        let (mut cnt1, mut cnt2) = ([0u8; 26], [0u8; 26]);
        for (&c1, &c2) in s1bytes.iter().zip(s2bytes.iter()) {
            cnt1[getidx(c1)] += 1;
            cnt2[getidx(c2)] += 1;
        }

        let mut matches = cnt1
            .iter()
            .zip(cnt2.iter())
            .filter(|(&a, &b)| a == b)
            .count();

        for i in n1..n2 {
            if matches == 26 {
                return true;
            }

            let (l, r) = (getidx(s2bytes[i - n1]), getidx(s2bytes[i]));

            cnt2[r] += 1;
            if cnt1[r] == cnt2[r] {
                matches += 1;
            } else if cnt1[r] + 1 == cnt2[r] {
                matches -= 1;
            }

            cnt2[l] -= 1;
            if cnt1[l] == cnt2[l] {
                matches += 1;
            } else if cnt1[l] - 1 == cnt2[l] {
                matches -= 1;
            }
        }

        matches == 26
    }
}
// @lc code=end
