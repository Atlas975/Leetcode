/*
 * @lc app=leetcode id=1615 lang=rust
 *
 * [1615] Maximal Network Rank
 */

// @lc code=start
impl Solution {
    pub fn maximal_network_rank(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let degree = roads.iter().fold(vec![0; n as usize], |mut degree, road| {
            degree[road[0] as usize] += 1;
            degree[road[1] as usize] += 1;
            degree
        });

        let (mut fmax, mut smax, mut fmcnt, mut smcnt) = (0, 0, 0, 0);
        for &degree in degree.iter() {
            if degree > fmax {
                smax = fmax;
                fmax = degree;
            } else if degree > smax {
                smax = degree;
            }
        }
        for &degree in degree.iter() {
            if degree == fmax {
                fmcnt += 1;
            } else if degree == smax {
                smcnt += 1;
            }
        }

        if fmcnt >= 2 {
            let edgecnt = roads.iter().fold(0, |acc, road| {
                let (u, v) = (road[0] as usize, road[1] as usize);
                acc + i32::from(degree[u] == fmax && degree[v] == fmax)
            });
            let mxfedge = (fmcnt * (fmcnt - 1)) / 2;
            return 2 * fmax - i32::from(mxfedge == edgecnt);
        }
        let edgecnt = roads.iter().fold(0, |acc, road| {
            let (u, v) = (road[0] as usize, road[1] as usize);
            acc + i32::from(degree[u] == fmax && degree[v] == smax)
                + i32::from(degree[u] == smax && degree[v] == fmax)
        });
        fmax + smax - i32::from(edgecnt == smcnt)
    }
}
// @lc code=end
