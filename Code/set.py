from hashtable import HashTable

class HashIterator:

   def __init__(self, hashset):
       self._hashset = hashset
       self._index = 0

   def __next__(self):
       if self._index < (len(self._hashset._keys)) :
           if self._index < len(self._hashset._keys):
               result = (self._hashset._keys[self._index])
           self._index +=1
           return result
       raise StopIteration

class HashSet(object):

    def __init__(self, elements=None):
        self.set = HashTable()
        self.size
        self._keys
        if elements is not None:
            for element in elements:
                self.add(element)
    @property
    def size(self):
        return self.set.size

    @property
    def _keys(self):
        return self.set.keys()

    def __iter__(self):
        return HashIterator(self)

    def contains(self, element):
        return self.set.contains(element)

    def add(self, element):
        self.set.set(element, None)

    def remove(self, element):
        self.set.delete(element)

    def union(self, other_set):
        for element in other_set:
            new_set.add(element)
        return new_set

    def intersection(self, other_set):
        new_set = HashSet()
        for element in self:
            if other_set.contains(element):
                new_set.add(element)
        return new_set

    def difference(self, other_set):
        new_set = HashSet()
        for element in self:
            if not other_set.contains(element):
                new_set.add(element)
        return new_set

    def is_subset(self, other_set):
        for element in self:
            if not other_set.contains(element):
                return False
        return True
