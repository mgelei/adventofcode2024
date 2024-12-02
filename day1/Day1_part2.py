if __name__ == '__main__':
    left = []
    right = []
    similarity = 0
    
    with open('input.txt') as f:
        for line in f:
            l, _, _, r = line.split(' ')
            left.append(int(l))
            right.append(int(r))
            
    left = sorted(left)
    right = sorted(right)
    
    for i in range(0, len(left)):
        item = left[i]
        similarity += (right.count(item) * item)
        
    print(similarity)