def is_king_in_check(*board_rows):
    try:
        board = [list(row) for row in board_rows]
        size = len(board)

        # ตรวจสอบว่ากระดานเป็นสี่เหลี่ยม
        if not all(len(row) == size for row in board):
            print("Invalid board")
            return

        # หาตำแหน่งของ King
        king_pos = None
        for y in range(size):
            for x in range(size):
                if board[y][x] == 'K':
                    king_pos = (y, x)
                    break
            if king_pos:
                break

        if not king_pos:
            print("Invalid board: No King")
            return

        yk, xk = king_pos

        directions = {
            'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],
            'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
            'P': [(-1, -1), (-1, 1)]  # Pawn attacks upward
        }

        def scan(y, x, dy, dx):
            ny, nx = y + dy, x + dx
            while 0 <= ny < size and 0 <= nx < size:
                cell = board[ny][nx]
                if cell == '.':
                    ny += dy
                    nx += dx
                    continue
                return cell
            return None

        # ตรวจทุกทิศ
        for piece, dirs in directions.items():
            for dy, dx in dirs:
                if piece == 'P':
                    ny, nx = yk + dy, xk + dx
                    if 0 <= ny < size and 0 <= nx < size and board[ny][nx] == 'P':
                        print("Success")
                        return
                else:
                    ny, nx = yk + dy, xk + dx
                    while 0 <= ny < size and 0 <= nx < size:
                        cell = board[ny][nx]
                        if cell == '.':
                            ny += dy
                            nx += dx
                            continue
                        elif cell == piece or (piece == 'Q' and cell in ['Q']):
                            print("Success")
                            return
                        else:
                            break  # blocked by other piece

        print("Fail")

    except Exception:
        # ไม่ทำอะไรหากเกิด error ตามโจทย์
        return