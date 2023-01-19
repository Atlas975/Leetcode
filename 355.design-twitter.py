#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
from collections import deque
import heapq as hq


class User:
    __slots__ = ("tweets", "follows")

    def __init__(self, userId):
        self.tweets = deque()
        self.follows = {userId}


class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.idmap = {}
        self.getUser = lambda k: self.idmap.setdefault(k, User(k))

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets = self.getUser(userId).tweets
        tweets.append((self.timestamp, tweetId))
        if len(tweets) > 10:
            tweets.popleft()
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        mxheap = []
        for followeeId in self.getUser(userId).follows:
            if tweets := self.getUser(followeeId).tweets:
                last = len(tweets) - 1
                time, tweetId = tweets[last]
                mxheap.append((-time, tweetId, tweets, last - 1))
        hq.heapify(mxheap)

        feed = []
        while mxheap and len(feed) < 10:
            _, tweetId, tweets, last = hq.heappop(mxheap)
            feed.append(tweetId)
            if last >= 0:
                time, tweetId = tweets[last]
                hq.heappush(mxheap, (-time, tweetId, tweets, last - 1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.getUser(followerId).follows.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.getUser(followerId).follows.discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
