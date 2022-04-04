from bnb import branchNbound
from lib import *
from PySimpleGUI import *
from os import getcwd

# membuat interface
def generate_interface():
    # mendapatkan directory saat ini untuk keperluan browse file
    cwd = getcwd()
    theme_background_color = '#8A360F'
    theme_text_color = '#F5F5F5'
    theme_button_color = "#CDAA7D"

    # membuat layout title
    title = [
        [
            Push(background_color=theme_background_color),
            Text('Puzzle Solver', font='Copperplate 35 bold', text_color=theme_text_color, justification ="center", background_color=theme_background_color),
            Push(background_color=theme_background_color),
        ],
        [
            HorizontalSeparator(),
        ]
    ]

    # membuat layout browse file
    browse_puzzle = [
        [
            Push(background_color=theme_background_color),
            # button generate random puzzle
            Button('Generate Puzzle', key="-GENERATE-", size=(14,1),button_color=theme_button_color, font='Copperplate 9 bold'),
            Input(size=(30,1), key="-BROWSE FILE-", enable_events = True, tooltip="Browse for a text file"),
            # browse file
            FileBrowse(file_types=(("Text Files", "*.txt"),), key="-BROWSE-", initial_folder=cwd ,size=(15,1) ,button_color=theme_button_color, font='Copperplate 9 bold'), 
            Push(background_color=theme_background_color),
        ],
    ]

    # membuat layout puzzle info
    puzzle_info = [
        [
            Text(key="-PUZZLE INFO-", font='Copperplate 11', text_color=theme_text_color, background_color=theme_background_color),
            
        ],
        [
            Text(key="-X-", font='Copperplate 11', text_color=theme_text_color, background_color=theme_background_color),
        ],
        [
            Text(key="-LIST KURANG-", font='Copperplate 11', text_color=theme_text_color, background_color=theme_background_color),
        ],
        [
            Text(key="-KURANG-", font='Copperplate 11', text_color=theme_text_color, background_color=theme_background_color),
        ],
        [
            Push(background_color=theme_background_color),
        ],
        [
            Text(key="-MOVE-", font='Copperplate 11', text_color=theme_text_color, background_color=theme_background_color),
        ],
        [
            Text(key="-TOTAL MOVE-", font='Copperplate 11', text_color=theme_text_color, background_color=theme_background_color),
        ],
        [
            Text(key="-VERTICES-", font='Copperplate 11', text_color=theme_text_color, background_color=theme_background_color),
        ],
        [
            Text(key="-TIME-", font='Copperplate 11', text_color=theme_text_color, background_color=theme_background_color),
            Push(background_color=theme_background_color),
            Button("New Game", key="-NEW GAME-", visible=False, size=(12,1),button_color=theme_button_color, font='Copperplate 9 bold'),
        ],
    ]

    # membuat layout button proses
    button_proses = [ 
        [
            Push(background_color=theme_background_color),
        ],
        [
            Push(background_color=theme_background_color),
            # button mencari solusi (belum di visualisasi)
            Button("Find Solution", key="-FIND-", disabled=True, size=(12,1),button_color=theme_button_color, font='Copperplate 9 bold'),
            # button untuk visualisasi puzzle
            Button("Visualize", key="-VISUALIZE-", disabled=True, size=(12,1),button_color=theme_button_color, font='Copperplate 9 bold'),
            Push(background_color=theme_background_color),
        ],
        [
            Push(background_color=theme_background_color),
        ],
        [
            Push(background_color=theme_background_color),
            # slider untuk menentukan kecepatan animasi
            Text("Animation Speed ", font='Copperplate 11', text_color=theme_text_color, background_color=theme_background_color),    
            Slider(key="-SLIDER-", range=(1500,100), default_value=250 ,orientation="h", size=(15,7), disable_number_display=True, disabled=True, background_color=theme_button_color),
            Push(background_color=theme_background_color),
            
        ],
    ]

    Puzzle_Coloum_1 = [
        [Image(key = "-IMAGE1-", filename="./assets/16.png" ,background_color=theme_background_color)],
        [Push(background_color=theme_background_color),],
        [Image(key = "-IMAGE5-", filename="./assets/16.png", background_color=theme_background_color)],
        [Push(background_color=theme_background_color),],
        [Image(key = "-IMAGE9-", filename="./assets/16.png", background_color=theme_background_color)],
        [Push(background_color=theme_background_color),],
        [Image(key = "-IMAGE13-", filename="./assets/16.png", background_color=theme_background_color)],
    ]

    Puzzle_Coloum_2 = [
        [Image(key = "-IMAGE2-", filename="./assets/16.png" ,background_color=theme_background_color)],
        [Push(background_color=theme_background_color),],
        [Image(key = "-IMAGE6-", filename="./assets/16.png", background_color=theme_background_color)],
        [Push(background_color=theme_background_color),],
        [Image(key = "-IMAGE10-", filename="./assets/16.png", background_color=theme_background_color)],
        [Push(background_color=theme_background_color),],
        [Image(key = "-IMAGE14-", filename="./assets/16.png", background_color=theme_background_color)],
    ]

    Puzzle_Coloum_3 = [
        [Image(key = "-IMAGE3-", filename="./assets/16.png" ,background_color=theme_background_color)],
        [Push(background_color=theme_background_color),],
        [Image(key = "-IMAGE7-", filename="./assets/16.png", background_color=theme_background_color)],
        [Push(background_color=theme_background_color),],
        [Image(key = "-IMAGE11-", filename="./assets/16.png", background_color=theme_background_color)],
        [Push(background_color=theme_background_color),],
        [Image(key = "-IMAGE15-", filename="./assets/16.png", background_color=theme_background_color)],
    ]

    Puzzle_Coloum_4 = [
        [Image(key = "-IMAGE4-", filename="./assets/16.png" ,background_color=theme_background_color)],
        [Push(background_color=theme_background_color),],
        [Image(key = "-IMAGE8-", filename="./assets/16.png", background_color=theme_background_color)],
        [Push(background_color=theme_background_color),],
        [Image(key = "-IMAGE12-", filename="./assets/16.png", background_color=theme_background_color)],
        [Push(background_color=theme_background_color),],
        [Image(key = "-IMAGE16-", filename="./assets/16.png", background_color=theme_background_color)],
    ]

    # membuat layout puzzle board
    puzzle_board = [
        [
            Push(background_color=theme_background_color),
            Column(Puzzle_Coloum_1,background_color=theme_background_color),
            Column(Puzzle_Coloum_2,background_color=theme_background_color),
            Column(Puzzle_Coloum_3,background_color=theme_background_color),
            Column(Puzzle_Coloum_4,background_color=theme_background_color),
            Push(background_color=theme_background_color),
        ],
    ]

    # menyatukan semua layout
    Layout = [
        [
            title,
            browse_puzzle,
            puzzle_board,
            button_proses,
            puzzle_info,    
        ],
    ]
    window = Window('Puzzle 15', Layout, background_color=theme_background_color, size=(600,780))
    return window

