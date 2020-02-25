#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes

        self.current = None

        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        """Identifies LinkedList as an iterable type"""
        self.current = self.head
        return self

    def __next__(self):
        """Identifies LinkedList as an iterable type"""
        current = self.current
        if self.current is None:
            raise StopIteration
        self.current = self.current.next
        return current

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""

        result = []
        node = self.head
        while node is not None:
            result.append(node.data)
            node = node.next
        return result
    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: O(n) in every case"""

        count = 0
        #Begin with the head node
        node = self.head
        #Loop untill None which is one past tail....
        while node is not None:
            # Count one for this node
            count += 1
            node = node.next
        #Count equals nodes
        return count

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) where index is 0
        Worst case running time: O(n) where index is n"""
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        for i, node in enumerate(self):
            if i == index:
                return node.data

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) if inserting at front
        Worst case running time: O(n) if inserting at end"""

        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))

        node_new = Node(item)

        if index == 0:
            self.prepend(item)

        else:
            for i, node in enumerate(self):
                if i == index - 1:
                    if node.next is not None:
                        node_new.next = node.next
                    else:
                        self.tail = node_new
                    node.next = node_new

            # Update size after successful insert
            self.size += 1

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1) in all cases"""
        # Create new node
        node_new = Node(item)
        # Check linked list
        if self.is_empty():
            # Set head to new node
            self.head = node_new
        else:
            # Else insert node after tail
            self.tail.next = node_new
        # Update tail
        self.tail = node_new
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: O(1) in all cases"""
        # Create New node
        node_new = Node(item)
        # Check Linked list
        if self.is_empty():
            # Set new tail
            self.tail = node_new
        else:
            # Set head
            node_new.next = self.head
        # Update head
        self.head = node_new
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # set head node
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            node = node.next
        return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: O(1) if item is first node
        Worst case running time: O(n) if last item or not in list because it
            must traverse the whole list"""
        index = -1
        for i, node in enumerate(self):
            if node.data == old_item:
                index = i

        if index < 0:
            raise ValueError

        self.delete(old_item)
        self.insert_at_index(index, new_item)

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if item is at first node
        Worst case running time: O(n) if item is last because must traverse
            list"""
        node = self.head
        left = None
        found = False
        while not found and node is not None:
            if node.data == item:
                found = True
            else:
                left = node
                node = node.next
        if found:
            if node is not self.head and node is not self.tail:
                left.next = node.next
                node.next = None
            if node is self.head:
                self.head = node.next
                node.next = None
            if node is self.tail:
                if left is not None:
                    left.next = None
                self.tail = left

            self.size -= 1

        else:
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
