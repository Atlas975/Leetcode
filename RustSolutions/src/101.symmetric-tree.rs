/*
 * @lc app=leetcode id=101 lang=rust
 *
 * [101] Symmetric Tree
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
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {

    }

    pub fn check_symmetry(left: Option<Rc<RefCell<TreeNode>>>, right: Option<Rc<RefCell<TreeNode>>>) -> bool {

        if None == left || None == right {
            return true;
        }
        match (left, right) {
            (None, None) => true,
            (Some(l), Some(r)) => {
                let (l, r) = (l.borrow(), r.borrow());
                l.val == r.val && Self::check_symmetry(l.left.clone(), r.right.clone()) && Self::check_symmetry(l.right.clone(), r.left.clone())
            },
            _ => false
        }
    }
}
// @lc code=end

