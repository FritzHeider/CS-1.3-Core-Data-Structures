#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
"""Return True if this queue is empty, or False otherwise."""
#Quick check true if empty
        if self.list.head is None:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
#.size for numbers
        return self.list.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1)"""
        #append
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – because it takes constant time to delete from the
        front of a linked list"""
        if self.is_empty():
            raise ValueError
        else:
            front = self.list.head.data
            self.list.delete(front)
            return front

# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        self.start = -1
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if self.start == -1:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        return self.start + 1

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(n) - because each item in an array must be individually
        shifted when prepending"""
        self.list.insert(0, item)
        self.start += 1

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list[self.start]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – because nothing gets moved or traversed, this takes
        constant time"""
        if self.is_empty():
            raise ValueError
        else:
            front = self.list[self.start]
            self.list[self.start] = None
            self.start -= 1
            return front

# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = LinkedQueue
