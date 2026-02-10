class Solution(object):
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        used = 0
        for c in capacity:
            total_apples -= c
            used += 1
            if total_apples <= 0:
                return used
        return used
