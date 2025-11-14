from two_sum import two_sum

def test_examples():
    assert two_sum([2,7,11,15], 9) == (0,1)
    

def test_negative_numbers():
    assert two_sum([3,2,4], 6) == (1,2)
    assert two_sum([-1,-2,-3,-4,-5], -8) == (2,4)

def test_single_pair_middle():
    nums = [1,5,3,4,2]
    i, j = two_sum(nums, 7)
    assert nums[i] + nums[j] == 7

def test_no_solution():
    
    assert two_sum([1,2,3], 100) is None

if __name__ == "__main__":
    test_examples()
    test_negative_numbers()
    test_single_pair_middle()
    test_no_solution()
    print("All two_sum tests passed!")
