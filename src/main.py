import tkinter as tk
import lib.GUI_util as gu
search_option = -2





window = tk.Tk()
window.configure(bg='black')
window.geometry("500x400")
window.resizable(False, False)
option = -2
intial_node = gu.node()
# * player section
moves = 0
player_node = gu.node()
# *title section
title_frame = tk.Frame(master=window, bg="black", height=50, width=500)
title = tk.Label(master=title_frame, text="Play on your own or use DFS/BFS to find the solution",
                 bg="black", fg="purple", font=("Arial", 12, 'bold'))
title.place(anchor=tk.W, rely=0.5)
settings_button = tk.Button(text="go", master=title_frame)
settings_button.place(height=30, width=30, x=460, y=10)
settings_button.bind('<Button>', open_settings)
# * grid section
grid_frame = tk.Frame(master=window, bg="black", height=300, width=300)
gu.make_grid(grid_frame, player_node.mat)
# * options section
option_frame = tk.Frame(master=window, bg="red", height=50, width=500)
# * final layout
title_frame.pack()
grid_frame.pack()
option_frame.pack()
window.mainloop()
