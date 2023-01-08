/*
 * @lc app=leetcode id=838 lang=rust
 *
 * [838] Push Dominoes
 */

// @lc code=start
impl Solution {
    pub fn push_dominoes(dominoes: String) -> String {
        let n = dominoes.len();
        let mut rpush = n;
        let mut res = dominoes.chars().collect::<Vec<char>>();
        let (mut l, mut r);

        for (hi, force) in dominoes.chars().enumerate() {
            if force == 'L' {
                if rpush == n {
                    for i in (0..hi).rev() {
                        if res[i] != '.' {
                            break;
                        }
                        res[i] = 'L';
                    }
                } else {
                    l = rpush + 1;
                    r = hi - 1;
                    while l < r {
                        res[l] = 'R';
                        res[r] = 'L';
                        l += 1;
                        r -= 1;
                    }
                    rpush = n;
                }
            } else if force == 'R' {
                if rpush != n {
                    (rpush+1..hi).for_each(|j| {
                        res[j] = 'R';
                    });
                }
                rpush = hi;
            }
        }

        if rpush != n {
            (1+rpush..n).for_each(|j| {
                res[j] = 'R';
            });
        }

        res.into_iter().collect()
    }


}
// @lc code=end

