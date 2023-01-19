/*
 * @lc app=leetcode id=355 lang=rust
 *
 * [355] Design Twitter
 */

// @lc code=start
use std::collections::{HashMap, HashSet, VecDeque, BinaryHeap};

struct User {
    pub user_id: i32,
    pub tweets: VecDeque<(i32, i32)>,
    pub follows: HashSet<i32>,
}

struct Twitter {
    timestamp: i32,
    idmap: HashMap<i32, User>,
}


impl Twitter {

    fn new() -> Self {
        Twitter {
            timestamp: 0,
            idmap: HashMap::new(),
        }
    }

    fn get_user(&mut self, user_id: i32) -> &mut User {
        self.idmap.entry(user_id).or_insert(User {
            user_id,
            tweets: VecDeque::new(),
            follows: HashSet::from([user_id]),
        })
    }

    fn post_tweet(&mut self, user_id: i32, tweet_id: i32) {
        let curtime = self.timestamp;
        let tweets = &mut self.get_user(user_id).tweets;
        tweets.push_back((curtime, tweet_id));
        if tweets.len() > 10 {
            tweets.pop_front();
        }
        self.timestamp += 1;
    }

    fn get_news_feed(&mut self, user_id: i32) -> Vec<i32> {
        let mut mxheap = BinaryHeap::new();

        let follows = match self.idmap.get(&user_id) {
            Some(user) => &user.follows,
            None => return vec![],
        };

        for followee in follows {
            if let Some(user) = self.idmap.get(followee) {
                let last = user.tweets.len() - 1;
                let (time, tweet_id) = user.tweets[last];
                mxheap.push((time, tweet_id, &user.tweets, last));
            }
        }

        let mut feed = vec![];
        while !mxheap.is_empty() && feed.len() < 10 {
            let (_, tweet_id, tweets, idx) = mxheap.pop().unwrap();
            feed.push(tweet_id);
            if let Some(&(time, tweet_id)) = tweets.get(idx - 1) {
                mxheap.push((time, tweet_id, tweets, idx - 1));
            }
        }

        feed
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

