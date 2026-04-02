"""
find if n is multiple of m such that n = mi
"""


def is_multiple(n, m):
    return n % m == 0


"""
find is even but your function should not use multiplication, modulo or division operator
"""


def is_even(k):
    """
    Using bitwise AND operator to check if number is even
    """
    print(f"binar representation of {k} is {bin(k)}")
    return (k & 1) == 0


if __name__ == "__main__":
    print(is_even(333))
