from primes import *

below50 = {2, 3, 5, 37, 7, 41, 11, 43, 13, 47, 17, 19, 23, 29, 31}
below_million_count = 78498


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


def test_correctness_all_6k_plus_minus_1_single_looping():
    res_below50 = all_6k_plus_minus_1_single_looping(50)

    assert(res_below50 == below50)


def test_correctness_sieve_of_sundaram():
    res_below50 = sieve_of_sundaram(50)

    assert(res_below50 == below50)


def test_large_correctness_sieve_of_erastothenes():
    count = len(sieve_of_eratosthenes(10**6))

    assert(count == below_million_count)


def test_large_correctness_all_odd_to_sqrt():
    count = len(all_odd_to_sqrt(10**6))

    assert(count == below_million_count)


def test_large_correctness_all_6k_plus_minus_1():
    count = len(all_6k_plus_minus_1(10**6))

    assert(count == below_million_count)


def test_large_correctness_sieve_of_atkin():
    count = len(sieve_of_atkin(10**6))

    assert(count == below_million_count)


def test_large_correctness_all_6k_plus_minus_1_single_looping():
    count = len(all_6k_plus_minus_1_single_looping(10**6))

    assert(count == below_million_count)


def test_large_correctness_all_sieve_of_sundaram():
    count = len(sieve_of_sundaram(10**6))

    assert(count == below_million_count)