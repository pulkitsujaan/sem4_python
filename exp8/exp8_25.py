class TicTacToe:
    def __init__(self):
        self.board  = [" "] * 9
        self.current = "X"

    def display(self):
        b = self.board
        print(f"{b[0]}|{b[1]}|{b[2]}")
        print(f"{b[3]}|{b[4]}|{b[5]}")
        print(f"{b[6]}|{b[7]}|{b[8]}")

    def make_move(self, pos):
        if self.board[pos] == " ":
            self.board[pos] = self.current
            self.current = "O" if self.current == "X" else "X"
        else:
            print("Cell taken!")

    def check_winner(self):
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
        for a,b,c in wins:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return None

g = TicTacToe()
for move in [0, 4, 1, 3, 2]:   # X wins on top row
    g.make_move(move)
    g.display()
    w = g.check_winner()
    if w:
        print(f"Winner: {w}")
        break