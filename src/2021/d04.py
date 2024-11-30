def parse(data) -> dict[int, tuple]:
    bingoNums, *boards = data.split("\n\n")
    bingoNums = bingoNums.strip().split(",")
    for board_idx, board in enumerate(boards):
        board = board.split("\n")
        for row_idx, row in enumerate(board):
            board[row_idx] = row.split()
        boards[board_idx] = board
    return {1: (bingoNums, boards), 2: (bingoNums, boards)}


def checkBingo(board):
    for row in board:
        if row == ["X"] * 5:
            return True
    for col_num in range(5):
        col = [row[col_num] for row in board]
        if col == ["X"] * 5:
            return True
    return False


def markBoard(board, bingoNum):
    for row in board:
        for idx, num in enumerate(row):
            if num == bingoNum:
                row[idx] = "X"
                return True
    return False


def part1(bingoNums, boards):
    bingoNums = iter(bingoNums.copy())
    bingoBoard = bingoNum = None

    while not bingoBoard:
        bingoNum = next(bingoNums)
        markedBoards = [board for board in boards if markBoard(board, bingoNum)]

        for markedBoard in markedBoards:
            if checkBingo(markedBoard):
                bingoBoard = markedBoard
                break

    sumOfBoard = 0
    for row in bingoBoard:
        for num in row:
            if num != "X":
                sumOfBoard += int(num)

    return sumOfBoard * int(bingoNum)


def part2(bingoNums, boards):
    bingoNums = iter(bingoNums.copy())
    bingoBoard = bingoNum = None

    while not bingoBoard:
        bingoNum = next(bingoNums)
        markedBoards = [board for board in boards if markBoard(board, bingoNum)]

        for markedBoard in markedBoards:
            if checkBingo(markedBoard):
                if len(boards) > 1:
                    boards.remove(markedBoard)
                else:
                    bingoBoard = markedBoard
                    break

    sumOfBoard = 0
    for row in bingoBoard:
        for num in row:
            if num != "X":
                sumOfBoard += int(num)

    return sumOfBoard * int(bingoNum)
