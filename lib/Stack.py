class Stack:
    def __init__(self, items=None, limit=None):
        self.items = items if items else []
        self.limit = limit

    def push(self, item):
        if self.limit and self.size() >= self.limit:
            raise OverflowError("Stack is full")
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def full(self):
        return self.limit is not None and self.size() >= self.limit

    def search(self, value):
        if value in self.items:
            return self.size() - 1 - self.items.index(value)
        return -1
