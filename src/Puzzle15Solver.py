from lib import *
from bnb import *

if __name__ == '__main__':
    succ = False
    puzzle, prog = None, None
    print("######  #     # ####### ####### #       #######      #   #######")    
    print("#     # #     #      #       #  #       #           ##   #      ")  
    print("#     # #     #     #       #   #       #          # #   #      ")
    print("######  #     #    #       #    #       #####        #   ###### ")
    print("#       #     #   #       #     #       #            #         #")
    print("#       #     #  #       #      #       #            #   #     #")
    print("#        #####  ####### ####### ####### #######    #####  ##### ")
    print()
    print("        #####  ####### #       #     # ####### ######             ")  
    print("       #     # #     # #       #     # #       #     #            ")
    print("       #       #     # #       #     # #       #     #            ")
    print("        #####  #     # #       #     # #####   ######             ")
    print("             # #     # #        #   #  #       #   #              ")
    print("       #     # #     # #         # #   #       #    #             ")
    print("        #####  ####### #######    #    ####### #     #            ")                                                                                                   
    while True:
        print("======================================================================")
        # input pilihan menu
        menu = int(input("Choose Input Method\n1. Input Keyboard\n2. Input File\n3. Generate Random\n4. Exit\n>> "))
        match menu:
            case 1: # input keyboard
                buffer = []
                print("Example input : ")
                print("3\t11\t4\t8")
                print("1\t2\t10\t16")
                print("6\t5\t7\t9")
                print("13\t14\t15\t12")
                print("Input Puzzle 15 : ")
                try:
                    c11, c12, c13, c14 = input().split()
                    c21, c22, c23, c24 = input().split()
                    c31, c32, c33, c34 = input().split()
                    c41, c42, c43, c44 = input().split()
                    succ = True
                except:
                    print("Error: Input not valid")
                buffer = [int(c11), int(c12), int(c13), int(c14), 
                          int(c21), int(c22), int(c23), int(c24), 
                          int(c31), int(c32), int(c33), int(c34), 
                          int(c41), int(c42), int(c43), int(c44)]
                puzzle = Puzzle(buffer)          
                for n in range(len(buffer)):
                    if buffer[n] == 16:
                        i, j = int(n/puzzle.col), n%puzzle.col
                        break
                puzzle.setX(i,j)
                puzzle.sigma_kurang = puzzle.kurang()
            case 2: # input file
                puzzle = Puzzle()
                try:
                    puzzle.read(input("Input file name (without .txt) : "))
                    succ = True
                except Exception as e:
                    print(e)
            case 3: # generate random puzzle
                puzzle = Puzzle()
                puzzle.generate_puzzle(randint(10,60))
                succ = True
            case 4: # keluar dari program
                exit()
            case _: # input menu tidak valid
                print("Error: Input not valid")
        # lakukan proses jika input sukses
        if (succ):
            succ = False
            puzzle.printInfo()
            prog = branchNbound(puzzle)
            try:
                prog.solve()
                prog.print_result()
            except Exception as e:
                print(e)
            puzzle, prog = None, None
        print("======================================================================\n")
