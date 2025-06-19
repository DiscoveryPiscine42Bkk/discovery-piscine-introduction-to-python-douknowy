def checkmate(board_str):
    board = [list(row) for row in board_str.splitlines()]
    n = len(board)

    # หา position ของ King
    king_pos = None
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break
    if not king_pos:
        # ไม่มี King ในบอร์ด => พิมพ์อะไรดี? ปล่อยเงียบหรือ Fail ก็ได้
        print("Fail")
        return

    kr, kc = king_pos

    # ฟังก์ชันช่วยตรวจสอบว่าตำแหน่ง (r,c) อยู่ในบอร์ดไหม
    def inside(r, c):
        return 0 <= r < n and 0 <= c < n

    # 1. ตรวจสอบ Pawn: Pawn โจมตีแบบทแยงหน้าไปด้านบน (คิดว่า Pawn เป็นฝ่ายตรงข้ามขึ้นข้างบน)
    # สมมติ Pawn ขึ้นไปบนบอร์ดโจมตี King
    for dc in [-1, 1]:
        pr, pc = kr - 1, kc + dc
        if inside(pr, pc) and board[pr][pc] == 'P':
            print("Success")
            return

    # 2. ตรวจสอบ Bishop และ Queen (ในแนวทแยง)
    directions_bishop = [(-1,-1), (-1,1), (1,-1), (1,1)]
    for dr, dc in directions_bishop:
        r, c = kr + dr, kc + dc
        while inside(r, c):
            if board[r][c] != '.':
                if board[r][c] == 'B' or board[r][c] == 'Q':
                    print("Success")
                    return
                else:
                    break
            r += dr
            c += dc

    # 3. ตรวจสอบ Rook และ Queen (ในแนวตั้งแนวนอน)
    directions_rook = [(-1,0), (1,0), (0,-1), (0,1)]
    for dr, dc in directions_rook:
        r, c = kr + dr, kc + dc
        while inside(r, c):
            if board[r][c] != '.':
                if board[r][c] == 'R' or board[r][c] == 'Q':
                    print("Success")
                    return
                else:
                    break
            r += dr
            c += dc

    # ถ้าไม่เจออะไร
    print("Fail")