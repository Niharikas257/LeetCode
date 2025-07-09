class Twitter:

    def __init__(self):
        self.count = 0
        self.followmap = defaultdict(set)
        self.tweetmap = defaultdict(list)     
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        self.count -= 1        

    def getNewsFeed(self, userId: int) -> List[int]:
        # res = []
        # minheap = []

        # self.followmap[userId].add(userId)
        # for followeeId in self.followmap[userId]:
        #     if followeeId in self.tweetmap:
        #         index = len(self.tweetmap[followeeId])-1
        #         count, tweetId = self.tweetmap[followeeId][index]
        #         heapq.heappush(minheap, [count, tweetId, followeeId, index-1])

        # while minheap and len(res) < 10:
        #     count, tweetId, followeeId, index = heapq.heappop(minheap)
        #     res.append(tweetId)
        #     if index >= 0:
        #         count, tweetId = self.tweetmap[followeeId][index]
        #         heapq.heappush(minheap, [count, tweetId, followeeId, index - 1])
        # return res
        res = []
        minheap = []

        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]: # for the followee in the user's follow list, if that followee ID is in tweetmap, means that person has tweeted in the past
            if followeeId in self.tweetmap:
                index = len(self.tweetmap[followeeId])-1
                count, tweetId = self.tweetmap[followeeId][index] # we want the count and tweetID of the followee's tweet from the tweetmap at a particular index inside the particular followee tweets list.
                heapq.heappush(minheap, [count, tweetId, followeeId, index-1]) # index -1  becuase we are pushing the 2nd latest tweet of the followee.
        heapq.heapify(minheap)
        while minheap and len(res) < 10: 
            # until we have elements in the min heap and until we not have 10 tweets for the newsfeed, we will keep on repeating the loop.
            count, tweetId, followeeId, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0: # while we still have the tweets from a particular person/followee
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index-1])
        return res
             


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)