if __name__ == '__main__':
    window = generate_interface()
    puzzle_board = None
    prog = None
    list_puzzle, total_move, list_move, total_vertice, time, str_list_kurang = [], None, [], None, None, ""
    while True:
        event, value = window.read()
        if event == "EXIT" or event == WIN_CLOSED: # jika keluar dari program
            break
        if event == "-BROWSE FILE-" or event == "-GENERATE-": # jika memilih file puzzle atau mengenerate random puzzle
            try:
                puzzle_board = Puzzle()
                # cek apakah memilih file atau mengenerate puzzle
                if (event == "-GENERATE-"):
                    # membersihkan input browse file
                    window["-BROWSE FILE-"].update("")
                    # generate puzzle
                    puzzle_board.generate_puzzle(randint(10,60))
                else:
                    # membaca file puzzle
                    puzzle_board.read(value["-BROWSE FILE-"], True)

                row = puzzle_board.row
                col = puzzle_board.col

                # visualisasi puzzle awal dari hasil input
                for i in range (row*col):
                    window["-IMAGE"+str(i+1)+"-"].update(filename="./assets/"+str(puzzle_board.buffer[i])+".png")

                # visualisasi informasi awal puzzle, yaitu nilai X, nilai masing-masing kurang(i), dan sigma kurang(i) + X
                window["-PUZZLE INFO-"].update(" Puzzle Info : ")

                window["-X-"].update(" X : " + str(puzzle_board.X))
                
                str_list_kurang += " List Kurang : \n"
                for i in range(puzzle_board.row):
                    for j in range(puzzle_board.col):
                        str_list_kurang += str(" Kurang(%.2d) : " %((i*Puzzle.col+j)+1)) + str("%.2d" %puzzle_board.list_kurang[i*Puzzle.col+j]) + " "
                    if i != puzzle_board.row-1:
                        str_list_kurang += "\n"

                window["-LIST KURANG-"].update(str_list_kurang)
                str_list_kurang = ""
                
                window["-KURANG-"].update(" Sigma(Kurang(i)) + X : " + str(puzzle_board.sigma_kurang))
                window["-FIND-"].update(disabled=False) # tombol find bisa digunakan
            except Exception as e:
                window["-FIND-"].update(disabled=True)

        if event == "-FIND-": # jika menekan tombol find
            try:
                # proses pencarian
                prog = branchNbound(puzzle_board)
                list_puzzle, total_move, list_move, total_vertice, time = prog.solve()
                list_puzzle.reverse()
                window["-VISUALIZE-"].update(disabled=False) # tombol visualisasi bisa digunakan
                window["-SLIDER-"].update(disabled=False) # slide bisa digunakan
            except Exception as e:
                # menampilkan eror yang di raise (iterasi mencapai max atau tidak ada solusi)
                popup(e)

        if event == "-VISUALIZE-": # jika menekan tombol visualize
            animation_speed = value["-SLIDER-"]
            str_move = ""

            # proses visualisasi
            for i, puzzle in enumerate(list_puzzle):
                if (i != len(list_puzzle)-1):
                    # menampilkan move yang diambil
                    window["-MOVE-"].update(" Taken move : " + str(list_move[i].capitalize()))
                for j, element in enumerate(puzzle.buffer):
                    window["-IMAGE"+str(j+1)+"-"].update(filename="./assets/"+str(element)+".png")
                window.read(timeout=animation_speed)

            # menampilkan informasi puzzle setelah di visualisasi, yaitu total move, total vertice, dan waktu yang dibutuhkan
            window["-TOTAL MOVE-"].update(" Total move : " + str(total_move))
            window["-VERTICES-"].update(" Total vertice : " + str(total_vertice))
            window["-TIME-"].update(" Time : %.4f" %time)
            window["-BROWSE-"].update(disabled=True) # tombol find di disable
            window["-GENERATE-"].update(disabled=True) # tombol find di disable
            window["-FIND-"].update(disabled=True) # tombol find di disable
            window["-NEW GAME-"].update(visible=True) # tombol new game muncul

        if event == "-NEW GAME-": # menekan tombol new game
            # mengembalikan ke kondisi awal program
            for i in range(1,16):
                window["-IMAGE"+str(i)+"-"].update(filename="./assets/16.png")
            window["-BROWSE FILE-"].update("")
            window["-PUZZLE INFO-"].update("")
            window["-X-"].update("")
            window["-LIST KURANG-"].update("")
            window["-KURANG-"].update("")
            window["-MOVE-"].update("")
            window["-TOTAL MOVE-"].update("")
            window["-VERTICES-"].update("")
            window["-TIME-"].update("")
            window["-GENERATE-"].update(disabled=False)
            window["-BROWSE-"].update(disabled=False)
            window["-NEW GAME-"].update(visible=False)
            window["-VISUALIZE-"].update(disabled=True)
            puzzle_board = None
            prog = None
            list_puzzle, total_move, list_move, total_vertice, time = [], None, [], None, None
    window.close()
    