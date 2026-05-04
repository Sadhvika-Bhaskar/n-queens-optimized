# import required modules
import time

MAX = 20

def printBoard(board, n, solutionCount):
    print(f"\nSolution {solutionCount}:")
    for i in range(n):
        row = [" Q " if board[i] == j else " . " for j in range(n)]
        print(''.join(row))

def solve(row, n, board, col, diag1, diag2, stats, show_solutions):
    stats['recursiveCalls'] += 1
    if row == n:
        stats['solutionCount'] += 1
        if show_solutions and stats['solutionCount'] <= 2:
            printBoard(board, n, stats['solutionCount'])
        return
    for c in range(n):
        if not col[c] and not diag1[row - c + n - 1] and not diag2[row + c]:
            board[row] = c
            col[c] = True
            diag1[row - c + n - 1] = True
            diag2[row + c] = True
            solve(row + 1, n, board, col, diag1, diag2, stats, show_solutions)
            col[c] = False
            diag1[row - c + n - 1] = False
            diag2[row + c] = False

def main():
    try:
        n = int(input("Enter value of N: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return
    if n <= 0 or n > MAX:
        print(f"Invalid input! N should be between 1 and {MAX}")
        return
    board = [0] * n
    col = [False] * n
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)
    stats = {'recursiveCalls': 0, 'solutionCount': 0}
    show_solutions = n <= 6
    if n > 6:
        print("Displaying only count for large N...")
    start = time.time()
    solve(0, n, board, col, diag1, diag2, stats, show_solutions)
    end = time.time()
    print(f"\nTotal Solutions: {stats['solutionCount']}")
    print(f"Total Recursive Calls: {stats['recursiveCalls']}")
    print(f"Execution Time: {end - start:.6f} seconds")

if __name__ == "__main__":
    main()
    