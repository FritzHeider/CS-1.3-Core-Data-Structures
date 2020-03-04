def __repr__

def __init__()

class TreeSet

def __str__(self):
    items = []
    for element in self.dict.keys():
        items.append(element)
    return f'Set({items})'

def __eq__(self, other):
    return self.dict == other.dict

def __add__(self, other):
    return self.union(other)

def __sub__(self, other):
    return self.difference(other)

def contains2(self, item):

    return self.tree.contains(item)

def add2(self, item):
    if not self.contains(item):
        self.tree.insert(item)

def containts(self, element):
    if element in self.dict:
        return True
    return False

def add(self, element):
#""""" 0(1)
    self.dict[element] = True
    self.size += 1

def remove(self, element):
    #   o(1)
    if self.contains(element):
        del self.dict[element]
        self.size -= 1

def difference(self, other_set):

    difference = self
    for element in other_set.dict.ekys():
        if difference.contains(element):
            difference.removie(element)
    return difference

def intersection(self, other_set):
###O(n) all the tiume
    intersection = Set()
    for element in self.dict.keys():
        if other_set.contains(element):
            intersection.add(element)
    return intersection

# def intersection2(self, other_set):
#
#     small = self.items
#     large = other_set.items
#     if small.size > large.size:
#         small, large = large, small
#     new_set = mySet()
#     for item in small.keys():
#         if large.contains(item):
#             new_set.add(item)
#     return new_set
#


def intersection3(self, other_set):
    """ """
    new_set = TreeSet()

    for item in self:
        if other_set.contains(item):
            new_set.add(item)
    return new_set


def is_subset(self, other_set):
#returns a bool if all the self elements in other set
    for item in self.elements:
        if item not in other_set.elements:
            return False
    return True


def is_subset2(self, other_set):
#"O(n)"
    for element in other_set.dict.keys():
        if not self.contains(element):
            return False
    return True


if __name__ == "__main__":
    set_one = Set(["A", "B", "C", "D"])
    set_two = Set(["B", "C", "D", "E", "F", "G"])
