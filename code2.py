def solveNQueens(n):
    res = []
    board = [["."] * n for _ in range(n)]

    cols = set()      # columns where queens are placed
    pos_diag = set()  # (r + c) positive diagonals
    neg_diag = set()  # (r - c) negative diagonals

    def backtrack(r):
        # Base case: all queens placed
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            # Place queen
            board[r][c] = "Q"
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)

            # Recurse to next row
            backtrack(r + 1)

            # Remove (backtrack)
            board[r][c] = "."
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)

    backtrack(0)
    return res


# Example usage
if __name__ == "__main__":
    n = 4
    solutions = solveNQueens(n)
    print(f"Total Solutions for n = {n}: {len(solutions)}\n")
    for s in solutions:
        for row in s:
            print(row)
        print()