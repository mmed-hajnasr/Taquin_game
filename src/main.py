import tkinter as tk
from time import sleep
from tkinter import messagebox
import copy
from lib.node_class import node
from playsound import playsound
# *variables
moves = 0
free_mode = True
search_option = -2
player_node = node()
SETTING_ICON = None
ind = 0
# -search_option==-2 mean DFS
# -search_option==-1 mean BFS
# -search_option>0 mean DFL

# *methods


def play():
    playsound('src/Undertale - Megalovania.mp3',block=False)


def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()


def start_game(event=None):
    global free_mode
    free_mode = True
    global moves
    moves = 0
    global player_node
    player_node = node()
    player_node.mat = copy.deepcopy(node.initial_state)
    node.initialise()
    clear_window(window)
    window.configure(bg='black')
    # *title section
    title_frame = tk.Frame(master=window, bg="black", height=50, width=500)
    title = tk.Label(master=title_frame, text="Play on your own or use DFS/BFS to find the solution",
                     bg="black", fg="purple", font=("Arial", 12, 'bold'))
    title.place(anchor=tk.W, rely=0.5, relx=0.03)
    global SETTING_ICON
    SETTING_ICON = tk.PhotoImage(file="img/settings.png")
    SETTING_ICON = SETTING_ICON.subsample(20)
    settings_button = tk.Button(title_frame, image=SETTING_ICON, bg="black")
    settings_button.place(x=460, y=10)
    settings_button.bind('<Button>', open_settings)
    # * grid section
    grid_frame = tk.Frame(master=window, bg="black", height=300, width=300)
    make_grid(grid_frame, player_node.mat)
    # * options section
    option_frame = tk.Frame(master=window, bg="black", height=50, width=500)
    game_buttons(option_frame)
    # * final layout
    title_frame.pack()
    grid_frame.pack()
    option_frame.pack(pady=5)


def open_settings(event):
    def submit(event):
        if v.get() == 0:
            try:
                result = int(input.get())
                assert (result > 0)
            except:
                input_warning.set("you need to type a positive number")
                return
            v.set(result)
        global search_option
        search_option = v.get()
        start_game()
    clear_window(window)
    v = tk.IntVar()
    global search_option
    if search_option > 0:
        v.set(0)
    else:
        v.set(search_option)  # initializing the choice
    input_warning = tk.StringVar()
    input_warning.set("")
    window.configure(bg='#d9d9d9')

    tk.Label(window, font=("Arial", 21),
             text="Choose the search algorithm:",
             justify=tk.LEFT,
             padx=20).pack()

    tk.Radiobutton(window, font=("Arial", 21), text="DFS", padx=20,
                   variable=v, value=-2).pack()
    tk.Radiobutton(window, font=("Arial", 21), text="heuristique", padx=20,
                   variable=v, value=-3).pack()
    tk.Radiobutton(window, font=("Arial", 21), text="BFS", padx=20,
                   variable=v, value=-1).pack()
    tk.Radiobutton(window, font=("Arial", 21), text="DFL", padx=20,
                   variable=v, value=0).pack()
    bt = tk.Button(text="apply", font=("Arial", 21))
    other = tk.Frame()
    tk.Label(other, font=("Arial", 21), text="DFL's Limit:").grid(row=0)
    input = tk.Entry(other, font=("Arial", 21), width=5)
    input.grid(row=0, column=1)
    other.pack()
    tk.Label(window, font=("Arial", 21), fg="red",
             textvariable=input_warning).pack()
    bt.pack()
    bt.bind('<Button>', submit)


