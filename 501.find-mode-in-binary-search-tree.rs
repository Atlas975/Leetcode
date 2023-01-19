/*
 * @lc app=leetcode id=501 lang=rust
 *
 * [501] Find Mode in Binary Search Tree
 */

// @lc code=start
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn find_mode(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut ans = vec![];
        let mut max = 0;
        let mut cur = 0;
        let mut cnt = 0;
        let mut dfs = |node: Option<Rc<RefCell<TreeNode>>>| {
            if let Some(node) = node {
                dfs(node.borrow().left.clone());
                if node.borrow().val == cur {
                    cnt += 1;
                } else {
                    cur = node.borrow().val;
                    cnt = 1;
                }
                if cnt > max {
                    max = cnt;
                    ans = vec![cur];
                } else if cnt == max {
                    ans.push(cur);
                }
                dfs(node.borrow().right.clone());
            }
        };
        dfs(root);
        ans

    }
}
// @lc code=end

