from tkinter import Button,Label
import random
import settings

class Cell:
    all = []
    def __init__(self, x, y , is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x 
        self.y = y

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

    def create_cell_count_label(self,location):
        lbl = Label(
            location,
            text = f'Cells Left: {settings.CELLS_COUNT}'
        )
        return lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")

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
        # Logic to interrupt the game and display message that player lost
        self.cell_btn_object.configure( bg= 'red' , text='Mine')
    
    def show_cell(self):
        self.cell_btn_object.configure(text = self.surrounded_cells_mines_length)

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all , settings.RANDOM_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f'Cell: ({self.x},{self.y})'