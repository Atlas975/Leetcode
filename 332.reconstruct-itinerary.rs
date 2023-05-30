/*
 * @lc app=leetcode id=332 lang=rust
 *
 * [332] Reconstruct Itinerary
 */

// @lc code=start
use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap, VecDeque};


impl Solution {
    pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
        let mut graph = HashMap::new();
    
        for (u, v) in tickets.iter().map(|v| (v[0].to_owned(), v[1].to_owned())) {
            graph.entry(u).or_insert(BinaryHeap::new()).push(Reverse(v));
        }
    
        fn dfs(
            graph: &mut HashMap<String, BinaryHeap<Reverse<String>>>,
            node: &str,
            route: &mut VecDeque<String>,
        ) {
            while let Some(next) = graph.get_mut(node).and_then(|dests| dests.pop()) {
                dfs(graph, &next.0, route);
            }
            route.push_front(node.to_string());
        }
    
        let mut route = VecDeque::new();
        dfs(&mut graph, "JFK", &mut route);
        route.into()
    }
}
// @lc code=end
 