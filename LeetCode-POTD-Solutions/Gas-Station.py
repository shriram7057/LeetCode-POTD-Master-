class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total = 0
        tank = 0
        start = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0:
                tank = 0
                start = i + 1
        
        return start if total >= 0 else -1
