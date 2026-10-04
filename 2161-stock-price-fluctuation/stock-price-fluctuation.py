from collections import defaultdict
import heapq

class StockPrice:

    '''
    General approach:

    store a seperate heap for the min and maxes respectively
    can't do scalar updates, because if we happen to update a timestamp
    corresponding to the max or min, previous/other prices can now become the new min/max

    The latest price can just be timestamped without concern

    We can lazy update via a dictionary that stores the most recent values
    for each timestamp
    '''

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.latest = (0, 0)

        #dict storing most recent prices per timestamps
        self.most_recent_prices = {}
    
    def update(self, timestamp: int, price: int) -> None:

        if timestamp >= self.latest[0]:
            self.latest = (timestamp, price)

        heapq.heappush(self.minheap, (price, timestamp))
        heapq.heappush(self.maxheap, (-price, timestamp))

        self.most_recent_prices[timestamp] = price

    def current(self) -> int:
        return self.latest[1]
        
    def maximum(self) -> int:

        #go through the heap extracting the max value while removing any stale entries
        while len(self.maxheap) > 0:
            #pop most recent value and check if stale 

            #the price stored is negative so need to reverse
            price, time = heapq.heappop(self.maxheap)
            if -price == self.most_recent_prices[time]:
                heapq.heappush(self.maxheap, (price, time))
                return -price

    def minimum(self) -> int:

        #same as the max heap
        while len(self.minheap) > 0:
            #pop most recent value and check if stale 
            price, time = heapq.heappop(self.minheap)
            if price == self.most_recent_prices[time]:
                heapq.heappush(self.minheap, (price, time))
                return price
        

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()