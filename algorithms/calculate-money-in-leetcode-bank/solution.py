class Solution(object):
    def totalMoney(self, n):
        total = 0
        for day in range(n):
            week = day // 7
            weekday = day % 7
            money = 1+week +weekday
            total+=money
        return total

