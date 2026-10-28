from collections import deque
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        # dictionary to keep the canonical version of each token and its expiry time
        # We can either keep a min heap, or queue,
        #Q must be ordered because time is monotonic. 
        self.toks = {}
        self.q = deque() 

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.toks[tokenId] = currentTime + self.ttl
        self.q.append((tokenId, currentTime + self.ttl))

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.toks: return
        # just update the dictionary, no need to filter from queue yet
        if self.toks[tokenId] > currentTime:
            self.toks[tokenId] = currentTime + self.ttl
            self.q.append((tokenId, currentTime + self.ttl))

    def countUnexpiredTokens(self, currentTime: int) -> int:
        # O(1) amortized
        while self.q:
            tokid, t = self.q[0]
            if t <= currentTime:
                self.q.popleft()
                if t == self.toks[tokid]:
                    del self.toks[tokid]
            else: break

        # you literally already have a canonical list of active tokens!
        return len(self.toks.keys())


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)