def shift_left(row):
    compressed = [x for x in row if x != 0]
    
    merged = []
    score = 0
    i = 0
    while i < len(compressed):
        if i + 1 < len(compressed) and compressed[i] == compressed[i + 1]:
            new_value = compressed[i] * 2
            merged.append(new_value)
            score += new_value
            i += 2
        else:
            merged.append(compressed[i])
            i += 1
    
    result = merged + [0] * (4 - len(merged))
    
    return result, score


def shift_right(row):
    reversed_row = row[::-1]
    shifted_reversed, score = shift_left(reversed_row)
    result = shifted_reversed[::-1]
    return result, score


def move_left(board):
    new_board = []
    total_score = 0
    
    for row in board:
        new_row, row_score = shift_left(row)
        new_board.append(new_row)
        total_score += row_score
    
    return new_board, total_score


def move_right(board):
    new_board = []
    total_score = 0
    
    for row in board:
        new_row, row_score = shift_right(row)
        new_board.append(new_row)
        total_score += row_score
    
    return new_board, total_score


def move_up(board):
    transposed = [[board[j][i] for j in range(4)] for i in range(4)]
    shifted_transposed, total_score = move_left(transposed)
    new_board = [[shifted_transposed[j][i] for j in range(4)] for i in range(4)]
    return new_board, total_score


def move_down(board):
    transposed = [[board[j][i] for j in range(4)] for i in range(4)]
    shifted_transposed, total_score = move_right(transposed)
    new_board = [[shifted_transposed[j][i] for j in range(4)] for i in range(4)]
    return new_board, total_score


def can_move(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                return True
    
    for row in range(4):
        for col in range(3):
            if board[row][col] == board[row][col + 1]:
                return True
    
    for col in range(4):
        for row in range(3):
            if board[row][col] == board[row + 1][col]:
                return True
    
    return False


def is_board_changed(old_board, new_board):
    for row in range(4):
        for col in range(4):
            if old_board[row][col] != new_board[row][col]:
                return True
    return False