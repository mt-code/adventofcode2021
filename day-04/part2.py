# parse boards into vars
def parse_boards(lines):
    line_num, boards, match_boards = 0, [], []

    while line_num < len(lines):
        board = []
        match_board = []

        for i in range(0, 5):
            row = []
            match_row = []

            for num in lines[line_num + i].split():
                row.append(num)
                match_row.append(False)

            board.append(row)
            match_board.append(match_row)

        boards.append(board)
        match_boards.append(match_board)
        line_num += 6

    return boards, match_boards


# mark items that match the current draw
def mark_matches(num, boards, matches, completed_boards):
    for board_index, board in enumerate(boards):
        # Don't update an already bingo'd board
        if board_index in completed_boards:
            continue

        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                if col == num:
                    matches[board_index][row_index][col_index] = True

    return matches


# check if the current board has achieved bingo
def check_win(board):
    cols = {}

    for row in board:
        if all(row):
            return True

        for x in range(0, 5):
            if x not in cols:
                cols[x] = []

            cols[x].append(row[x])

    for col in cols.values():
        if all(col):
            return True

    return False


# calculate the winning boards "score"
def calculate_score(board, match_board, latest_draw):
    unmarked = 0

    for row_index, row in enumerate(match_board):
        for col_index, col in enumerate(row):
            if not col:
                unmarked += int(board[row_index][col_index])

    return unmarked * int(latest_draw)


if __name__ == '__main__':
    lines = open("input.txt").read().splitlines()
    draw = lines[0].split(',')
    lines = lines[2:]
    boards, matches = parse_boards(lines)
    completed_boards, winning_draws = [], []

    for num in draw:
        matches = mark_matches(num, boards, matches, completed_boards)

        for index, board in enumerate(matches):
            if index not in completed_boards and check_win(board):
                completed_boards.append(index)
                winning_draws.append(num)

    last_win_index = completed_boards[-1]

    print(f"Board #{last_win_index} won last with a score of: {calculate_score(boards[last_win_index], matches[last_win_index], winning_draws[-1])}")