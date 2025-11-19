"""Day 08 - Merge intervals"""

def parse_intervals(line: str):
    """Parse a line like:'1 3, 2 6, 8 10' into [[1,3],[2,6],[8,10]]"""

    if not line:
        return  []
    parts = [p.strip() for p in line.split(',')]
    intervals = []
    for p in parts:
        if not p:
            continue
        nums =[int(x) for x in p.replace(',',' ').split()]
        if len(nums) >=2:
            intervals.append([nums[0],nums[1]])
    return intervals

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key =lambda x:x[0])

    res=[]
    current = intervals[0]

    for it in intervals[1:]:
        if it[0] <=current[1]:
            current[1] = max(current[1],it[1])
        else:
            res.append(current)
            current = it
    res.append(current)
    return res
if __name__=='__main__':
    print("merge intervals")
    print("enter the inervals like:1 3,2 6, 8 10,15 18")
    line = input("input intervals:").strip()
    intervals = parse_intervals(line)
    merged = merge_intervals(intervals)
    print("input:",intervals)
    print('merged',merged)