def make_grid(frame, mat):
    global moves

    def switch_cell(event):
        global moves
        if not free_mode:
            return
        if isinstance(event.widget, tk.Label):
            info = event.widget.master.grid_info()
        else:
            info = event.widget.grid_info()
        i = info["row"]
        j = info["column"]
        index = i*3+j
        b = player_node.empty_cell_location()
        if (abs(index-b) == 3 or (abs(index-b) == 1 and index//3 == b//3)):
            player_node.swap(b, index)
            moves += 1
            if player_node.is_final_state():
                victory_screen()
                return
            make_grid(frame, player_node.mat)
    clear_window(frame)
    i = 0
    j = 0
    for row in mat:
        for cell in row:
            grid_cell = tk.Frame(master=frame, height=80,
                                 width=80, bg="purple")
            grid_cell.bind("<Button-1>", switch_cell)
            grid_cell.grid(row=i, column=j, padx=10, pady=10)
            if cell != 0:
                cell_label = tk.Label(master=grid_cell, text=str(cell), bg="purple", font=(
                    "Arial", 30))
                cell_label.bind("<Button-1>", switch_cell)
                cell_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            else:
                grid_cell.destroy()
            j += 1
        i += 1
        j = 0


def victory_screen():
    clear_window(window)
    initial_node = node()
    initial_node.mat = copy.deepcopy(node.initial_state)
    solution, nb = initial_node.solution(BFS=True)
    optimal_moves = len(solution)-1
    if moves == optimal_moves:
        victory_statement = "you played perfectly \n you found the solution in " + \
            str(moves)+" moves!!!"
    else:
        victory_statement = "you found the solution in " + \
            str(moves)+" moves,\n you could've done better honestly.\n it's not a compitition but I did it in " + \
            str(optimal_moves)+" moves."
    tk.Label(window, text=victory_statement, bg="black", fg="purple",
             font=("Arial", 20)).place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    tk.Button(window, text="RESTART", fg="purple", font=("Arial", 10, "bold"),
              command=start_game).place(relx=0.5, rely=0.75, anchor=tk.CENTER)


def game_buttons(frame):
    clear_window(frame)
    restart_button = tk.Button(frame, text="restart", bg="purple")
    restart_button.grid(
        row=0, column=0, padx=10)
    edit_start = tk.Button(frame, text="edit start", bg="purple")
    edit_start.grid(row=0, column=1, padx=10)
    edit_end = tk.Button(frame, text="edit end", bg="purple")
    edit_end.grid(row=0, column=2, padx=10)
    solution = tk.Button(frame, text="solution", bg="purple")
    solution.grid(row=0, column=3, padx=10)
    restart_button.bind("<Button>", start_game)
    edit_end.bind("<Button>", lambda event: input_grid(end=True))
    edit_start.bind("<Button>", lambda event: input_grid(end=False))
    solution.bind("<Button>", lambda event: solution_screen())


def is_mat_valid(mat) -> bool:
    ref = set()
    for i in range(9):
        ref.add(i)
    for row in mat:
        for cell in row:
            if cell in ref:
                ref.remove(cell)
            elif cell >= 0 and cell < 9:
                messagebox.showerror(
                    'Error', "please don't use the same digit more than ounce")
                return False
            else:
                messagebox.showerror(
                    'Error', 'please use only digits from 0 to 8.\n'+str(cell)+" is not acceptable.")
                return False
    return True


def input_grid(end: bool):
    clear_window(window)

    def submit():
        mat = []
        for row in raw_mat:
            new_treated_row = []
            for cell in row:
                try:
                    if cell.get() == "":
                        new_treated_row.append(0)
                    else:
                        new_treated_row.append(int(cell.get()))
                except:
                    messagebox.showerror(
                        'Error', 'please use only digits from 0 to 8.\n'+str(cell.get())+" is not acceptable.")
                    return
            mat.append(new_treated_row)
        if is_mat_valid(mat):
            if end:
                node.final_state = copy.deepcopy(mat)
            else:
                node.initial_state = copy.deepcopy(mat)
            start_game()
    title_frame = tk.Frame(master=window, bg="black", height=50, width=500)
    title = tk.Label(master=title_frame, text="you can leave the designated empty cell empty or write 0",
                     bg="black", fg="purple", font=("Arial", 12, 'bold'))
    title.place(anchor=tk.W, rely=0.5)
    grid_frame = tk.Frame(window, bg="black")
    raw_mat = []
    for i in range(3):
        new_row = []
        for j in range(3):
            raw_cell = tk.StringVar()
            grid_cell = tk.Frame(grid_frame, height=80,
                                 width=80, bg="purple")
            grid_cell.grid(row=i, column=j, padx=10, pady=10)
            cell_input = tk.Entry(
                grid_cell, textvariable=raw_cell, font=("Arial", 30), bg="purple")
            cell_input.place(width=30, relx=0.5, rely=0.5, anchor=tk.CENTER)
            new_row.append(raw_cell)
        raw_mat.append(new_row)
    title_frame.pack()
    grid_frame.pack()
    tk.Button(window, text="SUBMIT", fg="purple", font=("Arial", 20, "bold"),
              command=submit).pack(pady=5)


def solution_screen():
    # -preprocess
    global free_mode
    free_mode = False
    limit = -1
    if search_option > 0:
        limit = search_option
    initial_node = node()
    solution, nb = initial_node.solution(
        BFS=(search_option == -1), A=(search_option == -3), limit=limit)
    nbr_explored = len(initial_node.explored_states)
    nbr_itrations = nbr_explored+nb
    global ind
    ind = 0

    def cycle():
        global ind
        ind = 0
        make_grid(grid_frame, solution[ind].mat)
        window.update()
        while (ind < len(solution)-1):
            sleep(3)
            add()
            window.update()

    def add():
        global ind
        ind = min(ind+1, len(solution)-1)
        make_grid(grid_frame, solution[ind].mat)

    def sub():
        global ind
        ind = max(0, ind-1)
        make_grid(grid_frame, solution[ind].mat)
    if solution == []:
        messagebox.showerror(
            'Error', "the solution was not found you propably set the limit too low.")
        return
    clear_window(window)
    # -title section
    title_frame = tk.Frame(master=window, bg="black", height=50, width=500)
    title = tk.Label(master=title_frame, text="The solution was found in "+str(nbr_itrations)+" after exploring "+str(nbr_explored)+" states.",
                     bg="black", fg="purple", font=("Arial", 12, 'bold'))
    title.place(anchor=tk.W, rely=0.5, relx=0.03)
    # -grid dection
    grid_frame = tk.Frame(master=window, bg="black", height=300, width=300)
    make_grid(grid_frame, solution[ind].mat)
    # -buttons section
    option_frame = tk.Frame(master=window, bg="black", height=50, width=500)
    auto = tk.Button(option_frame, text="auto", bg="purple")
    auto.grid(row=0, column=0, padx=10)
    previous = tk.Button(option_frame, text="previous", bg="purple")
    previous.grid(row=0, column=1, padx=10)
    next = tk.Button(option_frame, text="next", bg="purple")
    next.grid(row=0, column=2, padx=10)
    restart = tk.Button(option_frame, text="restart", bg="purple")
    restart.grid(row=0, column=3, padx=10)
    auto.bind("<Button>", lambda event: cycle())
    next.bind("<Button>", lambda event: add())
    previous.bind("<Button>", lambda event: sub())
    restart.bind("<Button>", start_game)
    # * final layout
    title_frame.pack()
    grid_frame.pack()
    option_frame.pack(pady=5)


# -open main window
window = tk.Tk()
play()
window.configure(bg='black')
window.geometry("500x400")
window.resizable(False, False)
start_game()
window.mainloop()
