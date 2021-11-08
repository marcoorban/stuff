import unittest
import binheap

class TestHeap(unittest.TestCase):

    def setUp(self):
        self.heap = binheap.BinHeap()

    def test_insert_one(self):
        self.heap.insert(3)
        self.assertEqual(self.heap.heapList, [0, 3])

    def test_insert_many(self):
        self.heap.insert(3)
        self.heap.insert(1)
        self.heap.insert(2)
        self.heap.insert(5)
        self.assertEqual(self.heap.heapList, [0,1,3,2,5])
        self.assertEqual(self.heap.currentSize, 4)

    def test_delMin(self):
        self.heap.insert(3)
        self.heap.insert(1)
        self.heap.insert(2)
        self.heap.insert(5)
        min = self.heap.delMin()
        self.assertEqual(min, 1)
        self.assertEqual(self.heap.heapList, [0,2,3,5])    

if __name__ == "__main__":
    unittest.main()