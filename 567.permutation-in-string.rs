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

        let get_idx = |c: u8| (c - b'a') as usize;
        let cnt1 = s1.bytes().fold([0u8; 26], |mut acc, c| {
            acc[get_idx(c)] += 1;
            acc
        });

        let s2bytes = s2.as_bytes();
        let mut cnt2 = s2bytes[0..n1].iter().fold([0u8; 26], |mut acc, &c| {
            acc[get_idx(c)] += 1;
            acc
        });
        let mut matches = (0..26).filter(|&i| cnt1[i] == cnt2[i]).count();

        for i in n1..n2 {
            if matches == 26 {
                return true;
            }

            let (l, r) = (get_idx(s2bytes[i - n1]), get_idx(s2bytes[i]));

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

