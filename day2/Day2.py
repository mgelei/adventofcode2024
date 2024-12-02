from pprint import pprint

def is_safe(report):
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
    increasing = True
    decreasing = True
    adjacent = True
    
    for i in range(0, len(report) - 1):
        left = report[i]
        right = report[i + 1]
        if(left > right):
            increasing = False
        if(left < right):
            decreasing = False
        if(abs(left - right) > 3 or abs(left - right) < 1):
            adjacent = False
            
    print(increasing, decreasing, adjacent)
            
    return (increasing or decreasing) and adjacent

if __name__ == '__main__':
    reports = []
    
    with open('input.txt') as f:
        reports = [[int(num) for num in line.split()] for line in f]
        
    safe_reports = [report for report in reports if is_safe(report)]
    print(len(safe_reports))