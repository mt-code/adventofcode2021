import sys


# Parse boards into a list
def parse_boards(lines):
    line_num = 0
    boards = []
    match_boards = []

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
def mark_matches(num, boards, matches):
    for board_index, board in enumerate(boards):
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                if col == num:
                    matches[board_index][row_index][col_index] = True

    return matches


# check if the current board has achieved bingo
def check_win(board):
    col = []

    for row in board:
        if all(row):
            return True

        col.append(row[0])

    return all(col)

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

    for num in draw:
        matches = mark_matches(num, boards, matches)

        for index, board in enumerate(matches):
            if check_win(board):
                print(f"Winning board: {index}")
                print(f"Winning board score: {calculate_score(boards[index], board, num)}")
                sys.exit(0)
