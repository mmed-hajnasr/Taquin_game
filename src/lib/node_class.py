import copy
from deepdiff import DeepDiff

class node():
    intitial_state = [[1, 2, 3], [8, 6, 0], [7, 5, 4]]
    final_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    explored_states = []

    def __init__(self, depth, parent_state, mat=copy.deepcopy(intitial_state)):
        self.mat = mat
        self.parent_state = parent_state
        self.depth = depth

    def empty_cell_location(self):
        index = 0
        for row in self.mat:
            for cell in row:
                if cell == 0:
                    return index
                else:
                    index += 1

    def is_final_state(self):
        if self.mat == self.final_state:
            return True
        else:
            return False

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
        aux = self.mat[a//3][a % 3]
        self.mat[a//3][a % 3] = self.mat[b//3][b % 3]
        self.mat[b//3][b % 3] = aux

    def equal(self,p):
        return DeepDiff(self.mat,p.mat) == {}

    def next_possible_moves(self):
        possibilitys = []
        possible_moves = []
        empty_space = self.empty_cell_location()
        if empty_space % 3 != 0:
            possible_moves.append(-1)
        if empty_space % 3 != 2:
            possible_moves.append(1)
        if empty_space//3 != 0:
            possible_moves.append(-3)
        if empty_space//3 != 2:
            possible_moves.append(3)
        for possible_move in possible_moves:
            aux = node(self.depth, self, copy.deepcopy(self.mat))
            aux.swap(empty_space, empty_space+possible_move)
            possibilitys.append(aux)
        return possibilitys
