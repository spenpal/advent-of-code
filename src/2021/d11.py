def parse(data: str) -> dict[int, tuple]:
    energy = data.splitlines()
    energy = [list(map(int, list(row))) for row in energy]
    return {1: (energy,), 2: (energy,)}


def checkFlash(energy, row, col):
    if 0 <= energy[row][col] <= 9:
        return 0
    energy[row][col] = 0
    row_length, col_length = len(energy), len(energy[0])
    nextFlashes = 0

    for row_bit in [-1, 0, 1]:
        for col_bit in [-1, 0, 1]:
            if row_bit == col_bit == 0:
                continue

            nextRow, nextCol = row + row_bit, col + col_bit
            if (0 <= nextRow < row_length) and (0 <= nextCol < col_length):
                energy[nextRow][nextCol] += energy[nextRow][nextCol] != 0
                nextFlashes += checkFlash(energy, nextRow, nextCol)

    return 1 + nextFlashes


def part1(energy):
    row_length, col_length = len(energy), len(energy[0])
    flash_count = 0
    for step in range(100):
        energy = [list(map(lambda x: x + 1, row)) for row in energy]
        flash_count += sum(checkFlash(energy, row, col) for row in range(row_length) for col in range(col_length))
    return flash_count


def part2(energy):
    row_length, col_length = len(energy), len(energy[0])
    total_octopuses = row_length * col_length
    flash_count = step = 0

    while flash_count != total_octopuses:
        energy = [list(map(lambda x: x + 1, row)) for row in energy]
        flash_count = sum(checkFlash(energy, row, col) for row in range(row_length) for col in range(col_length))
        step += 1

    return step
