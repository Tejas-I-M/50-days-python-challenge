""" Day 09 - Top K  Frequent elements"""

def parse_nums(line):
    if not line:
        return []
    return [int(x) for x in line.replace(',',' ').split() if x.strip() !='']

def top_k_fraquent(nums, k):
    if not nums or k<=0:
        return []
    
    freq ={}
    for x  in nums:
        freq[x] = freq.get(x,0) + 1

    n = len(nums)
    buckets = [[] for _ in range(n+1)]
    for num, count in freq.items():
        buckets[count].append(num)
    res=[]
    for f in range(n,0,-1):
        if buckets[f]:
            for num  in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res
    return res

if __name__=="__main__":
    print("Top K frequent elems")
    line = input("Enter integers (space or comma seperated):").strip()
    nums = parse_nums(line)
    try :
        k = int(input("Enter k(no. of top frequent elem):").strip())
    except:
        print("Invalid k.using k =1")
        k = 1

    result = top_k_fraquent(nums,k)
    print("input:",nums)
    print(f"top {k} frequent elements:",result)
