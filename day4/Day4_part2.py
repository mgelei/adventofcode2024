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
            if matrix[i][j] != 'A': # "A" would be the middle letter
                continue
            if not is_inside(i+1, j+1) or not is_inside(i-1, j-1) or not is_inside(i+1, j-1) or not is_inside(i-1, j+1):
                continue
            if not (matrix[i-1][j-1], matrix[i+1][j+1]) in (('M', 'S'), ('S', 'M')):
                continue
            if not (matrix[i+1][j-1], matrix[i-1][j+1]) in (('M', 'S'), ('S', 'M')):
                continue
            counter += 1
    
    print(counter)