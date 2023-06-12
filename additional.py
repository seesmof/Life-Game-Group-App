def get_neighbours(pole, row, col):
    rows = len(pole)
    cols = len(pole[0])
    count = 0

    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1),
               (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for offset in offsets:
        offset_row = row + offset[0]
        offset_col = col + offset[1]
        if 0 <= offset_row < rows and 0 <= offset_col < cols and pole[offset_row][offset_col] == 1:
            count += 1
    return count
