from pprint import pprint


def rotate(direction):
    if direction == up:
        return right
    elif direction == right:
        return down
    elif direction == down:
        return left
    elif direction == left:
        return up

def is_inbounds(x, y):
    return 0 <= x < len(map) and 0 <= y < len(map[0])

if __name__ == "__main__":
    map = []
    unvisited = "."
    visited = "X"
    obstacle = "#"
    guard_origin = "^"
    
    with open('input.txt') as f:
        for line in f:
            map.append(list(line.strip()))
    
    up = (-1, 0)
    down = (1, 0)
    left = (0, -1)
    right = (0, 1)
    direction = up
    
    guard = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == guard_origin:
                guard = [i, j]
                break
        else:
            continue
        break
        
    print(guard)
    
    while True:
        map[guard[0]][guard[1]] = visited
        next_step = [guard[0] + direction[0], guard[1] + direction[1]]
        if not is_inbounds(*next_step):
            break
        
        next_step_status = map[guard[0] + direction[0]][guard[1] + direction[1]]
        if next_step_status != obstacle:
            guard[0] += direction[0]
            guard[1] += direction[1]
        elif next_step_status == obstacle:
            direction = rotate(direction)
        else:
            break
    
    print(guard)
    
    for l in map:
        print("".join(l))
    
    print(sum([row.count(visited) for row in map]))