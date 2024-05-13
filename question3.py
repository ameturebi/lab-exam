class QueueUsingStacks:
    def __init__(self, capacity):
        self.stack1 = []
        self.stack2 = []
        self.capacity = capacity

    def enqueue(self, value):
        if len(self.stack1) == self.capacity:
            print("Queue is full. Cannot enqueue.")
            return

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(value)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if not self.stack1:
            raise IndexError("Queue is empty. Cannot dequeue.")

        return self.stack1.pop()

    def peek(self):
        if not self.stack1:
            raise IndexError("Queue is empty. Cannot peek.")

        return self.stack1[-1]

    def is_empty(self):
        return not self.stack==
queue = QueueUsingStacks(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Dequeued element:", queue.dequeue())
print("Peek element:", queue.peek())
queue.enqueue(4)
queue.enqueue(5)
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
