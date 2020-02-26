#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
#Quick return True if empty
        if self.list.tail is None:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        #> .Size to return items
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) """
        #Prepend
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        #.data read without removal
        if self.is_empty():
            return None
        return self.list.head.data

    def pop(self):

        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(n) """
        #removal
        if self.is_empty():
            raise ValueError
        else:
            top = self.list.head.data
            self.list.delete(top)
            return top
# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        self.top = -1
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if self.top == -1:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        return self.top + 1

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) """
        self.list.append(item)
        self.top += 1

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if self.is_empty():
            return None
        return self.list[self.top]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) """
        if self.is_empty():
            raise ValueError
        else:
            top = self.list[self.top]
            self.list[self.top] = None
            self.top -= 1
            return top

# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
