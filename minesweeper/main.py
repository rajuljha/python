from tkinter import *
import settings
import utils

root = Tk() #start the panel shell

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

# run the window
root.mainloop() 