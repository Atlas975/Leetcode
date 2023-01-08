/*
 * @lc app=leetcode id=355 lang=rust
 *
 * [355] Design Twitter
 */

// @lc code=start
use std::collections::{HashMap, HashSet, VecDeque, BinaryHeap};

struct User {
    userId: i32,
    tweets: VecDeque<(i32, i32)>,
    follows: HashSet<i32>,
}

struct Twitter {
    timestamp: i32,
    idmap: HashMap<i32, User>,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Twitter {

    fn new() -> Self {
        Twitter {
            timestamp: 0,
            idmap: HashMap::new(),
        }
    }

    fn get_user(&mut self, userId: i32) -> &mut User {
        self.idmap.entry(userId).or_insert(User {
            userId,
            tweets: VecDeque::new(),
            follows: HashSet::new(),
        })
    }

    fn post_tweet(&mut self, user_id: i32, tweet_id: i32) {
        let mut tweets = &mut self.get_user(user_id).tweets;
        tweets.push_front((self.timestamp, tweet_id));
        if tweets.len() > 10 {
            tweets.pop_back();
        }
        self.timestamp -= 1;
    }

    fn get_news_feed(&self, user_id: i32) -> Vec<i32> {

        // let mut mxheap = BinaryHeap::new();
        // for &followee in &self.get_user(user_id).follows {
        //     // get tweet at the end of tweet list
        //     let lstidx = self.get_user(followee).tweets.len() - 1;
        //     if lstidx >= 0 {
        //         let lsttweet = self.get_user(followee).tweets[lstidx];
        //         let (time, tweet) = (lsttweet)
        //     }

        //     let lsttweet = &self.get_user(followee).tweets;

        // }
        // for &followee in self.idmap.get(&user_id).unwrap().follows.iter() {
        //     // check if followee has tweets
        //     let last
        // }
        // // init max heap
        return vec![];

    }

    fn follow(&mut self, follower_id: i32, followee_id: i32) {
        self.get_user(follower_id).follows.insert(followee_id);
    }

    fn unfollow(&mut self, follower_id: i32, followee_id: i32) {
        self.get_user(follower_id).follows.remove(&followee_id);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * let obj = Twitter::new();
 * obj.post_tweet(userId, tweetId);
 * let ret_2: Vec<i32> = obj.get_news_feed(userId);
 * obj.follow(followerId, followeeId);
 * obj.unfollow(followerId, followeeId);
 */
// @lc code=end

