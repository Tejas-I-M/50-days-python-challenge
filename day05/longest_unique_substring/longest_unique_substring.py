"""
Day 05 - Longest Substring Without Repeating Characters
"""

def longest_unique_substring(s: str):

    if s is None:
        return 0,''
    
    last_seen={}
    left =0
    max_len=0
    max_start =0

    for right,ch in enumerate(s):
        if  ch in last_seen and last_seen[ch]>= left:
            left = last_seen[ch]+1
        last_seen[ch]=right
        window_len =  right - left +1
        if window_len >max_len:
            max_len = window_len
            max_start = left
    return max_len,s[max_start:max_start+max_len]

if __name__ == "__main__":
    user_input =input("enter a string:")
    length,susbstring = longest_unique_substring(user_input)

    print("result")
    print("longest substring without repeating characters:")
    print("Length:",length)
    print("Substring:",repr(susbstring))
