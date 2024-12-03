import re
from pprint import pprint

if __name__ == '__main__':
    pattern = re.compile(r'''(don't\(\))|(do\(\))|(mul\((\d+),(\d+)\))''')
    do = True
    result = 0
    
    with open('input.txt') as f:
        raw_content = f.read()
    commands = re.findall(pattern, raw_content)
    pprint(commands)
    
    for cmd in commands:
        match cmd:
            case ("don't()", _, _, _, _):
                do = False
            case (_, "do()", _, _, _):
                do = True
            case (_, _, _, a, b):
                result += int(a) * int(b) if do else 0
                
    print(result)