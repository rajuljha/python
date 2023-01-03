from tkinter import *
import random
import settings
import sys

class Cell:
    all = []
    cell_count = settings.CELLS_COUNT
    cell_count_label_object = None
    def __init__(self, x, y , is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x 
        self.y = y
        self.is_opened = False
        self.is_mine_candidate = False

        # append cell objects to Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width = 12,
            height= 4
        )
        btn.bind('<Button-1>', self.left_click_actions) # Left Click
        btn.bind('<Button-2>' , self.right_click_actions) # Right Click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text = f'Cells Left: {Cell.cell_count}',
            width = 12,
            height = 4,
            bg = 'white',
            fg = 'black',
            font=('', 20)
        )
        Cell.cell_count_label_object = lbl

    @staticmethod
    def game_over_display(text_displayed):
        game_over_root = Tk()
        game_over_root.title("GAME OVER!!")
        game_over_root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
        
        game_over_label = Label(
            game_over_root,
            text = f"{text_displayed}",
            font = ("Helvetica",100)
        )
        game_over_label.pack(pady = 200)

        game_over_root.after(3000, sys.exit())
        game_over_root.mainloop()
        
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

            #if mines count is equal to cells count then player won
            if Cell.cell_count == settings.RANDOM_COUNT :
                Cell.game_over_display("YOU WON!")

        # cancel left and right click events if cell is already opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-2>')

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg="yellow",
                text = 'Marked!'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg="SystemButtonFace",
                text = ""
            )

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell    


    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x , self.y - 1),
            self.get_cell_by_axis(self.x , self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_mine(self):
        self.cell_btn_object.configure( bg= 'red' , text='Mine')
        # Logic to interrupt the game and display message that player lost
        
        Cell.game_over_display("GAME OVER!")

        
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text = self.surrounded_cells_mines_length)
            # replace the text of cell count label with newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text = f'Cells Left: {Cell.cell_count}'
                )
            # If this was a mine candidate then for safety we should configure
            #the background color to SystemButtonface
            self.cell_btn_object.configure(bg="SystemButtonFace")
        # Mark the cell as opened (use it as the last line of this method)
        self.is_opened = True

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all , settings.RANDOM_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f'Cell: ({self.x},{self.y})'