class CircularBuffer:
    def __init__(self, amount):
        self.amount = amount
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]

    def add(self, item):
        self.items.append(item)
        if len(self.items) > self.amount:
            self.items.pop(0)
        

# buffer = CircularBuffer(3)

# buffer.add('a')
# buffer.add('b')
# buffer.add('c')
# buffer.add('d')
# buffer.add('e')

# print(buffer.items)

# print([buffer[0], buffer[1], buffer[2]])