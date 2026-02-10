class MyCalendarTwo(object):

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, start, end):
        # If this interval overlaps with an already double-booked interval → reject
        for s, e in self.overlaps:
            if not (end <= s or start >= e):
                return False

        # Record new overlaps with all single-booked intervals
        for s, e in self.booked:
            if not (end <= s or start >= e):
                self.overlaps.append((max(start, s), min(end, e)))

        # Insert into booked list
        self.booked.append((start, end))
        return True
