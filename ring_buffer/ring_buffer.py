class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        
    def append(self, item):
        # case 1: list is not full
        if len(self.list) < self.capacity:
            return self.list.append(item)
        # case 2: list is full
        current = 0
        while current < self.capacity:
            self.list.pop()
            self.list[current] = item
            current = current + 1

    def get(self):
        if type(self.list) is not list:
            return []
        return self.list
