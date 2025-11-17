"""Day 07 - Longest Increasing Subsequence"""

from bisect import bisect_left

def longest_increasing_sebsequence(arr):
    n=len(arr)
    if n==0:
        return 0,[]
    tails=[]
    tails_idx=[]
    prev = [-1]*n

    for i,x in enumerate(arr):
        pos = bisect_left(tails,x)

        if pos == len(tails):
            tails.append(x)
            tails_idx.append(i)
        else:
            tails[pos]=x
            tails_idx[pos] =i
        if pos>0:
            prev[i] = tails_idx[pos-1]
        else:
            prev[i] =-1

    lis_lenght=len(tails)
    lis=[]
    k= tails_idx[-1]
    while k !=-1:
        lis.append(arr[k])
        k = prev[k]

    lis.reverse()

    return lis_lenght, lis

def parse_input(line):
    if not line:
        return []
    tokens = [t.strip() for t in line.replace(',','').split()]
    return [int(t) for t in tokens if t!='']

if __name__=="__main__":
    print('longest  increasing subsequence - interactive')
    print("enter integers seperated by sopaces or commas(e.g. 10 9 2 5 3 7 101 18)")
    s = input('input array:').strip()
    arr = parse_input(s)
    length,subseq = longest_increasing_sebsequence(arr)

    print('result')
    print('array',arr)
    print('lis length:',length)
    print('one lis:',subseq)


        
        

