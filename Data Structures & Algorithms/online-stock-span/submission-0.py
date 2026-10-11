class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        res = 1
        for i in range(len(self.prices) - 1, -1, -1):
            if self.prices and self.prices[i] <= price:
                res += 1
            else:
                break
        self.prices.append(price)
        return res
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)