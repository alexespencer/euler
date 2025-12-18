coins = [1, 2, 5, 10, 20, 50, 100, 200]

def total(coin_counts):
    return sum([k * v for k, v in coin_counts.items()])

def count_combos_slow(goal):
    unique_combos = set()

    coin_counts = {p: 0 for p in coins}

    max_counts = [goal // p for p in coins]

    for p1 in range(max_counts[0] + 1):
        coin_counts[1] = p1
        for p2 in range(max_counts[1] + 1):#
            coin_counts[2] = p2
            for p5 in range(max_counts[2] + 1):
                coin_counts[5] = p5
                for p10 in range(max_counts[3] + 1):
                    coin_counts[10] = p10
                    for p20 in range(max_counts[4] + 1):
                        coin_counts[20] = p20
                        for p50 in range(max_counts[5] + 1):
                            coin_counts[50] = p50
                            for p100 in range(max_counts[6] + 1):
                                coin_counts[100] = p100
                                for p200 in range(max_counts[7] + 1):
                                    coin_counts[200] = p200
                                    if total(coin_counts) == goal:
                                        unique_combos.add(tuple(sorted(coin_counts.items())))

    return(len(unique_combos)), unique_combos

for goal in coins[0:5]:
    count, unique_combos = count_combos_slow(goal)
    print(goal, count)

class CoinCounter():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    def __init__(self, goal):
        self.ways = [0] * (goal + 1)
        self.ways[0] = 1

        for coin in self.coins:
            for i in range(coin, (goal + 1)):
                self.ways[i] += self.ways[i - coin]

    def count(self, n, mod=None):
        if mod:
            return self.ways[n] % mod
        return self.ways[n]

cc = CoinCounter(10**5)

for i in coins[0:5]:
    assert cc.count(i) == count_combos_slow(i)[0]

print(cc.count(10**5, 10**9 + 7))

print(cc.count(10, 10**9 + 7))
print(cc.count(15, 10**9 + 7))
print(cc.count(20, 10**9 + 7))
print(cc.count(200, 10**9 + 7))