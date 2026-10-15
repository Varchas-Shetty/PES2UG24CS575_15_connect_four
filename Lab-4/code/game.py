from board import Board
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = "X"

    def run(self):
        print("Connect Four — you are X.")
        while True:
            self.board.print()
            if self.turn == "X":
                try:
                    raw = input("Column (1-7), or q: ").strip().lower()
                except EOFError:
                    print("Input closed. Game ended.")
                    return
                if raw == "q":
                    print("Game ended.")
                    return
                try:
                    col = int(raw) - 1
                except ValueError:
                    print("Enter a column from 1 to 7, or q to quit.")
                    continue
                if not 0 <= col < 7:
                    print("Choose a column from 1 to 7.")
                    continue
            else:
                col = self.ai.choose_column(self.board)

            row = None if col is None else self.board.drop(col, self.turn)
            if row is None:
                print("No legal move is available." if col is None else "Column full. Choose another.")
                if self.turn == "O":
                    return
                continue
            print(f"{self.turn} dropped a disc in column {col + 1}.")

            if self.board.winner(self.turn):
                self.board.print()
                print(self.turn, "wins!")
                return
            if self.board.full():
                self.board.print()
                print("Draw.")
                return

            self.turn = "O" if self.turn == "X" else "X"
