from hashset import HashSet
import unittest

class ElementsMethodsTest(unittest.TestCase):
    def test_size(self):
        assert HashSet().size == 0
        assert HashSet([1, 2, 3, 4]).size == 4
        assert HashSet([1, 2, 3, 4, 1, 2, 3]).size == 4

    def test_iter(self):
        for index, element in enumerate(HashSet()):
            assert index + 1 == element

        for index, element in enumerate(HashSet([1, 2, 3])):
            assert index + 1 == element

    def test_contains(self):
        assert HashSet([1, 2, 3]).contains(1)
        assert not HashSet([1, 2, 3]).contains(5062)
        assert not HashSet().contains(5062)

    def test_add(self):
        new_set = HashSet([])
        assert not new_set.contains(0)
        new_set.add(1)
        assert new_set.contains(1)
        assert not new_set.contains(0)
        assert new_set.size == 1
        new_set.add(3)
        assert new_set.contains(1)
        assert new_set.contains(3)
        assert not new_set.contains(0)
        assert new_set.size == 2
        new_set.add(1)
        assert new_set.contains(1)
        assert new_set.contains(3)
        assert not new_set.contains(0)
        assert new_set.size == 2

    def test_remove(self):
        new_set = HashSet([1, 2, 3, 7, 8])
        assert new_set.contains(1)
        assert new_set.contains(2)
        assert new_set.contains(3)
        assert new_set.contains(7)
        assert new_set.contains(8)
        new_set.remove(3)
        assert new_set.contains(1)
        assert new_set.contains(2)
        assert not new_set.contains(3)
        assert new_set.contains(7)
        assert new_set.contains(8)
        with self.assertRaises(KeyError):
            new_set.remove(4)
        assert new_set.contains(1)
        assert new_set.contains(2)
        assert not new_set.contains(3)
        assert new_set.contains(7)
        assert new_set.contains(8)

class SetsMethodsTest(unittest.TestCase):
    def test_union(self):
        set_a = HashSet([1])
        set_b = HashSet([1, 2, 3])
        set_c = HashSet([2, 3, 4])
        set_d = HashSet()

        ab = set_a.union(set_b)
        ac = set_a.union(set_c)
        ad = set_a.union(set_d)
        bc = set_b.union(set_c)
        bd = set_b.union(set_d)
        cd = set_c.union(set_d)

        assert ab.contains(1)
        assert ab.contains(2)
        assert ab.contains(3)
        assert not ab.contains(4)
        assert not ab.contains(0)
        assert ab.size == 3

        assert ac.contains(1)
        assert ac.contains(2)
        assert ac.contains(3)
        assert ac.contains(4)
        assert not ac.contains(0)
        assert ac.size == 4

        assert ad.contains(1)
        assert not ad.contains(2)
        assert not ad.contains(3)
        assert not ad.contains(4)
        assert not ad.contains(0)
        assert ad.size == 1

        assert bc.contains(1)
        assert bc.contains(2)
        assert bc.contains(3)
        assert bc.contains(4)
        assert not bc.contains(0)
        assert bc.size == 4

        assert bd.contains(1)
        assert bd.contains(2)
        assert bd.contains(3)
        assert not bd.contains(4)
        assert not bd.contains(0)
        assert bd.size == 3

        assert not cd.contains(1)
        assert cd.contains(2)
        assert cd.contains(3)
        assert cd.contains(4)
        assert not cd.contains(0)
        assert cd.size == 3


    def test_intersection(self):
        set_a = HashSet([1])
        set_b = HashSet([1, 2, 3])
        set_c = HashSet([2, 3, 4])
        set_d = HashSet()

        ab = set_a.intersection(set_b)
        ac = set_a.intersection(set_c)
        ad = set_a.intersection(set_d)
        bc = set_b.intersection(set_c)
        bd = set_b.intersection(set_d)
        cd = set_c.intersection(set_d)

        assert ab.contains(1)
        assert not ab.contains(2)
        assert not ab.contains(3)
        assert not ab.contains(4)
        assert not ab.contains(0)
        assert ab.size == 1

        assert not ac.contains(1)
        assert not ac.contains(2)
        assert not ac.contains(3)
        assert not ac.contains(4)
        assert not ac.contains(0)
        assert ac.size == 0

        assert not ad.contains(1)
        assert not ad.contains(2)
        assert not ad.contains(3)
        assert not ad.contains(4)
        assert not ad.contains(0)
        assert ad.size == 0

        assert not bc.contains(1)
        assert bc.contains(2)
        assert bc.contains(3)
        assert not bc.contains(4)
        assert not bc.contains(0)
        assert bc.size == 2

        assert not bd.contains(1)
        assert not bd.contains(2)
        assert not bd.contains(3)
        assert not bd.contains(4)
        assert not bd.contains(0)
        assert bd.size == 0

        assert not cd.contains(1)
        assert not cd.contains(2)
        assert not cd.contains(3)
        assert not cd.contains(4)
        assert not cd.contains(0)
        assert cd.size == 0

    def test_difference(self):
        set_a = HashSet([1])
        set_b = HashSet([1, 2, 3])
        set_d = HashSet()

        ab = set_a.difference(set_b)
        ad = set_a.difference(set_d)
        bd = set_b.difference(set_d)
        ba = set_b.difference(set_a)
        da = set_d.difference(set_a)
        db = set_d.difference(set_b)

        assert not ab.contains(1)
        assert not ab.contains(2)
        assert not ab.contains(3)
        assert not ab.contains(4)
        assert not ab.contains(0)
        assert ab.size == 0

        assert ad.contains(1)
        assert not ad.contains(2)
        assert not ad.contains(3)
        assert not ad.contains(4)
        assert not ad.contains(0)
        assert ad.size == 1

        assert bd.contains(1)
        assert bd.contains(2)
        assert bd.contains(3)
        assert not bd.contains(4)
        assert not bd.contains(0)
        assert bd.size == 3

        assert not ba.contains(1)
        assert ba.contains(2)
        assert ba.contains(3)
        assert not ba.contains(4)
        assert not ba.contains(0)
        assert ba.size == 2

        assert not da.contains(1)
        assert not da.contains(2)
        assert not da.contains(3)
        assert not da.contains(4)
        assert not da.contains(0)
        assert da.size == 0

        assert not db.contains(1)
        assert not db.contains(2)
        assert not db.contains(3)
        assert not db.contains(4)
        assert not db.contains(0)
        assert db.size == 0

    def test_is_subset(self):
        set_a = HashSet([1])
        set_b = HashSet([1, 2, 3])
        set_d = HashSet()

        assert set_a.is_subset(set_b)
        assert not set_a.is_subset(set_d)
        assert not set_b.is_subset(set_d)
        assert not set_b.is_subset(set_a)
        assert set_d.is_subset(set_a)
        assert set_d.is_subset(set_b)

if __name__ == '__main__':
    unittest.main()
