import tkinter as tk
from lib.node_class import node
#*variables

#-search_option==-2 mean DFS
#-search_option==-1 mean BFS
#-search_option>0 mean DFL
#*methods
def make_grid(frame, mat):
    i = 0
    j = 0
    for row in mat:
        for cell in row:
            grid_cell = tk.Frame(master=frame, height=80,
                                 width=80, bg="purple")
            grid_cell.grid(row=i, column=j, padx=10, pady=10)
            if cell != 0:
                tk.Label(master=grid_cell, text=str(cell), bg="purple", font=(
                    "Arial", 30)).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            else:
                grid_cell.destroy()
            j += 1
        i += 1
        j = 0

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
        settings.destroy()
    settings = tk.Tk()
    v = tk.IntVar()
    global search_option
    v.set(search_option)  # initializing the choice
    input_warning = tk.StringVar()
    input_warning.set("")

    other = tk.Frame()
    tk.Label(other, text="DFL's Limit:").grid(row=0)
    input = tk.Entry(other, width=5)
    input.grid(row=0, column=1)
    other.pack()
    tk.Label(settings,
             text="Choose the search algorithm:",
             justify=tk.LEFT,
             padx=20).pack()

    tk.Radiobutton(settings, text="DFS", padx=20,
                   variable=v, value=-2).pack()
    tk.Radiobutton(settings, text="BFS", padx=20,
                   variable=v, value=-1).pack()
    tk.Radiobutton(settings, text="DFL", padx=20,
                   variable=v, value=0).pack()
    tk.Label(settings, fg="red", textvariable=input_warning).pack()
    bt = tk.Button(text="apply")
    bt.pack()
    bt.bind('<Button>', submit)
    settings.mainloop()
