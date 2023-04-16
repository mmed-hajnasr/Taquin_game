import copy
from deepdiff import DeepDiff
from bisect import insort_left
from collections import deque


def custom_cmp(obj):
    return obj.defect


class node():
    initial_state = [[1, 2, 3], [8, 6, 0], [7, 5, 4]]
    final_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    explored_states = []

    def __init__(self, depth=0, parent_state=None, mat=copy.deepcopy(initial_state)):
        self.mat = mat
        self.parent_state = parent_state
        self.depth = depth
        diff = DeepDiff(mat, self.final_state)
        if diff == []:
            self.defect = depth
        else:
            self.defect = len(diff['values_changed']) + depth

    @staticmethod
    def initialise():
        node.explored_states = []

    def empty_cell_location(self):
        index = 0
        for row in self.mat:
            for cell in row:
                if cell == 0:
                    return index
                else:
                    index += 1

    def is_final_state(self):
        return DeepDiff(self.mat, self.final_state) == {}

    def show(self):
        print("+---+---+---+\n", end="")
        for row in self.mat:
            print("| ", end="")
            for cell in row:
                if cell == 0:
                    cell = " "
                print(str(cell)+" | ", end="")
            print("\n+---+---+---+\n", end="")

    def swap(self, a, b):
        if ((a == self.empty_cell_location() or b == self.empty_cell_location()) and (abs(a-b) == 3 or (abs(a-b) == 1 and a//3 == b//3))):
            aux = self.mat[a//3][a % 3]
            self.mat[a//3][a % 3] = self.mat[b//3][b % 3]
            self.mat[b//3][b % 3] = aux

    def equal(self, p):
        return DeepDiff(self.mat, p.mat) == {}

    def next_possible_moves(self):
        # * add this node to explored
        self.explored_states.append(self)
        possibilitys = []
        possible_moves = []
        empty_space = self.empty_cell_location()
        if empty_space//3 != 0:
            possible_moves.append(-3)
        if empty_space//3 != 2:
            possible_moves.append(3)
        if empty_space % 3 != 0:
            possible_moves.append(-1)
        if empty_space % 3 != 2:
            possible_moves.append(1)
        # * itirate through all possible moves
        for possible_move in possible_moves:
            aux = node(self.depth+1, self, copy.deepcopy(self.mat))
            aux.swap(empty_space, empty_space+possible_move)
        # *check if this possible move is already explored if yes ignore
            new = True
            for old in self.explored_states:
                if aux.equal(old):
                    new = False
            if new:
                possibilitys.append(aux)
        return possibilitys

    def trace_back(self) -> list:
        if self.parent_state == None:
            l = []
            l.append(self)
            return l
        result = self.parent_state.trace_back()
        result.append(self)
        return result

    def Asolution(self):
        q = []
        insort_left(q, self, key=custom_cmp)
        while len(q) != 0:
            current_node = q[0]
            q.pop(0)
            if current_node.is_final_state():
                return current_node.trace_back(), len(q)
            new_nodes = current_node.next_possible_moves()
            for new_node in new_nodes:
                insort_left(q, new_node, key=custom_cmp)

    def solution(self, A=False, BFS=False, limit=-1):
        if (A):
            return (self.Asolution())
        q = deque()
        found = False
        q.append(self)
        while len(q) != 0:
            current_node = q[-1]
            q.pop()
            if current_node.is_final_state():
                found = True
                break
            if (current_node.depth >= limit and limit != -1):
                continue
            new_nodes = current_node.next_possible_moves()
            for new_node in new_nodes:
                if (BFS):
                    q.appendleft(new_node)
                else:
                    q.append(new_node)
        if found:
            return current_node.trace_back(), len(q)
        else:
            return [], 0
