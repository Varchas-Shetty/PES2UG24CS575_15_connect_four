class AI:
    def choose_column(self, board, me="O", opponent="X"):
        legal = [c for c in range(len(board.grid[0])) if board.grid[0][c] == "."]
        if not legal:
            return None

        # Take a win now, then block the opponent's immediate win.
        for token in (me, opponent):
            for col in legal:
                row = next(r for r in range(len(board.grid) - 1, -1, -1)
                           if board.grid[r][col] == ".")
                board.grid[row][col] = token
                wins = board.winner(token)
                board.grid[row][col] = "."
                if wins:
                    return col

        # Prefer the center, which gives the computer more possible lines.
        center = len(board.grid[0]) // 2
        return min(legal, key=lambda col: abs(col - center))
