from collections import deque

def solution(labyrinth):
    rows, cols = len(labyrinth), len(labyrinth[0])

    def valid_move(r, c, orientation):
        if orientation == 'H':
            if c + 2 >= cols or r >= rows or c < 0:  
                return False
            return all(labyrinth[r][c + i] == '.' for i in range(3))
        else:  # orientation == 'V'
            if r + 2 >= rows or c >= cols or r < 0:  
                return False
            return all(labyrinth[r + i][c] == '.' for i in range(3))

    def can_rotate(r, c, orientation):
        if orientation == 'H':  # Centro de rotación en (r, c+1)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= r+i < rows and 0 <= c+j+1 < cols and labyrinth[r+i][c+j+1] == '#':
                        return False
        else:  # orientation == 'V'
            for i in range(-1, 2):  # Centro de rotación está en (r+1, c)
                for j in range(-1, 2):
                    if 0 <= r+i+1 < rows and 0 <= c+j < cols and labyrinth[r+i+1][c+j] == '#':
                        return False
        return True


    visited = set()
    q = deque() 
    q.append(((0, 0), 'H', 0))  # posición, orientación, número de movimientos - Estado Inicial

    while q:
        (r, c), orientation, moves = q.popleft()

        # Si llegamos a la posición final
        if (orientation == 'H' and r == rows - 1 and c == cols - 3) or (orientation == 'V' and r == rows - 3 and c == cols - 1):
            return moves

        # Probamos todos los movimientos
        for dr, dc, do in [(1, 0, '0'), (-1, 0, '0'), (0, 1, '0'), (0, -1, '0'), (0, 0, 'R')]:
            nr, nc, no = r + dr, c + dc, orientation if do == '0' else ('H' if orientation == 'V' else 'V')

            # Si las coordenadas están fuera de los límites, continúa al siguiente ciclo
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                continue

            # Si es una rotación, verificamos si es posible
            if do == 'R' and not can_rotate(r, c, orientation):
                continue

            if (nr, nc, no) not in visited and valid_move(nr, nc, no):
                visited.add((nr, nc, no))
                q.append(((nr, nc), no, moves + 1))

    return -1


# --------------------------------- TEST ----------------------------------

labyrinths = [
    [[".",".",".",".",".",".",".",".","."],
    ["#",".",".",".","#",".",".",".","."],
    [".",".",".",".","#",".",".",".","."],
    [".","#",".",".",".",".",".","#","."],
    [".","#",".",".",".",".",".","#","."]],
    [[".", ".", ".", ".", ".", ".", ".", ".", "."],
     ["#", ".", ".", ".", "#", ".", ".", "#", "."],
     [".", ".", ".", ".", "#", ".", ".", ".", "."],
     [".", "#", ".", ".", ".", ".", ".", "#", "."],
     [".", "#", ".", ".", ".", ".", ".", "#", "."]],
    [[".", ".", "."],
     [".", ".", "."],
     [".", ".", "."]],
    [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", "#", ".", ".", ".", ".", "#", ".", ".", "."],
     [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", "#", ".", ".", ".", "#", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
]

results = [11, -1, 2, 16]
for labs, res in zip(labyrinths, results):
    print(solution(labs), "expected:", res)
