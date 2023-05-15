/*
 * @lc app=leetcode id=1110 lang=rust
 *
 * [1110] Delete Nodes And Return Forest
 */

// @lc code=start
// Definition for a binary tree node.
use std::{
    cell::RefCell,
    collections::{HashSet, VecDeque},
    rc::Rc,
};

// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }

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

impl Solution {
    pub fn del_nodes(
        root: Option<Rc<RefCell<TreeNode>>>,
        to_delete: Vec<i32>,
    ) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        let mut res = vec![root.clone()];
        let to_delete = to_delete.into_iter().collect::<HashSet<i32>>();
        let mut q = VecDeque::new();

        let root_val = root.as_ref().unwrap().borrow().val;
        q.push_back((root, true, to_delete.contains(&root_val)));

        while let Some((node, is_root, marked)) = q.pop_front() {
            if is_root && !marked {
                res.push(node.clone());
            }
            let mut parent = node.as_ref().unwrap().borrow_mut();

            if let Some(left) = parent.left.take() {
                let is_deleted = to_delete.contains(&left.borrow().val);
                q.push_back((Some(left), marked, is_deleted));
                if is_deleted {
                    parent.left = None;
                }
            }
            if let Some(right) = parent.right.take() {
                let is_deleted = to_delete.contains(&right.borrow().val);
                q.push_back((Some(right), marked, is_deleted));
                if is_deleted {
                    parent.right = None;
                }
            }
        }
        res
    }
}
// @lc code=end
