#Kayden Scheer
#Data Structures Lab 2
#09/04/2026

#1.1
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek()) #30 (top item)
print(s.pop()) #30
print(s.pop()) #20
print(s.pop()) #10
print(s.isEmpty()) #True
print()


#1.2
class Stack:
    """ A Last-In, First-Out (LIFO) data structure. 
    
    The 'top' of the stack is the end of the internal list.
    All operations are O(1)
    """

    def __init__(self):
        """ Create a new, empty stack. """
        self.items = []

    def push(self, item):
        """ Add a new item to the top of the stack. """
        self.items.append(item)

    def pop(self):
        """ Remove and return the top item
        
        Raise an IndexError if the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """ Return the top item from the stack without removing it.
        
        Raise an IndexError if the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def isEmpty(self):
        """ Return True if the stack is empty, False otherwise. """
        return len(self.items) == 0

    def size(self):
        """ Return the number of items in the stack. """
        return len(self.items)

    def clear(self):
        """Remove all items from the stack."""
        self.items = []

    def to_list(self):
        """Return a copy of the internal list (bottom to top)."""
        return list(self.items)

    def __len__(self):
        """Support len(stack)."""
        return self.size()

    def __bool__(self):
        """Support if stack: (truthy when non-empty)."""
        return not self.is_empty()

    def __str__(self):
        """Human-readable: Stack(bottom -> ... -> top)."""
        return 'Stack(' + ' -> '.join(str(x) for x in self.items) + ')'

    def __repr__(self):
        """Developer-readable."""
        return f'Stack({self.items})'

    def __contains__(self, item):
        """Support: if item in stack."""
        return item in self.items

    def __iter__(self):
        """Iterate from top to bottom (LIFO order)."""
        return reversed(self.items)


#2.1
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue("Alice")
q.enqueue("Bob")
q.enqueue("Charlie")
print(q.dequeue()) #Alice (first in)
print(q.dequeue()) #Bob (second in)
print(q.dequeue()) #Charlie (third in)
print(q.isEmpty()) #True
print()

#2.2
class Queue:
    """ A First-In, First-Out (FIFO) data structure. 
    
    enqueue at the rear (right), dequeue from the front (left).
    WARNING: dequeue is O(n) because list.pop(0) shifts elements
    """

    def __init__(self):
        """ Create a new, empty queue. """
        self.items = []

    def enqueue(self, item):
        """ Add a new item to the end of the queue. """
        self.items.append(item)

    def dequeue(self):
        """ Remove and return the front item"""
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def front(self):
        """ Return the front item from the queue without removing O(1)."""
        if self.isEmpty():
            raise IndexError("front from empty queue")
        return self.items[0]

    def isEmpty(self):
        """ Return True if the queue is empty, False otherwise. """
        return len(self.items) == 0

    def size(self):
        """ Return the number of items in the queue. """
        return len(self.items)

    def clear(self):
        """Remove all items from the queue."""
        self.items = []

    def to_list(self):
        """Return a copy of the internal list (front to back)."""
        return list(self.items)

    def __len__(self):
        """Support len(queue)."""
        return self.size()

    def __bool__(self):
        """Support if queue: (truthy when non-empty)."""
        return not self.isEmpty()

    def __str__(self):
        """Human-readable: Queue(front -> ... -> back)."""
        return 'Queue(' + ' -> '.join(str(x) for x in self.items) + ')'

    def __repr__(self):
        """Developer-readable."""
        return f'Queue({self.items})'

    def __contains__(self, item):
        """Support: if item in queue."""
        return item in self.items

    def __iter__(self):
        """Iterate from front to back (FIFO order)."""
        return iter(self.items)