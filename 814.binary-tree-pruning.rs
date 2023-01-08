/*
 * @lc app=leetcode id=814 lang=rust
 *
 * [814] Binary Tree Pruning
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
    pub fn prune_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if root.left.is_some() {
            root.left = self.prune_tree(root.left);
        }
        if root.right.is_some() {
            root.right = self.prune_tree(root.right);
        }
        if let Some(node) = root {
            if node.val == 0 && node.left.is_none() && node.right.is_none() {
                return None;
            }
        }

    }
}
// @lc code=end

