from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()

# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False,False)


top_frame = Frame(
    root,
    bg='black',
    width=f'{utils.width_prct(100)}', 
    height=f'{utils.height_prct(25)}' 
)
top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg="black",
    width=f'{utils.width_prct(25)}',
    height = f'{utils.height_prct(75)}'
)
left_frame.place(x=0,y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width = f'{utils.width_prct(75)}',
    height = f'{utils.height_prct(75)}'
)
center_frame.place(
    x = f'{utils.width_prct(25)}',
    y = f'{utils.height_prct(25)}'
)


# creating grid of cells
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column = x , row=y)

# call the label from cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=settings.WIDTH / 10,
    y=settings.HEIGHT / 4)

Cell.randomize_mines()


# run the window
root.mainloop() 