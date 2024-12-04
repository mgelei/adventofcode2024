from pprint import pprint

def is_inside(i, j):
    return 0 <= i < length and 0 <= j < length

if __name__ == '__main__':
    matrix = []
    counter = 0

    with open('input', 'r') as f:
        for line in f:
            matrix.append(list(line.strip()))
    length = len(matrix)

    for i in range(length):
        for j in range(length):
            if matrix[i][j] != 'X':
                continue
            for direction_x in [-1, 0, 1]:
                for direction_y in [-1, 0, 1]:
                    if (direction_x, direction_y) == (0, 0):
                        continue
                    if is_inside(i + 3 * direction_x, j + 3 * direction_y):
                        if ''.join(matrix[i + k * direction_x][j + k * direction_y] for k in range(4)) == 'XMAS':
                            counter += 1
    print(counter)