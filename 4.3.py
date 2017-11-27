class MyQueue:

    def __init__(self,items):
        self.items = items
        print(self.items)
    def enqueue(self, item):
        return self.items.append(item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self._items)
    def isEmpty(self):
        return self.items == []

a = MyQueue([1,2,3])
a.enqueue(5)
print (a.items)