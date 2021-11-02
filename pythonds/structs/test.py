import unittest
import binheap

a = binheap.BinHeap()
a.insert(3)
a.insert(5)
a.insert(7)
a.insert(2)
print(a.currentSize)
print(a.heapList)
