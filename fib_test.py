from fib import *

def test_fib0():
    obs = fib(0)
    assert obs == 1

def test_fib1():
    obs = fib(1)
    assert obs == 1

def test_fib6():
    obs = fib(6)
    assert obs == 8
