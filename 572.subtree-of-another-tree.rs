/*
 * @lc app=leetcode id=572 lang=rust
 *
 * [572] Subtree of Another Tree
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
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn is_subtree(
        root: Option<Rc<RefCell<TreeNode>>>,
        sub_root: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        fn preord(node: Option<Rc<RefCell<TreeNode>>>) -> String {
            match node {
                Some(node) => {
                    let node = node.borrow();
                    format!(
                        "({}{}{})",
                        node.val,
                        preord(node.left.clone()),
                        preord(node.right.clone())
                    )
                }
                None => "#".to_owned(),
            }
        }

        let p = preord(root);
        let q = preord(sub_root);
        p.contains(&q)
    }
}
// @lc code=end
