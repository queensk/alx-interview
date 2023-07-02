def isWinner(x, nums):
    """
    Determines the winner of the most rounds of a prime game
    """

    # A helper function that returns True if n is prime, False otherwise
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # A helper function that returns the number of primes in the range [1, n]
    def count_primes(n):
        count = 0
        for i in range(1, n + 1):
            if is_prime(i):
                count += 1
        return count

    # A variable to keep track of the score difference between Maria and Ben
    score = 0

    # Loop through each round
    for n in nums:
        primes = count_primes(n)
        if primes % 2 == 1:
            score += 1
        else:
            score -= 1

    if score > 0:
        return "Maria"
    elif score < 0:
        return "Ben"
    else:
        return None
