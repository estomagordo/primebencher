from primes import *

below50 = {2, 3, 5, 37, 7, 41, 11, 43, 13, 47, 17, 19, 23, 29, 31}


def test_correctness_sieve_of_erastothenes():
    res_below50 = sieve_of_eratosthenes(50)

    assert(res_below50 == below50)


def test_correctness_all_odd_to_sqrt():
    res_below50 = all_odd_to_sqrt(50)

    assert(res_below50 == below50)


def test_correctness_all_6k_plus_minus_1():
    res_below50 = all_6k_plus_minus_1(50)

    assert(res_below50 == below50)


def test_correctness_sieve_of_atkin():
    res_below50 = sieve_of_atkin(50)

    assert(res_below50 == below50)