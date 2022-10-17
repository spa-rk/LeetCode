class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        k_ticket = tickets[k]
        tot = tickets[k]
        for i in range(k):
            cur = tickets[i]
            if cur <= k_ticket:
                tot += cur
            else:
                tot += k_ticket
        for i in range(k+1, len(tickets)):
            cur = tickets[i]
            if cur <= k_ticket:
                tot += cur
                if cur == k_ticket:
                    tot -= 1
            else:
                tot += k_ticket
                tot -= 1
        return tot