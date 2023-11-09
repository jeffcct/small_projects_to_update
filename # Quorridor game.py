# Quorridor game
import tkinter as tk

class Player:
    def __init__(self, name):
        self.name = name
        self.pos = None
        
class Cell:
    def __init__(self):
        self.neighbours = []
        self.left = None
        self.right = None
        self.above = None
        self.below = None      
        
class Board:
    def __init__(self, length = 8):
        self.board = self.create_board()
        self.players = []
        self.length = length
        
    def add_player(self, player):
        if len(self.players) > 2 or type(player) != Player:
            return False
        
        self.players.append(player)
        return True
            
    def create_board(self):
        board = []
        for y in range(self.length):
            row = []
            for x in range(self.length):
                row.append(Cell())
            board.append(row)
            
        for x in range(self.length - 1):
            for y in range(self.length):
                
        return board
    
    def draw(canvas):
        for x in range(self.board.length):
            for y in range(self.board.length):
                
        
class Visuals: 
    def __init__(self, board, players):
        self.canvas = self.create_canvas()
        self.board = board
        self.players = players
        
    def create_canvas(self):
        window = tk.Tk()
        canvas = tk.Canvas(window, width = 1200, height = 1200)
        canvas.pack()
        self.board.draw(canvas)

        window.mainloop()
        return canvas
    
      
        


