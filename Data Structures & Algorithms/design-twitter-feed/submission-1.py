class Tweet:
    def __init__(self, time, tweetId, nextTweet=None):
        self.time = time
        self.id = tweetId
        self.next = nextTweet

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        tweet = Tweet(
            self.time,
            tweetId,
            self.tweets.get(userId)
        )

        self.tweets[userId] = tweet

        self.following[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for followee in self.following[userId]:

            if followee in self.tweets:
                tweet = self.tweets[followee]

                heapq.heappush(
                    heap,
                    (-tweet.time, tweet.id, tweet)
                )
        
        result = []

        while heap and len(result) < 10:
            _, tweetId, tweet = heapq.heappop(heap)
            result.append(tweetId)

            if tweet.next:
                heapq.heappush(
                    heap,
                    (-tweet.next.time, tweet.next.id, tweet.next)
                )

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
