from copy import deepcopy
from heapq import heappush, heappop
from random import randint

# class priority queue
class PriorityQueue:
    def __init__(self):
        self.elements = [] # inisialisasi awal priority queue
    
    def empty(self):
        return len(self.elements) == 0 # apakah priority queue kosong
    
    def enqueue(self, node):
        heappush(self.elements, node) # menambahkan node ke priority queue
    
    def dequeue(self):
        return heappop(self.elements) # mengambil node paling awal dari priority queue

# class node
class Node:
    count = 0 # inisialisasi awal counter
    step = 1 # inisialisasi awal step untuk keperluan print move
    def __init__(self, parent = None, puzzle = None, depth = None, cost = None, list_move = None):
        self.id = "Node " + str(Node.count) # inisialisasi id node 
        self.parent = parent # inisialisasi parent node (untuk root parent = None)
        self.puzzle = puzzle # inisialisasi puzzle node
        self.depth = depth # inisialisasi depth node
        self.cost = cost # inisialisasi cost node
        self.list_move = list_move # inisialisasi list move node
        Node.count += 1 # menambah counter untuk id
        Node.step = 1 # inisialisasi awal step
    
    # operator overloading kurang dari untuk keperluan priority queue
    def __lt__(self, other):
        return self.cost < other.cost

    # melakukan print info node digunakan ketika debugging
    def printNode(self):
        print("------------------")
        print("ID : ", self.id)
        if (self.parent == None):
            print("ParentID : None")
        else:
            print("ParentID : ", self.parent.id)
        print("Puzzle : ")
        self.puzzle.printPuzzle()
        print("Depth : ", self.depth)
        print("Cost : ", self.cost)
        print("------------------")

    # print semua node lintasan dari akar ke simpul goal
    def printall(self):
        if (self.parent == None):
            self.step = 1
            self.puzzle.printPuzzle()
            return
        self.parent.printall()
        print("Step : ", Node.step, "\nMove : ", self.list_move[Node.step-1].capitalize())
        Node.step += 1
        print()
        print("         ⬇             ")
        print()
        self.puzzle.printPuzzle()
    
    # menyimpan semua node lintasan dari akar ke simpul goal ke dalam list untuk keperluan GUI
    def node_to_list(self):
        list_puzzle = []
        p = self
        while (p != None):
            list_puzzle.append(p.puzzle)
            p = p.parent
        return list_puzzle

