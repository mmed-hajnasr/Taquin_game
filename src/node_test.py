import lib.node_class as mine
import unittest


class Test_node(unittest.TestCase):

    def test_basic(self):
        t = mine.node()
        assert (t.depth == 0)

    def test_possible_moves(self):
        # * test if the explores nodes are ignored
        first_node = mine.node()
        first_moves = first_node.next_possible_moves()
        second_moves = first_moves[0].next_possible_moves()
        for node in second_moves:
            self.assertFalse(node.equal(first_node))

    def test_solution(self):
        first_node = mine.node()
        solution = first_node.solution(True)
        self.assertTrue(len(solution) == 4)
        test_node = mine.node()
        assert (test_node.equal(solution[0]))
        test_node.swap(5, 8)
        assert (test_node.equal(solution[1]))
        test_node.swap(8, 7)
        assert (test_node.equal(solution[2]))
        test_node.swap(4, 7)
        assert (test_node.equal(solution[3]))
