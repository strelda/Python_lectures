def find_smallest_divisor(n: int) -> int:
    """
    Finds the smallest divisor of the given number n greater than 1.
    If no such divisor exists, returns n itself, indicating that n is prime.

    Parameters:
        n (int): The number to find the smallest divisor for.

    Returns:
        int: The smallest divisor of n greater than 1, or n itself if n is prime.
    """
    if n <= 1:
        return n

    d = 2
    while d < n:
        if n % d == 0:
            return d
        d += 1

    return n


def check_divisor(n: int, smallest_divisor: int) -> str:
    """Based on number n and its smallest divisor, return if the number is prime or not."""
    if smallest_divisor == n:
        return str(n) + " is prime"
    else:
        return str(n) + " can be divided by " + str(smallest_divisor)

n = int(input("Enter a number: "))
smallest_divisor = find_smallest_divisor(n)
print(check_divisor(n, smallest_divisor))


