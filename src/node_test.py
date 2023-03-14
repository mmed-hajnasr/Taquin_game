import lib.node_class as mine
import unittest

class Test_node(unittest.TestCase):
    def test_basic(self):
        t=mine.node(5,None)
        assert(t.depth==5)