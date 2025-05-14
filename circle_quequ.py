class CircularQueue:
    def __init__(self, size):
        self.queue = [None]*size
        self.max_size = size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear+1) % self.max_size == self.front:
            print("Queue is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear+1) % self.max_size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            return None
        elif self.front == self.rear:
            val = self.queue[self.front]
            self.front = self.rear = -1
            return val
        else:
            val = self.queue[self.front]
            self.front = (self.front+1) % self.max_size
            return val
