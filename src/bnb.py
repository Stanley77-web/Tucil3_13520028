from copy import deepcopy
from lib import PriorityQueue, Node, Puzzle
from time import time

# class algoritma BnB
class branchNbound:
    def __init__(self, puzzle = Puzzle()):
        self.puzzle = puzzle # simpan state awal puzzle
        self.goal = Puzzle() # simpan state goal
        self.goal.generate_goal() # mengenerate goal
        self.pq = PriorityQueue() # definisi awal priority queue
        self.leaf = None # definisi awal leaf (simpul yang diambil)
        self.table_node = {} # definisi awal hash tabel untuk menyimpan node
        self.result = None # definisi awal result (simpul goal)
        self.time = 0 # definisi awal waktu untuk menyimpan waktu proses
    
    # algoritma BnB
    def solve(self):
        # check apakah puzzle dapat diselesaikan
        if (self.puzzle.sigma_kurang%2 != 0):
            # jika sigma kurang ganjil puzzle tidak dapat diselesaikan, raise error
            raise Exception("\nCan't solve puzzle")
        print("Searching for solution...")
        # menyimpan waktu mulai proses
        start = time()
        # membangkitkan simpul akar
        initial = self.puzzle
        final = self.goal
        root_node = Node(None, initial, 0, self.calculateCost(initial, final), [])
        # menambahkan simpul akar ke priority queue
        self.pq.enqueue(root_node)
        # insialisasi jumlah iterasi
        iterasi = 0
        while (not self.pq.empty()):  
            if (iterasi < 1000000):
                # mengambil simpul pada queue paling awal
                minimumNode = self.pq.dequeue()
                # leaf adalah simpul yang sedang diproses saat ini
                self.leaf = minimumNode
                self.puzzle = self.leaf.puzzle
                # check apakah puzzle sudah mencapai goal
                if (self.is_final(self.puzzle)):
                    # menyimpan waktu akhir proses
                    end = time()
                    # jika mencapai goal prunning leaf yang memiliki cost lebih besar cost saat ini
                    self.prunning(minimumNode.cost)
                    # simpul goal adalah simpul yang sedang diproses saat ini
                    self.result = self.leaf
                    break
                else:
                    # mengecek proses pergeseran yang aman
                    swap_list = self.puzzle.safe_swap()
                    # simpan puzzle pada simpul yang sedang diproses
                    current_puzzle = self.puzzle
                    # mengambil semua swap yang aman
                    for move in swap_list:
                        if (move != '-'):
                            self.puzzle = deepcopy(current_puzzle)
                            # lakukan swap terhadap puzzle
                            self.puzzle.swap(move)
                            # tambahan informasi yang diperlukan node seperti parent, depth, dan list_move
                            new_depth = minimumNode.depth + 1 # f(i)
                            new_cost = self.calculateCost(self.puzzle, final) + new_depth # c(i) = f(i) + g(i)
                            new_move = minimumNode.list_move + [move] 
                            new_node = Node(minimumNode, self.puzzle, new_depth, new_cost, new_move)
                            # mengecek apakah simpul yang sedang diproses sudah ada di hash tabel node                            
                            str_new_puzzle = self.puzzle.puzzle_to_string()
                            if (str_new_puzzle not in self.table_node):
                                # jika belum ada di hash tabel node, maka tambahkan simpul tersebut ke hash tabel node dan priority queue
                                self.pq.enqueue(new_node)
                                self.table_node.update({str_new_puzzle:(new_node.id)})                           
                    iterasi += 1
            else:
                # jika iterasi melebihi batas maksimal, raise error
                raise Exception("\nReach max iteration")

        # menyimpan semua informasi hasil yang diperlukan (untuk keperluan GUI)
        self.time = end - start
        list_puzzle =  self.result.node_to_list()
        list_move = self.result.list_move
        total_vertice = len(self.table_node)
        total_move = self.result.depth
        return list_puzzle, total_move, list_move, total_vertice, self.time

    # menghitung taksiran cost g(i)
    def calculateCost(self, puzzle, goal):
        cost = 0
        for i in range(len(puzzle.buffer)):
            # jika ubin tidak sama dengan posisinya pada goal cost akan ditambahkan
            if (puzzle.get(i) != goal.get(i) and puzzle.get(i) != 16):
                cost += 1
        return cost

    # melakukan pemotongan terhadap node yang memiliki cost lebih besar dari cost saat ini
    def prunning(self, current_best):
        temp = PriorityQueue()
        for i in range(len(self.pq.elements)):
            if (self.pq.elements[i].cost <= current_best):
                temp.enqueue(self.pq.elements[i])
        self.pq = temp
    
    # mengecek apakah puzzle sudah mencapai goal
    def is_final(self, new_puzzle):
        # jika buffer puzzle sama dengan buffer goal maka puzzle sudah mencapai goal
        return new_puzzle.buffer == self.goal.buffer
    
    # melakukan print hasil
    def print_result(self):
        print("\n\nCompletion Step : ")
        # print semua node lintasan dari akar ke simpul goal
        self.result.printall()
        print("Total move :", self.result.depth, "step")
        print("All moves : ", end="")
        for i, move in enumerate(self.result.list_move):
            print(move.capitalize(), end="")
            if (i != len(self.result.list_move) - 1):
                print(", ", end="")
        print()
        print("Total vertices raised : ", len(self.table_node))
        print("Completion time : %.4f second" %(self.time)) 
    
