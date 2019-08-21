from mean import *

def test_ints():
    nums = [4,5, 28, 3]
    obs = mean(nums)
    exp = 10
    assert obs == exp