# class puzzle
class Puzzle:
    row = 4 # nilai default row puzzle
    col = 4 # nilai default col puzzle
    # nilai default goal
    #  1  2  3  4
    #  5  6  7  8
    #  9 10 11 12
    # 13 14 15 16
    default_goal = [1,2,3,4, 
                     5,6,7,8,
                     9,10,11,12,
                     13,14,15,16]
    def __init__(self, buffer = []):
        self.buffer = buffer # inisialisasi awal buffer puzzle
        self.blank = None # inisialisasi awal posisi kosong
        self.X = None # inisialisasi awal posisi X
        self.list_kurang = [] # inisialisasi awal list nilai fungsi kurang(i)
        self.sigma_kurang = None # inisialisasi jumlah semua nilai kurang(i) puzzle

    # mendapatkan buffer puzzle
    def get(self, i):
        return self.buffer[i]
    
    # mengisi nilai X
    def setX(self, i, j):
        # mengisi nilai posisi kosong
        self.blank = i *Puzzle.col + j
        # apabila i-j-1 adalah genap maka nilai X adalah 1 (bagian yang diarsir)
        if ((i-j-1)%2 == 0):
            self.X = 1
        # apabila i-j-1 adalah ganjil maka nilai X adalah 0 (bagian yang tidak diarsir)
        else:
            self.X = 0

    # mengubah nilai posisi kosong untuk swap
    def setBlank(self, new_pos):
        current_pos = self.blank
        current_elmt = self.buffer[new_pos]
        self.blank = new_pos
        self.buffer[current_pos] = current_elmt
        self.buffer[new_pos] = 16

    # melakukan read file tc
    def read(self, filename, gui = False):
        # jika bukan dibaca melalui GUI, default path adalah test/[filename].txt
        if (gui == False):
            path = '../test/' + filename + '.txt'
        else:
        # jika dibaca melalui GUI
            path = filename
        # check apakah file ada
        try:
            # proses pembaca file
            with open(path, 'r') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    elements = line.split()
                    for j, element in enumerate(elements):
                        self.buffer.append(int(element))
                        if (int(element) == 16):
                            # mengisi nilai X
                            self.setX(i,j)
                # mengisi nilai sigma kurang(i) + X
                self.sigma_kurang = self.kurang()
        except:
            print('Error: Cannot open file')
            raise Exception("File not found")

    # generate puzzle random        
    def generate_puzzle(self, moves = 10):
        # deepcopy default goal ke buffer
        self.buffer = deepcopy(Puzzle.default_goal)
        self.blank = 15

        # menyimpan move yang sudah dilakukan
        list_move = []
        list_move.append(self.blank)
        temp_puzzle = self # menyimpan address self
        
        # melakukan generate puzzle
        while moves > 0:
            swap_list = self.safe_swap()
            ran_num = randint(0,3)
            
            # simpan puzzle pada saat ini
            current_puzzle = deepcopy(self)

            # melakukan swap random dari list swap yang aman
            self.swap(swap_list[ran_num])
            
            i = 0
            # mengecek apakah swap random sudah pernah dilakukan atau belum
            while self.blank in list_move or swap_list[ran_num] == "-":
                # jika sudah dilakukan maka random swap kembali
                if (self.blank in list_move):
                    self = deepcopy(current_puzzle)
                    self.swap(swap_list[ran_num])
                # jika sudah melakukan random hingga 1000 dan selalu swap ke state yang sama maka hentikan loop
                # mencegah infinity loop
                if (swap_list[ran_num] != "-"):
                    if (i < 1000):
                        break
                ran_num = randint(0,3)
                i += 1

            # menyimpan swap yang dilakukan
            list_move.append(self.blank)
            moves -= 1

        # jika hasil random sama dengan goal lakukan random ulang
        if (self.buffer == self.default_goal):
            self.generate_puzzle(moves)

        # mencari kolom dan baris dari posisi kosong
        i, j = int(self.blank/Puzzle.col), self.blank%Puzzle.col

        # mengisi informasi nilai buffer ke address yang sudah disimpan
        temp_puzzle.buffer = self.buffer
        # mengisi nilai X
        temp_puzzle.setX(i,j)
        # mengisi nilai sigma kurang(i) + X
        temp_puzzle.sigma_kurang = temp_puzzle.kurang()

    # mengubah puzzle menjadi string
    def puzzle_to_string(self):
        return str(self.buffer)
                    
    # membuat goal state bisa menggunakan default goal bisa tidak
    def generate_goal(self, final = default_goal):
        self.buffer = final    

    # print semua informasi puzzle
    def printInfo(self):
        print('Puzzle : ')
        # print puzzle
        self.printPuzzle()
        print("Info Puzzle :")
        print("======================================================================")
        # print nilai X
        print('X :', self.X)
        print()
        print("List Kurang(i) : ")
        # print nilai kurang(i) dengan i = 1 -16
        for i in range (Puzzle.row):
            for j in range (Puzzle.col):
                print("Kurang(%.2d) : " %((i*Puzzle.col+j)+1), end="")
                print(str(self.list_kurang[i*Puzzle.col+j]).ljust(2), end = "   ")
            print()
        print()
        # print nilai sigma kurang(i) + X
        print("Sigma(Kurang(i)) + X :", self.sigma_kurang)
        print("======================================================================")

    # print puzzle
    def printPuzzle(self):
        print(" ___________________________")
        for i in range(Puzzle.row):
            print("|      |      |      |      |")
            for j in range(Puzzle.col):
                if (j == 0):
                    print("|", end = "")
                if (self.buffer[i*Puzzle.col + j] == 16):
                    print("     ".ljust(3) + " " , end = "|")
                else:
                    print(str("  %.2d  " %self.buffer[i*Puzzle.col + j]).ljust(3), end='|')
            print()
            print("|______|______|______|______|")

    # mencari nilai sigma kurang(i) + X dan masing-masing nilai kurang(i)
    def kurang(self):
        sum = 0
        temp = 0
        row = Puzzle.row
        col = Puzzle.col
        for i in range(row*col):
            temp = 0
            for j in range (i,row*col):
                if (self.buffer[i] > self.buffer[j]):
                    sum += 1
                    temp += 1
            self.list_kurang.append(temp)
        sum += self.X
        return sum

    # mencari swap yang aman
    def safe_swap(self):
        col = Puzzle.col
        row = Puzzle.row
        pos = self.blank
        # urutan list swap kiri, bawah, kanan, atas
        list_direct = ['-', '-', '-', '-'] 
        if ((pos+1)%col == 0): # swap ke kiri aman
            list_direct[2] = 'left' 
        elif ((pos+1)%col == 1): # swap ke kanan aman
            list_direct[0] = 'right'
        else:   # swap ke kiri dan kanan aman
            list_direct[0] = 'right'
            list_direct[2] = 'left'
        # swap ke bawah aman    
        if ((pos+1) <= row*col - col and pos >= 0):
            list_direct[3] = 'down'
        # swap ke atas aman
        if ((pos+1) > col and pos < row*col):
            list_direct[1] = 'up'
        return list_direct

    # swap puzzle
    def swap(self, direct):
        new_pos = self.blank
        match direct:
            case 'up':
                new_pos -= Puzzle.col
            case 'down':
                new_pos += Puzzle.col
            case 'left':
                new_pos -= 1
            case 'right':
                new_pos += 1
        # set posisi blank baru
        self.setBlank(new_pos)