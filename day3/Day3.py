import re
from pprint import pprint

if __name__ == '__main__':
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    with open('input.txt') as f:
        raw_content = f.read()
    valid_multiplications = re.findall(pattern, raw_content)
    pprint(valid_multiplications)
    
    result = sum([int(a) * int(b) for a, b in valid_multiplications])
    print(result)