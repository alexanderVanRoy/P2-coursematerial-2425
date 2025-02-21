class Queue:
    def __init__(self):
        self.__items = []
    
    @property
    def items(self):
        return self.__items

    def add(self, item):
        self.items.append(item)
    
    def next(self):
        if len(self.items) != 0:
            return self.items.pop(0)
            
    
    def is_empty(self):
        return len(self.items) == 0

    

# queue = Queue()

# queue.add('Alice')
# queue.add('Bob')
# queue.add('Charlie')

# queue.next()
# queue.next()
# queue.next()

# print(queue.is_empty())


# print(queue.items)
