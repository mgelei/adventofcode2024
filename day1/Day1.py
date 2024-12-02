from os.path import split

if __name__ == '__main__':
    left = []
    right = []
    distance = 0
    
    with open('input.txt') as f:
        for line in f:
            l, _, _, r = line.split(' ')
            left.append(int(l))
            right.append(int(r))
            
    left = sorted(left)
    right = sorted(right)
    
    for i in range(0, len(left)):
        distance += abs(left[i] - right[i])
        
    print(distance)