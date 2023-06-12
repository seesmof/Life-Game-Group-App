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


def update_pole(pole):
    global cycle
    new_pole = []
    for row in range(len(pole)):
        new_row = []
        for col in range(len(pole[row])):
            cell = pole[row][col]

            live_neighbours = get_neighbours(pole, row, col)

            if cell == 1:
                if live_neighbours in [2, 3]:
                    new_row.append(1)
                else:
                    cycle += 1
                    new_row.append(0)
            else:
                if live_neighbours == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)

        new_pole.append(new_row)
    return new_pole
