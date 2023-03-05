/*
 * @lc app=leetcode id=838 lang=rust
 *
 * [838] Push Dominoes
 */

// @lc code=start
impl Solution {
    pub fn push_dominoes(dominoes: String) -> String {
        let (n, mut rpush) = (dominoes.len(), None);
        let mut res = dominoes.chars().collect::<Vec<char>>();

        for (hi, force) in dominoes.chars().enumerate() {
            if force == 'L' {
                match rpush {
                    Some(lo) => {
                        let (mut l, mut r) = (lo + 1, hi - 1);
                        while l < r {
                            res[l] = 'R';
                            res[r] = 'L';
                            l += 1;
                            r -= 1;
                        }
                        rpush = None;
                    },
                    None => {
                        for i in (0..hi).rev() {
                            if res[i] != '.' {
                                break;
                            }
                            res[i] = 'L';
                        }
                    }
                }
            } else if force == 'R' {
                if let Some(rpush) = rpush {
                    for i in (rpush + 1)..hi {
                        res[i] = 'R';
                    }
                }
                rpush = Some(hi);
            }
        }

        if let Some(rpush) = rpush {
            for i in (rpush+1)..n {
                res[i] = 'R';
            }
        }
        res.into_iter().collect()
    }
}
// @lc code=end
